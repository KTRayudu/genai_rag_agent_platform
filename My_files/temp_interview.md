
## PART 6 — Interview Preparation: Key Questions & Answers

### 1. Architecture & Infrastructure

**Q: Why did you choose FastAPI over Flask or Django for the backend?**
**A:** FastAPI was chosen for its high performance (built on Starlette and Pydantic) and native async/await support, which is critical for I/O-bound operations like calling the Gemini API and querying the Qdrant Vector DB. Additionally, its automatic generation of OpenAPI (Swagger) documentation makes testing endpoints straightforward.

**Q: How does the communication work between your Streamlit frontend, FastAPI backend, and Qdrant database in your Docker setup?**
**A:** We use a `docker-compose.yml` file to orchestrate three separate containers. By placing them on a shared custom bridge network (`rag-network`), they can communicate using their service names as hostnames (e.g., FastAPI connects to Qdrant via `http://qdrant:6333` and Streamlit connects to FastAPI via `http://api:8000`). This ensures secure internal communication without exposing all ports to the host machine.

### 2. Retrieval-Augmented Generation (RAG) vs. Fine-Tuning

**Q: Why use RAG instead of just fine-tuning the Gemini model on your Amazon product dataset?**
**A:** RAG provides three massive advantages over fine-tuning for this use case:
1. **Real-time Updates:** If a product's price or rating changes, or a new product is added, we just update the Qdrant database. Fine-tuning would require retraining the model entirely.
2. **Hallucination Prevention (Groundedness):** RAG forces the model to answer *only* based on the provided context chunks. Fine-tuned models still rely on their internal weights and can easily hallucinate fake features or prices.
3. **Cost & Speed:** Embedding text into Qdrant is drastically cheaper and faster than fine-tuning a massive LLM.

### 3. Embeddings & Vector Databases (Qdrant)

**Q: What is an embedding, and why are we using `gemini-embedding-001` with 3072 dimensions?**
**A:** An embedding is a numerical representation of text (a vector array) that captures semantic meaning. We use `gemini-embedding-001` to map our product descriptions into a 3072-dimensional space. Words or products with similar features (e.g., "wireless earbuds" and "Bluetooth headphones") will have vectors that point in roughly the same direction, allowing us to find related products even if the exact keywords don't match.

**Q: What metric do you use to calculate the similarity between the user's question and the product embeddings?**
**A:** We use **Cosine Similarity**. Cosine similarity measures the angle between two vectors rather than their magnitude (length). This is crucial for text search because a long product description and a short user query might have very different magnitudes, but if they point in the same semantic direction, the angle between them will be small, indicating high relevance.

### 4. Advanced Prompt Engineering

**Q: How do you prevent the LLM from answering questions outside the scope of your inventory?**
**A:** We enforce strict constraints in the System Prompt. We explicitly instruct the model: *"You need to answer the question based on the provided context only"* and *"If the answer cannot be found... politely state that you do not have that information."* By injecting the retrieved Qdrant results directly into the prompt as the sole source of truth, we tightly bound the model's reasoning capabilities.

### 5. Evaluation & RAGAS

**Q: How do you mathematically prove your RAG pipeline is working? What is RAGAS?**
**A:** We use the **RAGAS (Retrieval Augmented Generation Assessment)** framework. Because manual testing is unscalable, we first generate a synthetic evaluation dataset (questions paired with known ground-truth context IDs). RAGAS uses a "Judge LLM" to score our pipeline on two main fronts:
- **Generation Metrics:** 
  - **Faithfulness:** Does the generated answer contain hallucinations, or is it strictly derived from the retrieved context?
  - **Response Relevancy:** Did the answer actually address the user's question without useless verbosity?
- **Retrieval Metrics:**
  - **Context Precision:** Did Qdrant retrieve the most relevant chunks, and were they ranked at the top?
  - **Context Recall:** Did Qdrant successfully retrieve *all* the chunks necessary to fully answer the question?
