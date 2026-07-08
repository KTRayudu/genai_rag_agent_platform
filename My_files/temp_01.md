## Part 5: Notebooks

---

## Part 5.0: LLM API Prerequisites (`notebooks/prerequisites/01-llm-apis.ipynb`)

### Overview
Before building a complex RAG system, we must ensure our foundational tools—the LLM APIs—are configured and responding correctly. This short prerequisite notebook acts as a "Hello World" to verify connectivity with three major AI providers: OpenAI, Google (Gemini), and Groq. 

### Step 1: Loading the Environment
```python
from dotenv import load_dotenv
import os

load_dotenv("../../.env")
```
*   **The "Why"**: APIs require authentication via secret keys. Instead of hardcoding them (a major security risk), we load them securely from the `.env` file located in the root of our workspace.

### Step 2: Testing the Clients
The notebook proceeds to test each client individually by asking them to "print random words".

1.  **OpenAI Client**: Tests connectivity using the standard `openai` SDK. 
2.  **Google GenAI Client**: Uses the `google-genai` SDK and our `GOOGLE_API_KEY` to prompt the `gemini-2.5-flash` model. This is the model we will use for our final RAG generation.
3.  **Groq Client**: Tests Groq's high-speed inference engine using the `llama-3.3-70b-versatile` open-source model.

If all three cells execute and return random words without `Unauthorized` or `Connection` errors, our environment is fully ready for the bootcamp.

---

## Part 5.1: Exploring the Amazon Dataset (`notebooks/week_1/01-explore-amazon-dataset.ipynb`)

### Overview
Data wrangling is the unglamorous but essential first step of any ML project. In this notebook, we take the massive raw Amazon Electronics dataset (millions of rows) and filter it down into a clean, highly relevant subset of 100 items that we can comfortably embed and search locally on our laptops.

### Step 1: Parsing Raw JSONL Data
The raw data comes in `.jsonl` (JSON Lines) format, where every single line is a complete JSON object representing one product.

```python
import json
import pandas as pd

with open('../../data/meta_Electronics.jsonl', 'r') as f:
    first_line = json.loads(f.readline())
```
*   **The "Why"**: We inspect the first line to understand the schema. We discover fields like `title`, `average_rating`, `description`, `images`, and `details`.

### Step 2: Temporal Filtering (2022 and Newer)
RAG systems are often used to answer questions about *recent* data. We write a filter to only keep products that became available in 2022 or later.

```python
def filter_data(data: dict) -> dict:
    filter = False
    if int(data['details']['Date First Available'][-4:]) < 2022:
        filter = True
    return filter
```
*   **The "Why"**: We open the massive raw file, stream it line-by-line (to prevent running out of RAM), apply this filter, and write the valid lines to a new file: `meta_Electronics_2022_2023.jsonl`.

### Step 3: Categorical Filtering
We apply a second pass to remove any products that lack a `main_category` tag.

```python
def filter_category(data: dict) -> dict:
    filter = False
    if data['main_category'] == None:
        filter = True
    return filter
```

### Step 4: Data Visualization & Subsetting
We load our cleaned, recent, categorized data into a Pandas DataFrame to visualize it.

```python
df = pd.read_json("../../data/meta_Electronics_2022_2023_with_category.jsonl", lines=True)

# Count products per category
category_counts = df['main_category'].value_counts()
category_counts.plot(kind='bar', figsize=(10, 6))
```
*   **The "Why"**: Visualizing the distribution ensures we don't have massive imbalances (e.g., 99% phone cases and 1% laptops).
*   **The Final Output**: Finally, we extract exactly 100 diverse rows and save them to `Amazon-items-subset-100.jsonl`. This small, perfectly formatted file is what our RAG pipeline will ingest in the next notebook.

---

