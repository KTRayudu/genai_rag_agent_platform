# GenAI RAG Agent Platform - Evaluation Pipeline

This README documents the end-to-end local evaluation pipeline for the RAG application. 
The pipeline has been migrated away from cloud APIs (Groq/Gemini) and now runs entirely locally using Ollama.

## 🧠 Models Used
To avoid rate limits and costs, the entire evaluation and generation pipeline is powered by your local hardware:
* **Vector Embeddings (Qdrant Database):** `gemini-embedding-001`
* **Dataset Generation (Synthetic Q&A):** Local Ollama (`gpt-oss:120b`)
* **Application RAG Answer Generation:** Local Ollama (`llama3.3:70b`)
* **Ragas Evaluator / Judge:** Local Ollama (`gpt-oss:120b`)

---

## 🚀 How to Run the Pipeline

The entire pipeline is controlled by a single `Makefile` command. It is a **two-step pipeline**:
1. It runs `generate_dataset.py` (which checks if the dataset needs to be generated).
2. It runs `eval_retriever.py` (which pulls the dataset from LangSmith and grades the app).

### Option A: Standard Run (Fast)
If you already generated the dataset and just want to run the evaluation, run:
```bash
make run-evals-retriever
```
*What happens:* The generator script will instantly ping LangSmith, see that your dataset (`ollama-70b-amazon-dataset`) already exists, and instantly skip the heavy generation process. It will then pass execution directly to the Ragas evaluator.

### Option B: Force Dataset Regeneration (Slow)
If you want to use the local 70B model to generate a brand new set of synthetic questions from your Qdrant database, you must attach the `FORCE=true` flag:
```bash
make run-evals-retriever FORCE=true
```
*What happens:* The Python script will ignore the safety check, fire up `llama3.3:70b`, process chunks from Qdrant, write 30 brand new synthetic Q&A pairs, upload them to LangSmith, and *then* seamlessly begin evaluating against them.

---

## 🛠️ Memory Management (Ollama)
You **do not** need to manually kill or manage Ollama's memory!
When the Python script finishes evaluating, Ollama will automatically start a 5-minute timer. If no new requests are sent within 5 minutes, it will automatically clear the massive model from your RAM/VRAM to free up space.

If you ever want to check what is loaded in memory:
```bash
ollama ps
```
If you want to manually force it to clear immediately:
```bash
ollama stop llama3.3:70b
```
