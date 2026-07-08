## Part 5.2: RAG Data Preprocessing & Vector Database Setup (`notebooks/week_1/02-RAG-preprocessing-Amazon.ipynb`)

### Overview
This notebook is the critical bridge between raw data and our Retrieval-Augmented Generation (RAG) system. Its primary purpose is to take the cleaned Amazon product data, convert the text into numerical vectors (embeddings) using Google's Gemini API, and store these vectors in our local Qdrant Vector Database. This enables the core semantic search capability of our RAG pipeline.

### Prerequisites & Setup
Before we begin vectorizing data, we need the right tools to connect to Gemini and Qdrant.

```python
!pip install -qU google-genai qdrant-client python-dotenv
```
*   **`google-genai`**: The official SDK to interact with Google's Gemini models (including the embedding model).
*   **`qdrant-client`**: The Python client to connect to and interact with our running Qdrant Vector Database container.
*   **`python-dotenv`**: A utility to load our `.env` file containing the `GOOGLE_API_KEY`.

### Step 1: Loading Dependencies and Data
We start by loading our previously cleaned JSONL dataset.

```python
import json
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from google import genai
from google.genai import types

# Load environment variables (importantly, GOOGLE_API_KEY)
load_dotenv()

# Load the previously extracted Amazon data
data_to_embed = []
with open("../../data/amazon_data.jsonl", "r") as f:
    for line in f:
        data_to_embed.append(json.loads(line))
```
*   **Why this matters**: We are loading the `amazon_data.jsonl` file we prepared in the previous notebook into memory. Each item in `data_to_embed` is a Python dictionary containing the product `description`, `image` URL, `price`, etc. 

### Step 2: Defining the Embedding Function
Embeddings are the backbone of semantic search. They convert human-readable text into a list of numbers (a vector) that captures the "meaning" of the text.

```python
gemini_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_embedding(text, task_type="RETRIEVAL_DOCUMENT"):
    """
    Generates an embedding vector for the given text using Gemini's current model.
    """
    response = gemini_client.models.embed_content(
        model="gemini-embedding-001", 
        contents=text,
        config=types.EmbedContentConfig(
            task_type=task_type
        )
    )
    return response.embeddings[0].values

# Verify the embedding dimensionality
len(get_embedding("Hi")) # Returns 3072
```
*   **The "Why"**: 
    *   We initialize the `genai.Client`.
    *   We use the `gemini-embedding-001` model. This model converts any string of text into a vector of exactly **3072 dimensions** (floating-point numbers). 
    *   `task_type="RETRIEVAL_DOCUMENT"` tells the model that this text is intended to be stored and searched against later. This optimizes the vector representation for semantic search.

> [!WARNING]
> **Deprecation Notice Addressed**: Earlier versions of this codebase might have used the deprecated `google.generativeai` package. We have successfully migrated to the new, official `google.genai` SDK.

### Step 3: Setting up the Qdrant Vector Database
With our data in memory and an embedding function ready, we need a place to store the vectors.

```python
# Connect to local Qdrant container
qdrant_client = QdrantClient(url="http://localhost:6333")

# Create the collection
qdrant_client.create_collection(
    collection_name="Amazon-items-collection-03",
    vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
)
```
*   **The Connection**: We connect to `http://localhost:6333`, which is the default port for the Qdrant REST API exposed by our Docker container.
*   **Creating the Collection**: A "collection" in Qdrant is akin to a table in a relational database.
*   **`size=3072`**: This is crucial. We must explicitly tell Qdrant that every vector we insert will have exactly 3072 dimensions (matching the output of `gemini-embedding-001`). If there's a mismatch, Qdrant will throw an error.
*   **`distance=Distance.COSINE`**: This defines *how* we measure similarity. Cosine distance measures the angle between two vectors, which is the industry standard for determining semantic similarity between text embeddings.

### Step 4: Structuring Data for Qdrant (PointStructs)
Qdrant requires data to be formatted in a specific way before insertion: using the `PointStruct` object.

```python
pointstructs = []
for i, data in enumerate(data_to_embed):
    # Generate the vector for the product description
    embedding = get_embedding(data["description"])
    
    # Create the PointStruct
    pointstructs.append(
        PointStruct(
            id=i, # Unique integer ID
            vector=embedding, # The 3072-dimensional vector
            payload=data, # The original dictionary (metadata)
        )
    )
```
*   **The "Why"**: A `PointStruct` requires three components:
    1.  `id`: A unique identifier (we simply use the loop index `i`).
    2.  `vector`: The actual list of 3072 numbers representing the text.
    3.  `payload`: The metadata. By passing our entire `data` dictionary as the payload, we ensure that when we retrieve a vector later, we get back the `image` URL, `price`, and `rating_number` along with it.

### Step 5: Uploading to Qdrant (The Upsert)
Finally, we send all our structured points to the database.

```python
qdrant_client.upsert(
    collection_name="Amazon-items-collection-03",
    points=pointstructs,
)
```
*   **The Execution**: The `upsert` command ("update or insert") pushes the list of `pointstructs` to our Qdrant container. Once this completes, our Vector Database is fully populated and ready to serve semantic queries!

---
