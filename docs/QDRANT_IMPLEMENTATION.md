# Qdrant Vector Database Implementation Guide

This document provides a comprehensive explanation of the Qdrant vector database implementation used in this project. It is designed for developers who are learning about vector databases and Retrieval-Augmented Generation (RAG) systems.

## Table of Contents

1. [Introduction](#introduction)
2. [What is Qdrant?](#what-is-qdrant)
3. [Architecture Overview](#architecture-overview)
4. [Setup and Configuration](#setup-and-configuration)
5. [Creating Collections](#creating-collections)
6. [Generating and Storing Vectors](#generating-and-storing-vectors)
7. [Similarity Search](#similarity-search)
8. [The Complete RAG Pipeline](#the-complete-rag-pipeline)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Introduction

This project implements a RAG (Retrieval-Augmented Generation) system that uses Qdrant as its vector database. The system allows users to ask natural language questions about Amazon electronics products and receive AI-generated answers grounded in actual product data.

**Why use a vector database?**

Traditional databases excel at exact matches (e.g., "find all products where price = 29.99"). However, they struggle with semantic queries like "find products similar to wireless headphones for running." Vector databases solve this by storing numerical representations (embeddings) of data and finding items based on mathematical similarity.

---

## What is Qdrant?

Qdrant is an open-source vector similarity search engine designed for production use. Key characteristics include:

- **High Performance**: Optimized for fast similarity searches across millions of vectors
- **Filtering Support**: Combine vector search with traditional filters (price ranges, ratings, etc.)
- **Payload Storage**: Store metadata alongside vectors for rich query results
- **REST and gRPC APIs**: Multiple integration options for different use cases
- **Persistence**: Data survives restarts with configurable storage options

### Why Qdrant for This Project?

1. **Ease of Use**: Simple Python client with intuitive APIs
2. **Docker Support**: Quick local setup for development
3. **Scalability**: Can handle production workloads when needed
4. **Cost-Effective**: Open-source with no licensing fees

---

## Architecture Overview

The data flow in this system follows these steps:

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Raw Product    │────▶│   Preprocessing  │────▶│    Embedding    │
│     Data        │     │   (Notebooks)    │     │   Generation    │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   AI Response   │◀────│   LLM Generation │◀────│     Qdrant      │
│                 │     │                  │     │   (Retrieval)   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### Key Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Qdrant Server | Docker container | Stores and searches vectors |
| Embedding Function | [retrieval_generation.py](../apps/api/src/api/agents/retrieval_generation.py) | Converts text to vectors |
| Retrieval Function | [retrieval_generation.py](../apps/api/src/api/agents/retrieval_generation.py) | Searches Qdrant for similar items |
| API Endpoint | [endpoints.py](../apps/api/src/api/api/endpoints.py) | Exposes RAG functionality via HTTP |
| Preprocessing | [Notebook 02](../notebooks/week_1/02-RAG-preprocessing-Amazon.ipynb) | Prepares and indexes product data |

---

## Setup and Configuration

### Docker Configuration

Qdrant runs as a Docker service defined in [docker-compose.yml](../docker-compose.yml):

```yaml
qdrant:
  image: qdrant/qdrant
  container_name: qdrant
  ports:
    - "6333:6333"  # REST API
    - "6334:6334"  # gRPC API
  volumes:
    - ./qdrant_storage:/qdrant/storage
  restart: always
```

**Understanding the configuration:**

- **Ports 6333/6334**: REST API for HTTP requests, gRPC for high-performance applications
- **Volume mounting**: `./qdrant_storage:/qdrant/storage` persists data on your local machine, ensuring data survives container restarts
- **Restart policy**: `always` ensures Qdrant automatically restarts if it crashes

### Client Initialization

The Python client connects to Qdrant in [endpoints.py:16](../apps/api/src/api/api/endpoints.py):

```python
from qdrant_client import QdrantClient

# When running inside Docker network
qdrant_client = QdrantClient(url="http://qdrant:6333")

# When running locally (outside Docker)
# qdrant_client = QdrantClient(url="http://localhost:6333")
```

**Why the different URLs?**

- Inside Docker: Services communicate using container names (`qdrant`)
- Outside Docker: Use `localhost` to access the exposed port

### Dependencies

Add the Qdrant client to your project:

```toml
# pyproject.toml
dependencies = [
    "qdrant-client>=1.16.2",
]
```

---

## Creating Collections

A **collection** in Qdrant is analogous to a table in a relational database. It defines the structure of your vectors.

### Collection Creation

From the preprocessing notebook:

```python
from qdrant_client.models import Distance, VectorParams

qdrant_client.create_collection(
    collection_name="Amazon-items-collection-00",
    vectors_config=VectorParams(
        size=1536,           # Dimensions of your embeddings
        distance=Distance.COSINE  # Similarity metric
    ),
)
```

### Understanding the Parameters

#### Vector Size (1536)

This must match the output dimensions of your embedding model:

| Embedding Model | Dimensions |
|-----------------|------------|
| OpenAI text-embedding-3-small | 1536 |
| OpenAI text-embedding-3-large | 3072 |
| Cohere embed-english-v3.0 | 1024 |

**Important**: Mismatched dimensions will cause errors during insertion.

#### Distance Metric (COSINE)

The distance metric determines how similarity is calculated:

| Metric | Range | Best For |
|--------|-------|----------|
| COSINE | -1 to 1 | Normalized embeddings, semantic similarity |
| EUCLID | 0 to ∞ | When magnitude matters |
| DOT | -∞ to ∞ | When vectors are normalized and you want speed |

**Why COSINE?**

Cosine similarity measures the angle between vectors, ignoring magnitude. This is ideal for text embeddings because:
- Two sentences about "wireless headphones" should be similar regardless of length
- OpenAI embeddings are optimized for cosine similarity

---

## Generating and Storing Vectors

### The Embedding Function

Located in [retrieval_generation.py:11-25](../apps/api/src/api/agents/retrieval_generation.py):

```python
import openai

def get_embedding(text, model="text-embedding-3-small"):
    response = openai.embeddings.create(
        input=text,
        model=model,
    )
    return response.data[0].embedding
```

**What happens here:**

1. Text is sent to OpenAI's embedding API
2. The model converts text into a 1536-dimensional vector
3. This vector captures the semantic meaning of the text

### Preparing Data for Storage

Before storing in Qdrant, data must be structured properly:

```python
from qdrant_client.models import PointStruct

# Prepare product data
def preprocess_description(row):
    return f"{row['title']} {' '.join(row['features'])}"

df_items["description"] = df_items.apply(preprocess_description, axis=1)
```

**Why combine title and features?**

- More context leads to better embeddings
- A title alone ("Sony WH-1000XM4") is less informative than title + features ("Sony WH-1000XM4 Noise Canceling Wireless Bluetooth Over-Ear Headphones")

### Creating and Uploading Points

```python
pointstructs = []
for i, data in enumerate(data_to_embed):
    embedding = get_embedding(data["description"])
    pointstructs.append(
        PointStruct(
            id=i,                    # Unique identifier
            vector=embedding,        # The 1536-dimensional vector
            payload=data,            # Metadata (description, price, rating, etc.)
        )
    )

# Upload to Qdrant
qdrant_client.upsert(
    collection_name="Amazon-items-collection-00",
    wait=True,
    points=pointstructs,
)
```

### Understanding PointStruct

Each point in Qdrant consists of three parts:

| Field | Purpose | Example |
|-------|---------|---------|
| `id` | Unique identifier | `0`, `1`, `"product-abc"` |
| `vector` | Numerical representation | `[0.023, -0.156, 0.891, ...]` |
| `payload` | Searchable metadata | `{"price": 299.99, "rating": 4.5}` |

**The payload is crucial**: It stores all the information you want to retrieve alongside the vector match. Without it, you would only get back IDs.

### The Upsert Operation

```python
qdrant_client.upsert(
    collection_name="Amazon-items-collection-00",
    wait=True,      # Block until operation completes
    points=pointstructs,
)
```

**Why `upsert` instead of `insert`?**

- **Upsert** = Update + Insert
- If a point with the same ID exists, it updates it
- If not, it inserts a new point
- This makes the operation idempotent (safe to run multiple times)

**Why `wait=True`?**

- Ensures the data is fully indexed before proceeding
- Without it, subsequent searches might miss recently added data

---

## Similarity Search

### The Retrieval Function

Located in [retrieval_generation.py:32-58](../apps/api/src/api/agents/retrieval_generation.py):

```python
def retrieve_data(query, qdrant_client, k=5):
    # Step 1: Convert query to embedding
    query_embedding = get_embedding(query)

    # Step 2: Search for k nearest neighbors
    results = qdrant_client.query_points(
        collection_name="Amazon-items-collection-00",
        query=query_embedding,
        limit=k,
    )

    # Step 3: Extract results
    retrieved_context = []
    similarity_scores = []

    for result in results.points:
        retrieved_context.append(result.payload["description"])
        similarity_scores.append(result.score)

    return {
        "retrieved_context": retrieved_context,
        "similarity_scores": similarity_scores,
    }
```

### How Similarity Search Works

1. **Query Embedding**: The user's question is converted to a vector using the same embedding model
2. **k-NN Search**: Qdrant finds the `k` vectors closest to the query vector
3. **Score Calculation**: Each result includes a similarity score (0-1 for cosine, higher = more similar)
4. **Payload Return**: The metadata stored with each vector is returned

### Interpreting Similarity Scores

For cosine similarity:

| Score | Interpretation |
|-------|----------------|
| 0.9+ | Very high similarity, likely relevant |
| 0.7-0.9 | Good similarity, probably relevant |
| 0.5-0.7 | Moderate similarity, might be relevant |
| < 0.5 | Low similarity, likely not relevant |

**Note**: These thresholds are approximate and may vary based on your data and embedding model.

---

## The Complete RAG Pipeline

### Pipeline Overview

The RAG pipeline in [retrieval_generation.py:125-142](../apps/api/src/api/agents/retrieval_generation.py) combines all components:

```python
def rag_pipeline(question, qdrant_client, top_k=5):
    # Step 1: Retrieve relevant products
    retrieved_context = retrieve_data(question, qdrant_client, top_k)

    # Step 2: Format context for the LLM
    preprocessed_context = process_context(retrieved_context)

    # Step 3: Build the prompt
    prompt = build_prompt(preprocessed_context, question)

    # Step 4: Generate answer
    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "question": question,
        "retrieved_context": retrieved_context["retrieved_context"],
        "similarity_scores": retrieved_context["similarity_scores"]
    }
```

### Context Formatting

The retrieved products are formatted into a readable string:

```python
def process_context(context):
    formatted_context = ""
    for id, chunk, rating in zip(
        context["retrieved_context_ids"],
        context["retrieved_context"],
        context["retrieved_context_ratings"]
    ):
        formatted_context += f"- ID: {id}, rating: {rating}, description: {chunk}\n"
    return formatted_context
```

### Prompt Construction

The prompt grounds the LLM's response in retrieved data:

```python
def build_prompt(preprocessed_context, question):
    prompt = f"""
You are a shopping assistant that can answer questions about the products in stock.

Instructions:
- Answer the question based on the provided context only.
- Never use the word "context"; refer to it as "available products."

Context:
{preprocessed_context}

Question:
{question}
"""
    return prompt
```

**Why this prompt structure?**

1. **Role definition**: Establishes the assistant's purpose
2. **Grounding instruction**: Prevents hallucination by limiting answers to provided data
3. **Context injection**: Provides the retrieved product information
4. **Clear question**: Ensures the model knows what to answer

### API Exposure

The pipeline is exposed via FastAPI in [endpoints.py:20-31](../apps/api/src/api/api/endpoints.py):

```python
@rag_router.post("/")
def rag(request: Request, payload: RAGRequest) -> RAGResponse:
    answer = rag_pipeline(payload.query, qdrant_client)
    return RAGResponse(
        request_id=request.state.request_id,
        answer=answer["answer"]
    )
```

---

## Best Practices

### 1. Embedding Consistency

Always use the same embedding model for indexing and querying. Mixing models will produce meaningless results because different models create incompatible vector spaces.

```python
# Good: Same model for both
EMBEDDING_MODEL = "text-embedding-3-small"
index_embedding = get_embedding(product_description, model=EMBEDDING_MODEL)
query_embedding = get_embedding(user_question, model=EMBEDDING_MODEL)
```

### 2. Payload Design

Store all metadata you might need for filtering or display:

```python
payload = {
    "description": "Product description for display",
    "price": 299.99,           # For filtering: "under $300"
    "category": "headphones",  # For filtering: "only headphones"
    "rating": 4.5,             # For sorting: "highest rated"
    "in_stock": True,          # For filtering: "available items"
}
```

### 3. Batch Operations

For large datasets, batch your uploads:

```python
BATCH_SIZE = 100

for i in range(0, len(all_points), BATCH_SIZE):
    batch = all_points[i:i + BATCH_SIZE]
    qdrant_client.upsert(
        collection_name="my-collection",
        points=batch,
        wait=True
    )
```

### 4. Error Handling

Always handle potential failures gracefully:

```python
from qdrant_client.http.exceptions import UnexpectedResponse

try:
    results = qdrant_client.query_points(
        collection_name="my-collection",
        query=query_embedding,
        limit=5
    )
except UnexpectedResponse as e:
    logger.error(f"Qdrant query failed: {e}")
    # Fallback behavior
```

### 5. Collection Naming

Use descriptive, versioned collection names:

```python
# Good: Descriptive and versioned
"amazon-electronics-v2"
"product-catalog-2024-01"

# Avoid: Generic or unclear
"collection1"
"data"
```

---

## Troubleshooting

### Common Issues

#### 1. Connection Refused

```
Error: Connection refused at localhost:6333
```

**Solutions:**
- Verify Qdrant container is running: `docker ps`
- Check port mapping in docker-compose.yml
- If inside Docker network, use service name (`qdrant`) instead of `localhost`

#### 2. Dimension Mismatch

```
Error: Vector dimension mismatch
```

**Solution:**
- Ensure your embedding model outputs vectors matching the collection's configured size
- Check collection configuration: `qdrant_client.get_collection("collection-name")`

#### 3. Collection Not Found

```
Error: Collection "my-collection" not found
```

**Solutions:**
- Create the collection before inserting data
- Verify collection name spelling (case-sensitive)
- List existing collections: `qdrant_client.get_collections()`

#### 4. Slow Queries

**Solutions:**
- Add indexes for frequently filtered payload fields
- Consider using quantization for large datasets
- Reduce `limit` parameter if retrieving too many results

### Useful Debug Commands

```python
# List all collections
print(qdrant_client.get_collections())

# Get collection info
print(qdrant_client.get_collection("Amazon-items-collection-00"))

# Count points in collection
print(qdrant_client.count("Amazon-items-collection-00"))

# Retrieve a specific point
print(qdrant_client.retrieve("Amazon-items-collection-00", ids=[0]))
```

---

## Additional Resources

- [Qdrant Official Documentation](https://qdrant.tech/documentation/)
- [Qdrant Python Client](https://github.com/qdrant/qdrant-client)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [RAG Best Practices](https://www.anthropic.com/news/contextual-retrieval)

---

## Summary

This implementation demonstrates a production-ready approach to building a RAG system with Qdrant:

1. **Data Preparation**: Product data is preprocessed and combined into searchable descriptions
2. **Embedding Generation**: OpenAI's text-embedding-3-small converts text to 1536-dimensional vectors
3. **Vector Storage**: Qdrant stores vectors with rich metadata payloads
4. **Similarity Search**: User queries are embedded and matched against stored vectors
5. **Response Generation**: Retrieved context grounds LLM responses in actual data

The architecture separates concerns cleanly, making it maintainable and scalable for production use.
