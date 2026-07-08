# LangSmith Implementation Guide

This document provides a comprehensive overview of how LangSmith is integrated into this project for observability, tracing, and monitoring of the RAG (Retrieval-Augmented Generation) pipeline.

## Table of Contents

1. [What is LangSmith?](#what-is-langsmith)
2. [Why Use LangSmith?](#why-use-langsmith)
3. [Configuration](#configuration)
4. [Implementation Overview](#implementation-overview)
5. [The @traceable Decorator](#the-traceable-decorator)
6. [Run Types Explained](#run-types-explained)
7. [Capturing Custom Metrics](#capturing-custom-metrics)
8. [Trace Hierarchy](#trace-hierarchy)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## What is LangSmith?

LangSmith is an observability and evaluation platform developed by LangChain specifically designed for LLM applications. It provides:

- **Tracing**: Visualize the execution flow of your LLM pipelines
- **Debugging**: Identify issues in complex multi-step AI workflows
- **Monitoring**: Track performance, latency, and costs in production
- **Evaluation**: Compare different prompts, models, and retrieval strategies

---

## Why Use LangSmith?

When building LLM applications like RAG pipelines, several challenges arise that LangSmith addresses:

### 1. Debugging Complex Pipelines
RAG systems involve multiple components (embedding, retrieval, prompt construction, generation). When something goes wrong, it can be difficult to pinpoint the issue. LangSmith provides visibility into each step.

### 2. Cost Tracking
LLM API calls can be expensive. By tracking token usage at each step, you can:
- Identify which operations consume the most tokens
- Optimize prompts to reduce costs
- Set budgets and alerts

### 3. Performance Monitoring
Understanding latency across your pipeline helps you:
- Identify bottlenecks
- Compare different models or configurations
- Ensure acceptable response times

### 4. Quality Assurance
LangSmith allows you to:
- Review inputs and outputs of each step
- Compare different retrieval strategies
- Evaluate answer quality over time

---

## Configuration

LangSmith is configured through environment variables. The following variables must be set:

```bash
# Enable or disable tracing (set to "true" to enable)
LANGSMITH_TRACING=true

# LangSmith API endpoint (use the default for cloud service)
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

# Your LangSmith API key (obtain from LangSmith dashboard)
LANGSMITH_API_KEY=<your-api-key>

# Project name for organizing traces in LangSmith
LANGSMITH_PROJECT="cohort-project"
```

### How to Obtain Your API Key

1. Create an account at [smith.langchain.com](https://smith.langchain.com)
2. Navigate to Settings > API Keys
3. Generate a new API key
4. Add it to your `.env` file

### Dependency Installation

LangSmith is included in the project dependencies:

```toml
# In pyproject.toml
dependencies = [
    "langsmith>=0.6.4",
    # ... other dependencies
]
```

---

## Implementation Overview

The LangSmith integration is implemented in the RAG pipeline located at:
```
apps/api/src/api/agents/retrieval_generation.py
```

### Key Imports

```python
from langsmith import traceable, get_current_run_tree
```

- **`traceable`**: A decorator that automatically traces function execution
- **`get_current_run_tree`**: Provides access to the current trace context for adding custom metadata

---

## The @traceable Decorator

The `@traceable` decorator is the primary mechanism for instrumenting functions with LangSmith. It automatically captures:

- Function inputs (arguments)
- Function outputs (return values)
- Execution time
- Any errors that occur

### Basic Usage

```python
@traceable(name="my_function")
def my_function(input_text):
    # Your logic here
    return result
```

### Decorator Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `name` | Display name in LangSmith UI | `"embed_query"` |
| `run_type` | Categorizes the operation type | `"llm"`, `"retriever"`, `"embedding"` |
| `metadata` | Additional key-value pairs for filtering and analysis | `{"ls_provider": "openai"}` |

### Example with All Parameters

```python
@traceable(
    name="generate_answer",
    run_type="llm",
    metadata={"ls_provider": "openai", "ls_model_name": "gpt-5-nano"}
)
def generate_answer(prompt):
    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content
```

---

## Run Types Explained

LangSmith uses `run_type` to categorize different operations in your pipeline. This enables specialized visualization and filtering in the UI.

### Available Run Types

| Run Type | Purpose | When to Use |
|----------|---------|-------------|
| `"llm"` | Language model calls | Any call to an LLM API (OpenAI, Anthropic, etc.) |
| `"embedding"` | Embedding generation | Creating vector embeddings from text |
| `"retriever"` | Document retrieval | Fetching relevant documents from a vector store |
| `"prompt"` | Prompt construction | Building or formatting prompts |
| `"chain"` | Multi-step chains | Orchestrating multiple operations |
| `"tool"` | Tool execution | Running external tools or APIs |

### How Run Types Are Used in This Project

```python
# Embedding generation
@traceable(name="embed_query", run_type="embedding")
def get_embedding(text, model="text-embedding-3-small"):
    ...

# Document retrieval from vector database
@traceable(name="retrieve_data", run_type="retriever")
def retrieve_data(query, qdrant_client, k=5):
    ...

# Prompt construction
@traceable(name="build_prompt", run_type="prompt")
def build_prompt(preprocessed_context, question):
    ...

# LLM answer generation
@traceable(name="generate_answer", run_type="llm")
def generate_answer(prompt):
    ...
```

---

## Capturing Custom Metrics

Beyond automatic tracing, you can add custom metrics using `get_current_run_tree()`. This is particularly useful for tracking token usage and costs.

### Token Usage Example

```python
from langsmith import traceable, get_current_run_tree

@traceable(
    name="generate_answer",
    run_type="llm",
    metadata={"ls_provider": "openai", "ls_model_name": "gpt-5-nano"}
)
def generate_answer(prompt):
    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "system", "content": prompt}]
    )

    # Access the current trace context
    current_run = get_current_run_tree()

    if current_run:
        # Add token usage to the trace metadata
        current_run.metadata["usage_metadata"] = {
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }

    return response.choices[0].message.content
```

### Why Check for `current_run`?

The `if current_run:` check ensures the code works even when:
- LangSmith tracing is disabled (`LANGSMITH_TRACING=false`)
- Running in environments without LangSmith configuration
- Unit testing without LangSmith dependencies

---

## Trace Hierarchy

When you nest `@traceable` functions, LangSmith automatically creates a hierarchical trace. This provides a clear visualization of your pipeline's execution flow.

### Our RAG Pipeline Hierarchy

```
rag_pipeline (root)
├── retrieve_data
│   └── get_embedding
├── process_context
├── build_prompt
└── generate_answer
```

### Implementation

```python
@traceable(name="rag_pipeline")
def rag_pipeline(question, qdrant_client, top_k=5):
    # Each of these calls is traced as a child of rag_pipeline
    retrieved_context = retrieve_data(question, qdrant_client, top_k)
    preprocessed_context = process_context(retrieved_context)
    prompt = build_prompt(preprocessed_context, question)
    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "question": question,
        "retrieved_context_ids": retrieved_context["retrieved_context_ids"],
        "retrieved_context": retrieved_context["retrieved_context"],
        "similarity_scores": retrieved_context["similarity_scores"]
    }
```

### Benefits of Hierarchical Tracing

1. **Visual Debugging**: See exactly where time is spent in the UI
2. **Error Localization**: Identify which step failed in a multi-step pipeline
3. **Performance Analysis**: Compare latency across different operations
4. **Data Flow Visibility**: See inputs and outputs at each step

---

## Best Practices

### 1. Use Descriptive Names
Choose names that clearly describe what the function does:
```python
# Good
@traceable(name="embed_query")
@traceable(name="retrieve_product_data")

# Avoid
@traceable(name="step1")
@traceable(name="process")
```

### 2. Include Provider and Model Metadata
This enables filtering and comparison in LangSmith:
```python
@traceable(
    name="generate_answer",
    run_type="llm",
    metadata={"ls_provider": "openai", "ls_model_name": "gpt-5-nano"}
)
```

### 3. Track Token Usage
Always capture token usage for LLM and embedding calls to enable cost tracking:
```python
current_run = get_current_run_tree()
if current_run:
    current_run.metadata["usage_metadata"] = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens
    }
```

### 4. Use Appropriate Run Types
Select the correct `run_type` for proper categorization in the UI.

### 5. Trace at the Right Granularity
- Too fine: Tracing every small helper function adds noise
- Too coarse: Tracing only the top-level function loses visibility
- Just right: Trace logical steps in your pipeline

---

## Troubleshooting

### Traces Not Appearing in LangSmith

1. **Verify Environment Variables**
   ```bash
   echo $LANGSMITH_TRACING  # Should be "true"
   echo $LANGSMITH_API_KEY  # Should be set
   ```

2. **Check API Key Validity**
   - Ensure the API key is correct and not expired
   - Verify the key has the necessary permissions

3. **Verify Project Name**
   - Check that `LANGSMITH_PROJECT` matches your project in the LangSmith UI
   - Create the project if it doesn't exist

### Token Usage Not Being Captured

1. **Check the Null Guard**
   ```python
   current_run = get_current_run_tree()
   if current_run:  # This might be None if tracing is disabled
       current_run.metadata["usage_metadata"] = {...}
   ```

2. **Verify API Response Structure**
   - Ensure the API response includes usage information
   - Some API configurations might not return token counts

### Performance Impact

LangSmith tracing adds minimal overhead:
- Traces are sent asynchronously
- The decorator adds negligible latency
- For high-throughput applications, consider sampling

To disable tracing in performance-critical environments:
```bash
LANGSMITH_TRACING=false
```

---

## Further Reading

- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangSmith Python SDK](https://github.com/langchain-ai/langsmith-sdk)
- [LangChain Observability Guide](https://python.langchain.com/docs/langsmith/)

---

## Summary

This project demonstrates a production-ready LangSmith integration that provides:

- Complete tracing of the RAG pipeline
- Token usage tracking for cost analysis
- Hierarchical visualization of the execution flow
- Metadata enrichment for filtering and comparison

By following this guide, you can understand, maintain, and extend the observability capabilities of this application.
