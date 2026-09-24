run-docker-compose:
	uv sync
	docker compose up --build

clean-notebook-outputs:
	jupyter nbconvert --clear-output --inplace notebooks/*/*.ipynb

run-evals-retriever:
	uv sync
	# 1. Run the Dataset Generator first (It will automatically skip if dataset already exists, unless FORCE=true)
	PYTHONPATH=${PWD}/apps/api:${PWD}/apps/api/src:$$PYTHONPATH:${PWD} QDRANT_URL="http://localhost:6333" FORCE_REGENERATE=$(FORCE) uv run --env-file .env python apps/api/evals/generate_dataset.py
	
	# 2. Run the Evaluator
	PYTHONPATH=${PWD}/apps/api:${PWD}/apps/api/src:$$PYTHONPATH:${PWD} QDRANT_URL="http://localhost:6333" uv run --env-file .env python -m evals.eval_retriever