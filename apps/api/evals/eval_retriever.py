from api.agents.retrieval_generation import rag_pipeline
import os
import asyncio
import time

from qdrant_client import QdrantClient

from langsmith import Client
from qdrant_client import QdrantClient

# from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from ragas.dataset_schema import SingleTurnSample 
from ragas.metrics import IDBasedContextPrecision, IDBasedContextRecall, Faithfulness, ResponseRelevancy
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.embeddings import Embeddings
from google import genai
from ragas.run_config import RunConfig

os.environ["LANGCHAIN_CONCURRENCY_LIMIT"] = "10"

ls_client = Client()
qdrant_client = QdrantClient(
    url=f"http://localhost:6333"
)

# ragas_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4.1-mini"))
# ragas_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small"))

# --- OLD CODE (gemini-2.5-flash is no longer available, gave 404 error) ---
# ragas_llm = LangchainLLMWrapper(ChatGoogleGenerativeAI(model="gemini-2.5-flash"))
# --------------------------------------------------------------------------

# --- OLD CODE (Hit Gemini 15 Requests-Per-Minute rate limits because Ragas makes concurrent calls) ---
# ragas_llm = LangchainLLMWrapper(ChatGoogleGenerativeAI(model="gemini-3.6-flash"))
# ragas_embeddings = LangchainEmbeddingsWrapper(GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
# --------------------------------------------------------------------------

# NEW CODE: Added RunConfig(max_workers=1) to prevent Ragas from firing concurrent requests and exceeding the Gemini free tier RPM limits.
SAFE_CONFIG = RunConfig(max_workers=1, max_retries=10, max_wait=60)

# --- OLD CODE (Swapped to Groq because Gemini had a 20-request/day limit) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGoogleGenerativeAI(model="gemini-3.6-flash"),
#     run_config=SAFE_CONFIG
# )
# -----------------------------------------------------------------------------

# --- OLD CODE (Caused 404 access denied error on free tier) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGroq(model="llama-3.1-8b-instant")
# )
# --------------------------------------------------------------

# --- OLD CODE (Caused 400 error: llama3-8b-8192 is decommissioned) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGroq(model="llama3-8b-8192")
# )
# ---------------------------------------------------------------------

# --- OLD CODE (Caused 400 error: gemma2-9b-it is decommissioned) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGroq(model="gemma2-9b-it")
# )
# ---------------------------------------------------------------------

# --- OLD CODE (Hit Groq 200,000 TPD limit for gpt-oss-20b) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGroq(model="openai/gpt-oss-20b")
# )
# -------------------------------------------------------------

# --- OLD CODE (Hit Groq 200,000 TPD limit for gpt-oss-20b) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGroq(model="openai/gpt-oss-20b")
# )
# -------------------------------------------------------------

# --- OLD CODE (Hit Groq 120b limit) ---
# ragas_llm = LangchainLLMWrapper(
#     ChatGroq(model="openai/gpt-oss-120b", max_tokens=4096)
# )
# --------------------------------------

ragas_llm = LangchainLLMWrapper(
    ChatOllama(model="gpt-oss:120b")
)
# --- OLD CODE (Caused 404 error: embedding-001 is deprecated/removed) ---
# ragas_embeddings = LangchainEmbeddingsWrapper(
#     GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
#     run_config=SAFE_CONFIG
# )
# -------------------------------------------------------------------------

# --- OLD CODE (Caused 404 error: Google embeddings are broken in the current API package) ---
# ragas_embeddings = LangchainEmbeddingsWrapper(
#     GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
#     run_config=SAFE_CONFIG
# )
# --------------------------------------------------------------------------------------------

# --- OLD CODE (Replaced with custom Gemini wrapper) ---
# ragas_embeddings = LangchainEmbeddingsWrapper(
#     HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
#     run_config=SAFE_CONFIG
# )
# -----------------------------------------------------

class ModernGoogleEmbeddings(Embeddings):
    """
    A custom wrapper to bypass Langchain's broken Google API integration
    and connect directly to the modern google.genai SDK (which works perfectly).
    """
    def __init__(self, model="gemini-embedding-001"):
        self.model = model
        self.client = genai.Client()
        
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        res = self.client.models.embed_content(model=self.model, contents=texts)
        return [e.values for e in res.embeddings]
        
    def embed_query(self, text: str) -> list[float]:
        res = self.client.models.embed_content(model=self.model, contents=text)
        return res.embeddings[0].values

