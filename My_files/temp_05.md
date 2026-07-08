## Part 5.5: Evaluating the RAG Pipeline with RAGAS (`notebooks/week_1/05-RAG-Evals.ipynb`)

### Overview
This final notebook closes the loop on our RAG architecture. We have a pipeline, and we have a synthetic evaluation dataset. Now, we use the **RAGAS** (Retrieval Augmented Generation Assessment) framework to score our pipeline against the dataset. This allows us to quantify performance and track improvements over time.

### Step 1: Loading the Evaluation Dataset
We start by retrieving the dataset we uploaded to LangSmith in the previous step.

```python
from langsmith import Client

client = Client()
dataset = client.read_dataset(dataset_name="rag-evaluation-dataset")

# Pull an example to evaluate
reference_input = list(client.list_examples(dataset_id=dataset.id, limit=10))[0].inputs
reference_output = list(client.list_examples(dataset_id=dataset.id, limit=10))[0].outputs
```
*   **The "Why"**: We need the `reference_input` (the question) to feed into our pipeline, and the `reference_output` (the ground truth answer and context IDs) to compare against our pipeline's output.

### Step 2: Running the RAG Pipeline
We define a slightly modified `rag_pipeline` function. Instead of just returning the text answer, it returns a dictionary containing all intermediate states (the retrieved contexts, IDs, and scores).

```python
def rag_pipeline(question, top_k=5):
    # ... (Retrieval and Generation logic) ...
    
    final_result = {
        "answer": answer,
        "question": question,
        "retrieved_context_ids": retrieved_context["retrieved_context_ids"],
        "retrieved_context": retrieved_context["retrieved_context"],
        "similarity_scores": retrieved_context["similarity_scores"]
    }
    return final_result

# Run the pipeline on the test question
result = rag_pipeline(reference_input["question"])
```

### Step 3: Setting up RAGAS Evaluators
RAGAS evaluates two distinct parts of our pipeline: **Generation** (how good the LLM's answer is) and **Retrieval** (how good Qdrant's search was).

```python
from ragas.dataset_schema import SingleTurnSample 
from ragas.metrics import IDBasedContextPrecision, IDBasedContextRecall, Faithfulness, ResponseRelevancy
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Initialize the "Judge" LLM used for evaluation
ragas_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
ragas_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small"))
```
*   **The "Judge" LLM**: RAGAS uses an LLM to grade our LLM. Here, we configure `gpt-4o-mini` (or an equivalent model) as the objective scorer.

### Step 4: Generation Metrics (Faithfulness & Relevancy)
These metrics determine if the LLM is behaving correctly *given* the retrieved context.

```python
async def ragas_faithfulness(run, example):
    sample = SingleTurnSample(
        user_input=run["question"],
        response=run["answer"],
        retrieved_contexts=run["retrieved_context"]
    )
    scorer = Faithfulness(llm=ragas_llm)
    return await scorer.single_turn_ascore(sample)
```
*   **`Faithfulness`**: Measures hallucinations. Does the `answer` contain information that is *not* present in the `retrieved_contexts`? If yes, the score drops.
*   **`ResponseRelevancy`**: Measures if the `answer` actually addresses the user's `question`. It penalizes evasive or overly verbose, off-topic answers.

### Step 5: Retrieval Metrics (Precision & Recall)
These metrics determine if our Vector Database and Embedding model are finding the right documents.

```python
async def ragas_context_precision_id_based(run, example):
    sample = SingleTurnSample(
        retrieved_context_ids=run["retrieved_context_ids"],
        reference_context_ids=example["reference_context_ids"]
    )
    scorer = IDBasedContextPrecision()
    return await scorer.single_turn_ascore(sample)
```
*   **`IDBasedContextPrecision`**: Of the chunks we retrieved (`retrieved_context_ids`), how many were actually relevant (in the `reference_context_ids`)? And were the most relevant ones ranked at the top?
*   **`IDBasedContextRecall`**: Did we manage to retrieve *all* the relevant chunks that existed in the database? If the ground truth required 3 chunks, and we only retrieved 2 of them, our recall score drops.

> [!TIP]
> **Continuous Improvement**: By automating these evaluations, we can confidently experiment with different chunk sizes, embedding models, or prompts. If a change improves our RAGAS scores across the dataset, we know it's safe to deploy to production.

---
