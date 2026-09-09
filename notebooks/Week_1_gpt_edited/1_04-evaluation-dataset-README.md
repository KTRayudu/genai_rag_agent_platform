# Evaluation Dataset Generation for RAG Systems

This README explains the notebook `04-evaluation-dataset.ipynb`, which demonstrates how to create a synthetic evaluation dataset for Retrieval-Augmented Generation (RAG) applications.

## Overview

When building RAG systems, you need a way to measure how well your retrieval and generation components perform. This notebook shows how to:

1. Extract data from a vector database (Qdrant)
2. Use an LLM to generate synthetic evaluation questions
3. Store the evaluation dataset in LangSmith for tracking experiments

## Why Create Evaluation Datasets?

Evaluation datasets are essential for:

- **Measuring retrieval quality**: Does your system find the right documents?
- **Measuring answer quality**: Are the generated answers accurate and grounded?
- **Tracking improvements**: Compare different configurations over time
- **Identifying failure modes**: Find where your system struggles

Without evaluation data, you're essentially flying blind when making changes to your RAG pipeline.

## Prerequisites

- Qdrant running locally on port 6333
- OpenAI API access
- LangSmith API key
- A populated Qdrant collection with product data

## Step-by-Step Explanation

### 1. Connecting to Qdrant and Extracting Data

```python
qdrant_client = QdrantClient(url="http://localhost:6333")

all_points = qdrant_client.scroll(
    collection_name="Amazon-items-collection-00",
    limit=100,
    with_payload=True,
    with_vectors=False
)
```

**Why this approach?**
- `scroll()` retrieves all documents from a collection efficiently
- `with_vectors=False` reduces data transfer since we only need the text content
- The payload contains product descriptions that will serve as context for question generation

### 2. Preparing Context for the LLM

```python
all_context = [
    {"id": data.payload["parent_asin"], "text": data.payload["description"]}
    for data in all_points[0]
]
```

**Why structure it this way?**
- Each chunk needs a unique identifier (`parent_asin`) so the LLM can reference which chunks answer each question
- The text content provides the context from which questions can be derived

### 3. Designing the Prompt for Synthetic Data Generation

The prompt asks the LLM to generate three types of questions:

| Question Type | Count | Purpose |
|--------------|-------|---------|
| Multi-chunk questions | 10 | Tests retrieval of multiple relevant documents |
| Single-chunk questions | 15 | Tests precise retrieval of specific information |
| Unanswerable questions | 5 | Tests the system's ability to recognize knowledge gaps |

**Why include unanswerable questions?**
A robust RAG system should recognize when it cannot answer a question rather than hallucinating an answer. Including these in your evaluation helps measure this capability.

### 4. Defining the Output Schema

```python
output_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {...},
            "chunk_ids": {...},
            "answer_example": {...},
            "reasoning": {...}
        }
    }
}
```

**Why each field matters:**
- `question`: The synthetic user query
- `chunk_ids`: Ground truth for which documents should be retrieved
- `answer_example`: Reference answer for evaluating generation quality
- `reasoning`: Helps verify the LLM's logic and catch errors

### 5. Generating the Dataset with an LLM

```python
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    reasoning_effort="minimal"
)
```

**Why use an LLM for this?**
- Manual creation of evaluation datasets is time-consuming
- LLMs can generate diverse, realistic questions
- The process is reproducible and scalable

**Important considerations:**
- Review generated questions for quality
- Verify that chunk_ids actually contain relevant information
- Consider generating multiple batches and curating the best examples

### 6. Uploading to LangSmith

```python
client = Client(api_key=os.environ["LANGSMITH_API_KEY"])

dataset = client.create_dataset(
    dataset_name="rag-evaluation-dataset",
    description="Dataset for evaluating RAG pipeline"
)

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

**Why use LangSmith?**
- Centralized storage for evaluation datasets
- Built-in tools for running evaluations
- Experiment tracking and comparison
- Collaboration features for teams

**Dataset structure:**
- `inputs`: What your RAG system receives (the question)
- `outputs`: Ground truth for comparison (expected answer, relevant chunks)

## Helper Function

```python
def get_description(parent_asin: str) -> str:
    points = qdrant_client.scroll(
        collection_name="Amazon-items-collection-00",
        scroll_filter=Filter(
            must=[
                FieldCondition(
                    key="parent_asin",
                    match=MatchValue(value=parent_asin)
                )
            ]
        ),
        ...
    )
    return points[0].payload["description"]
```

**Purpose:** Retrieves the full description text for a given product ID. This is used to store reference descriptions alongside the evaluation examples, making it easier to inspect what context should have been retrieved.

## Best Practices

1. **Review generated data**: LLM-generated datasets can contain errors. Sample and verify.

2. **Balance question types**: Include easy, medium, and hard questions to get a complete picture of system performance.

3. **Version your datasets**: When you improve your dataset, create a new version rather than overwriting.

4. **Include edge cases**: Questions with ambiguous answers, multiple valid responses, or requiring reasoning across chunks.

5. **Document your methodology**: Record the prompts and models used so results are reproducible.

## Common Evaluation Metrics

Once you have this dataset, you can measure:

| Metric | What it Measures |
|--------|-----------------|
| Retrieval Precision | % of retrieved chunks that are relevant |
| Retrieval Recall | % of relevant chunks that were retrieved |
| Answer Correctness | How well the generated answer matches ground truth |
| Faithfulness | Whether the answer is grounded in retrieved context |
| Answer Relevance | Whether the answer addresses the question |

## Next Steps

After creating your evaluation dataset:

1. Run your RAG pipeline against these questions
2. Compare retrieved chunks to `reference_context_ids`
3. Compare generated answers to `ground_truth`
4. Iterate on your retrieval and generation strategies
5. Track improvements over time in LangSmith

## Additional Resources

- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [RAG Evaluation Best Practices](https://www.anthropic.com/research)