ragas_embeddings = LangchainEmbeddingsWrapper(
    ModernGoogleEmbeddings(model="gemini-embedding-001"),
    run_config=SAFE_CONFIG
)


def get_outputs(run):
    # LangSmith sometimes wraps dictionary returns in an "output" key.
    # This helper safely extracts the actual dictionary.
    if "retrieved_context_ids" in run.outputs:
        return run.outputs
    elif "output" in run.outputs and isinstance(run.outputs["output"], dict):
        return run.outputs["output"]
    
    print(f"\n[DEBUG] Unexpected run.outputs structure: {run.outputs}\n")
    return run.outputs

# --- OLD CODE (Caused RuntimeError: There is no current event loop in thread 'ThreadPoolExecutor') ---
# async def ragas_faithfulness(run, example):
#     # --- OLD CODE (Caused KeyError because it strictly required exact keys) ---
#     # sample = SingleTurnSample(...)
#     # --------------------------------------------------------------------------
#     await asyncio.sleep(5)
#     outputs = get_outputs(run)
#     sample = SingleTurnSample(
#             user_input=outputs.get("question", ""),
#             response=outputs.get("answer", ""),
#             retrieved_contexts=outputs.get("retrieved_context", [])
#         )
#     scorer = Faithfulness(llm=ragas_llm)
#     return await scorer.single_turn_ascore(sample)
# ------------------------------------------------------------------------------------------------

# NEW CODE: Changed to synchronous `def` and added `asyncio.run()` to safely create an event loop for LangSmith's thread pool
def ragas_faithfulness(run, example):
    # --- OLD CODE (Caused KeyError because it strictly required exact keys) ---
    # sample = SingleTurnSample(
    #         user_input=run.outputs["question"],
    #         response=run.outputs["answer"],
    #         retrieved_contexts=run.outputs["retrieved_context"]
    #     )
    # --------------------------------------------------------------------------
    async def _run():
        # --- OLD CODE (Throttled for Gemini API limits) ---
        # await asyncio.sleep(5)
        # --------------------------------------------------
        
        outputs = get_outputs(run)
        sample = SingleTurnSample(
                user_input=outputs.get("question", ""),
                response=outputs.get("answer", ""),
                retrieved_contexts=outputs.get("retrieved_context", [])
            )
        scorer = Faithfulness(llm=ragas_llm)

        return await scorer.single_turn_ascore(sample)
    return asyncio.run(_run())


# --- OLD CODE (Caused RuntimeError: There is no current event loop in thread 'ThreadPoolExecutor') ---
# async def ragas_responce_relevancy(run, example):
#     await asyncio.sleep(25)
#     outputs = get_outputs(run)
#     sample = SingleTurnSample(
#             user_input=outputs.get("question", ""),
#             response=outputs.get("answer", ""),
#             retrieved_contexts=outputs.get("retrieved_context", [])
#         )
#     scorer = ResponseRelevancy(llm=ragas_llm, embeddings=ragas_embeddings)
#     return await scorer.single_turn_ascore(sample)
# ------------------------------------------------------------------------------------------------

# NEW CODE: Changed to synchronous `def` and added `asyncio.run()` to safely create an event loop for LangSmith's thread pool
def ragas_responce_relevancy(run, example):
    # --- OLD CODE (Caused KeyError) ---
    # sample = SingleTurnSample(
    #         user_input=run.outputs["question"],
    #         response=run.outputs["answer"],
    #         retrieved_contexts=run.outputs["retrieved_context"]
    #     )
    # ----------------------------------
    async def _run():
        # --- OLD CODE (Throttled for Gemini API limits) ---
        # await asyncio.sleep(25)
        # --------------------------------------------------

        outputs = get_outputs(run)
        sample = SingleTurnSample(
                user_input=outputs.get("question", ""),
                response=outputs.get("answer", ""),
                retrieved_contexts=outputs.get("retrieved_context", [])
            )
        # --- OLD CODE (Caused 'n must be at most 1' error on Groq) ---
        # scorer = ResponseRelevancy(llm=ragas_llm, embeddings=ragas_embeddings)
        # -------------------------------------------------------------
        
        scorer = ResponseRelevancy(llm=ragas_llm, embeddings=ragas_embeddings)
        scorer.strictness = 1 # FIX: Groq only supports n=1 completions per prompt

        return await scorer.single_turn_ascore(sample)
    return asyncio.run(_run())


