## Part 5.4: Generating Synthetic Evaluation Data (`notebooks/week_1/04-evaluation-dataset.ipynb`)

### Overview
Before deploying a RAG system to production, we must measure its accuracy and reliability. However, creating a comprehensive evaluation dataset manually is extremely time-consuming. This notebook demonstrates a modern AI engineering technique: using a powerful LLM (like Gemini) to generate a synthetic evaluation dataset based on our own data, and then uploading it to an evaluation tracking platform (LangSmith).

### Step 1: Downloading Context from Qdrant
To generate questions about our products, the LLM first needs to know what products exist. 

```python
# Download 100 product entries from our local Vector DB
all_points = qdrant_client.scroll(
    collection_name="Amazon-items-collection-03",
    limit=100,
    offset=None,
    with_payload=True,
    with_vectors=False # We only need the text, not the numbers
)

# Format the data into a simple list of dictionaries
all_context = [{"id": data.payload["parent_asin"], "text": data.payload["description"]} for data in all_points[0]]
```
*   **The "Why"**: We extract a sample of our actual product data from Qdrant. We explicitly ask for `with_payload=True` (to get the text) but `with_vectors=False` (to save memory, since the LLM can't read vector numbers).

### Step 2: Prompt Engineering for Synthetic Data Generation
We create a highly specific `SYSTEM_PROMPT` to instruct Gemini on how to act as a dataset generator.

```python
# 1. Define the exact JSON structure we expect back
output_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "Suggested question."},
            "chunk_ids": {"type": "array", "items": {"type": "string"}},
            "answer_example": {"type": "string", "description": "Suggested answer grounded in the context."},
            "reasoning": {"type": "string", "description": "Reasoning why the question could be answered with the chunks."},
        },
    },
}

# 2. Instruct the model on the distribution of questions
SYSTEM_PROMPT = f"""
I am building a RAG application. I have a collection of 50 chunks of text...
I want you to come up with 30 questions to which the answers could be grounded in the chunk context.
Construct 10 questions that could use multipple chunks in the answer.
Construct 15 questions that could use single chunk in the answer.
Construct 5 questions that can't be answered with the available chunks.

<OUTPUT JSON SCHEMA>
{json.dumps(output_schema, indent=2)}
</OUTPUT JSON SCHEMA>
"""
```
*   **Structured Output (JSON)**: By providing a strict JSON Schema, we ensure the LLM returns data that Python can easily parse, rather than a wall of unstructured text.
*   **Data Distribution**: We intentionally ask for different *types* of questions. 
    *   **Single-chunk**: Tests basic retrieval.
    *   **Multi-chunk**: Tests the system's ability to synthesize answers from multiple products (e.g., comparing two items).
    *   **Unanswerable**: Tests the system's ability to politely decline answering when it doesn't have the context (preventing hallucination).

### Step 3: LLM Generation and Parsing
We send the prompt and our `all_context` to Gemini, and parse the resulting JSON.

```python
# Send request to Gemini
# ... (API call omitted for brevity) ...

# Parse the text response into a list of Python dictionaries
json_output = json.loads(response.text)
```

### Step 4: Uploading to LangSmith for Tracking
With our synthetic dataset generated (containing `question`, `answer_example`, and the ground truth `chunk_ids`), we upload it to LangSmith. LangSmith is an observability platform specifically built for LLM applications.

```python
from langsmith import Client

# Initialize the LangSmith client using the API key in our .env
client = Client(api_key=os.environ["LANGSMITH_API_KEY"])

# Create a new dataset project
dataset_name = "rag-evaluation-dataset"
dataset = client.create_dataset(
    dataset_name=dataset_name,
    description="Dataset for evaluating RAG pipeline"
)

# Upload each generated example to the LangSmith dataset
for item in json_output:
    client.create_example(
        dataset_id=dataset.id,
        inputs={"question": item["question"]},
        outputs={
            "ground_truth": item["answer_example"],
            "reference_context_ids": item["chunk_ids"],
            "reference_descriptions": [get_description(id) for id in item["chunk_ids"]]
        }
    )
```
*   **The "Why"**: 
    *   `inputs`: This is what our RAG pipeline will eventually be tested against (the user's question).
    *   `outputs`: This is the "answer key". It contains what the LLM *should* generate (`ground_truth`) and the specific database chunks it *should* retrieve (`reference_context_ids`). 
    *   In the next notebook, we will run our actual pipeline against this dataset and LangSmith will grade its performance!

---
