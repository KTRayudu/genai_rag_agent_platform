## Part 5.3: The End-to-End RAG Pipeline (`notebooks/week_1/03-RAG-pipeline.ipynb`)

### Overview
With our Vector Database populated, this notebook combines all the pieces to create a functional, interactive RAG (Retrieval-Augmented Generation) pipeline. It demonstrates how to take a user's natural language question, search the database for relevant products, format those products into a prompt, and ask a generative LLM (Gemini 2.5 Flash) to synthesize a coherent answer.

### Step 1: The Retrieval Function
The first half of RAG is **Retrieval**. When a user asks a question, we don't know the answer, but our database might have the relevant context.

```python
def retrieve_data(query, qdrant_client, k=5):
    # 1. Convert the user's text question into a vector
    query_embedding = get_embedding(query)

    # 2. Perform a semantic search in Qdrant
    results = qdrant_client.query_points(
        collection_name="Amazon-items-collection-03",
        query=query_embedding,
        limit=k,
    )

    # 3. Extract the useful information from the search results
    retrieved_context_ids = []
    retrieved_context = []
    similarity_scores = []
    retrieved_context_ratings = []

    for result in results.points:
        retrieved_context_ids.append(result.payload["parent_asin"])
        retrieved_context.append(result.payload["description"])
        retrieved_context_ratings.append(result.payload["average_rating"])
        similarity_scores.append(result.score)

    return {
        "retrieved_context_ids": retrieved_context_ids,
        "retrieved_context": retrieved_context,
        "retrieved_context_ratings": retrieved_context_ratings,
        "similarity_scores": similarity_scores,
    }
```
*   **The Vector Search**: Qdrant takes our query vector and compares it against all 3072-dimensional vectors in the database using Cosine Similarity. It returns the top `k` closest matches.
*   **Data Extraction**: The `results` object contains the `PointStructs` we inserted in the previous notebook. We loop through them and pull out the `payload` (our metadata) and the `score` (how closely it matched the query).

### Step 2: Processing and Prompt Building
Raw database results aren't useful to an LLM. We must format them into a human-readable string.

```python
def process_context(context):
    formatted_context = ""
    for id, chunk, rating in zip(context["retrieved_context_ids"], context["retrieved_context"], context["retrieved_context_ratings"]):
        formatted_context += f"- ID: {id}, rating: {rating}, description: {chunk}\n"
    return formatted_context

def build_prompt(preprocessed_context, question):
    prompt = f"""
You are a shopping assistant that can answer questions about the products in stock.

You will be given a question and a list of context.

Instructions:
- You need to answer the question based on the provided context only.
- Never use word context and refer to it as the available products.

Context:
{preprocessed_context}

Question:
{question}
"""
    return prompt
```
*   **Context Formatting**: `process_context` creates a bulleted list of the top retrieved products, including their ID, rating, and description.
*   **Prompt Engineering**: `build_prompt` uses an f-string to dynamically insert the retrieved product descriptions (`{preprocessed_context}`) and the user's original `{question}` into a strict set of instructions. 
    *   **Crucial Instruction**: *"You need to answer the question based on the provided context only."* This constraint minimizes hallucination, forcing the model to act solely as a synthesizer of our data rather than relying on its internal, potentially outdated knowledge base.

### Step 3: Generative Answer
The second half of RAG is **Generation**. We send our highly specific prompt to the LLM.

```python
def generate_answer(prompt, model_name="gemini-2.5-flash"):
    """
    Generates a response using the specified Gemini model.
    """
    response = gemini_client.models.generate_content(
        model=model_name,
        contents=prompt,
    )
    return response.text
```
*   **`gemini-2.5-flash`**: We utilize Google's `gemini-2.5-flash` model via the `google.genai` SDK. It is highly optimized for speed and low-latency text tasks, making it ideal for real-time chatbot interactions.

### Step 4: The Orchestrator (`rag_pipeline`)
Finally, we wrap all individual functions into a single pipeline.

```python
def rag_pipeline(question, top_k=5):
    qdrant_client = QdrantClient(url="http://localhost:6333")
    
    # 1. Retrieve raw data
    retrieved_context = retrieve_data(question, qdrant_client, top_k)
    
    # 2. Format context
    preprocessed_context = process_context(retrieved_context)
    
    # 3. Build Prompt
    prompt = build_prompt(preprocessed_context, question)
    
    # 4. Generate Answer
    answer = generate_answer(prompt)
    
    return answer

# Example Usage
print(rag_pipeline("What kind of earphones can I get with ratings above 4.3?"))
```
*   **The Full Flow**: In a single function call, a natural language query is vectorized, searched, formatted, and answered intelligently based *only* on the products in our Amazon dataset. This pipeline represents the core logic that will eventually be moved into the FastAPI backend (`apps/api/src/api/agents/retrieval_generation.py`).

---