# --- OLD CODE (Caused RuntimeError: There is no current event loop in thread 'ThreadPoolExecutor') ---
# async def ragas_context_precision_id_based(run, example):
#     outputs = get_outputs(run)
#     sample = SingleTurnSample(
#             retrieved_context_ids=outputs.get("retrieved_context_ids", []),
#             reference_context_ids=example.outputs.get("reference_context_ids", [])
#         )
#     scorer = IDBasedContextPrecision()
#     return await scorer.single_turn_ascore(sample)
# ------------------------------------------------------------------------------------------------

# NEW CODE: Changed to synchronous `def` and added `asyncio.run()` to safely create an event loop for LangSmith's thread pool
def ragas_context_precision_id_based(run, example):
    # --- OLD CODE (Caused KeyError) ---
    # sample = SingleTurnSample(
    #         retrieved_context_ids=run.outputs["retrieved_context_ids"],
    #         reference_context_ids=example.outputs["reference_context_ids"]
    #     )
    # ----------------------------------
    async def _run():
        outputs = get_outputs(run)
        sample = SingleTurnSample(
                retrieved_context_ids=outputs.get("retrieved_context_ids", []),
                reference_context_ids=example.outputs.get("reference_context_ids", [])
            )
        scorer = IDBasedContextPrecision()

        return await scorer.single_turn_ascore(sample)
    return asyncio.run(_run())


# --- OLD CODE (Caused RuntimeError: There is no current event loop in thread 'ThreadPoolExecutor') ---
# async def ragas_context_recall_id_based(run, example):
#     outputs = get_outputs(run)
#     sample = SingleTurnSample(
#             retrieved_context_ids=outputs.get("retrieved_context_ids", []),
#             reference_context_ids=example.outputs.get("reference_context_ids", [])
#         )
#     scorer = IDBasedContextRecall()
#     return await scorer.single_turn_ascore(sample)
# ------------------------------------------------------------------------------------------------

# NEW CODE: Changed to synchronous `def` and added `asyncio.run()` to safely create an event loop for LangSmith's thread pool
def ragas_context_recall_id_based(run, example):
    # --- OLD CODE (Caused KeyError) ---
    # sample = SingleTurnSample(
    #         retrieved_context_ids=run.outputs["retrieved_context_ids"],
    #         reference_context_ids=example.outputs["reference_context_ids"]
    #     )
    # ----------------------------------
    async def _run():
        outputs = get_outputs(run)
        sample = SingleTurnSample(
                retrieved_context_ids=outputs.get("retrieved_context_ids", []),
                reference_context_ids=example.outputs.get("reference_context_ids", [])
            )
        scorer = IDBasedContextRecall()

        return await scorer.single_turn_ascore(sample)
    return asyncio.run(_run())


def rate_limited_rag_pipeline(question):
    # --- OLD CODE (Throttled for Gemini API limits) ---
    # time.sleep(15)
    # --------------------------------------------------
    return rag_pipeline(question)

# --- OLD CODE (Caused the target function to hit rate limits because it ran too fast without a buffer) ---
# results = ls_client.evaluate(
#     lambda x: rag_pipeline(x["question"]),
# --------------------------------------------------------------------------

# NEW CODE: Wrapped rag_pipeline in rate_limited_rag_pipeline to guarantee a 15s delay between target function evaluations
results = ls_client.evaluate(
    lambda x: rate_limited_rag_pipeline(x["question"]),
    data="ollama-70b-amazon-dataset",
    evaluators=[
        ragas_faithfulness,
        ragas_responce_relevancy,
        ragas_context_precision_id_based,
        ragas_context_recall_id_based
    ],
    experiment_prefix="retriever-eval-v2",
    
    # --- OLD CODE (Removed because Groq handles parallel requests easily, unlike Gemini Free Tier) ---
    # max_concurrency=1, # FORCE LangSmith to process only 1 row at a time to prevent rate limits
    # -------------------------------------------------------------------------------------------------
)