rayudu@tungsten:~/otherwork_assignment_all_jobs/Todo/genai_rag_agent_platform$ source .venv/bin/activate
(cohort-repo) rayudu@tungsten:~/otherwork_assignment_all_jobs/Todo/genai_rag_agent_platform$ make run-docker-compose
uv sync
Resolved 182 packages in 1ms
Checked 170 packages in 1ms
docker compose up --build
[+] Building 4.0s (18/22)                                                                                                                                
 => [internal] load local bake definitions                                                                                                          0.0s
 => => reading from stdin 1.21kB                                                                                                                    0.0s
 => [api internal] load build definition from Dockerfile                                                                                            0.1s
 => => transferring dockerfile: 1.16kB                                                                                                              0.0s
 => [streamlit-app internal] load build definition from Dockerfile                                                                                  0.1s
 => => transferring dockerfile: 1.36kB                                                                                                              0.0s
 => [api internal] load metadata for ghcr.io/astral-sh/uv:python3.12-bookworm-slim                                                                  0.8s
 => [streamlit-app internal] load .dockerignore                                                                                                     0.0s
 => => transferring context: 93B                                                                                                                    0.0s
 => [streamlit-app internal] load build context                                                                                                     0.1s
 => => transferring context: 710.22kB                                                                                                               0.0s
 => CACHED [api stage-0 1/8] FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa  0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa78e58                0.0s
 => [api internal] load build context                                                                                                               0.1s
 => => transferring context: 725.80kB                                                                                                               0.0s
 => [streamlit-app stage-0 2/8] RUN addgroup --system app &&     adduser --system --ingroup app app &&     mkdir -p /home/app/.streamlit/data /hom  0.6s
 => [api stage-0 2/8] RUN addgroup --system app &&     adduser --system --ingroup app app &&     mkdir -p /home/app /app                            0.6s
 => [api stage-0 3/8] WORKDIR /app                                                                                                                  0.1s
 => [streamlit-app stage-0 3/8] WORKDIR /app                                                                                                        0.1s
 => [api stage-0 4/8] COPY pyproject.toml uv.lock ./                                                                                                0.1s 
 => [streamlit-app stage-0 4/8] COPY pyproject.toml uv.lock ./                                                                                      0.1s 
 => [api stage-0 5/8] COPY apps/api ./apps/api                                                                                                      0.1s 
 => [streamlit-app stage-0 5/8] COPY apps/chatbot_ui ./apps/chatbot_ui                                                                              0.1s 
 => ERROR [api stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package api                               1.8s
 => ERROR [streamlit-app stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package chatbot_ui              1.7s
------                                                                                                                                                   
 > [api stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package api:                                          
0.490 Using CPython 3.12.12 interpreter at: /usr/local/bin/python3                                                                                       
0.490 Creating virtual environment at: .venv                                                                                                             
0.509    Building api @ file:///app/apps/api                                                                                                             
0.530 Downloading zstandard (5.3MiB)                                                                                                                     
0.531 Downloading grpcio (6.3MiB)                                                                                                                        
0.532 Downloading openai (1.0MiB)                                                                                                                        
0.540 Downloading numpy (15.6MiB)                                                                                                                        
0.542 Downloading pydantic-core (2.0MiB)
0.832  Downloaded openai
0.962  Downloaded pydantic-core
1.264  Downloaded zstandard
1.334  Downloaded grpcio
1.440   × Failed to build `api @ file:///app/apps/api`
1.440   ├─▶ The build backend returned an error
1.440   ╰─▶ Call to `hatchling.build.build_editable` failed (exit status: 1)
1.440 
1.440       [stderr]
1.440       Traceback (most recent call last):
1.440         File "<string>", line 11, in <module>
1.440         File
1.440       "/home/app/.cache/uv/builds-v0/.tmpKY9CAG/lib/python3.12/site-packages/hatchling/build.py",
1.440       line 83, in build_editable
1.440           return os.path.basename(next(builder.build(directory=wheel_directory,
1.440       versions=["editable"])))
1.440       
1.440       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.440         File
1.440       "/home/app/.cache/uv/builds-v0/.tmpKY9CAG/lib/python3.12/site-packages/hatchling/builders/plugin/interface.py",
1.440       line 92, in build
1.440           self.metadata.validate_fields()
1.440         File
1.440       "/home/app/.cache/uv/builds-v0/.tmpKY9CAG/lib/python3.12/site-packages/hatchling/metadata/core.py",
1.440       line 266, in validate_fields
1.440           self.core.validate_fields()
1.440         File
1.440       "/home/app/.cache/uv/builds-v0/.tmpKY9CAG/lib/python3.12/site-packages/hatchling/metadata/core.py",
1.440       line 1437, in validate_fields
1.440           getattr(self, attribute)
1.440         File
1.440       "/home/app/.cache/uv/builds-v0/.tmpKY9CAG/lib/python3.12/site-packages/hatchling/metadata/core.py",
1.440       line 533, in readme
1.440           raise OSError(message)
1.440       OSError: Readme file does not exist: README.md
1.440 
1.440       hint: This usually indicates a problem with the package or the build
1.440       environment.
------
------
 > [streamlit-app stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package chatbot_ui:
0.424 Using CPython 3.12.12 interpreter at: /usr/local/bin/python3
0.424 Creating virtual environment at: .venv
0.448    Building chatbot-ui @ file:///app/apps/chatbot_ui
0.468 Downloading pydantic-core (2.0MiB)
0.469 Downloading numpy (15.6MiB)
0.469 Downloading streamlit (8.7MiB)
0.469 Downloading pydeck (6.6MiB)
0.472 Downloading pillow (6.7MiB)
0.472 Downloading pandas (11.8MiB)
0.479 Downloading pyarrow (45.4MiB)
0.736  Downloaded pydantic-core
1.149  Downloaded pydeck
1.157  Downloaded pillow
1.266  Downloaded streamlit
1.336   × Failed to build `chatbot-ui @ file:///app/apps/chatbot_ui`
1.336   ├─▶ The build backend returned an error
1.336   ╰─▶ Call to `hatchling.build.build_editable` failed (exit status: 1)
1.336 
1.336       [stderr]
1.336       Traceback (most recent call last):
1.336         File "<string>", line 11, in <module>
1.336         File
1.336       "/home/app/.cache/uv/builds-v0/.tmpOBnIvn/lib/python3.12/site-packages/hatchling/build.py",
1.336       line 83, in build_editable
1.336           return os.path.basename(next(builder.build(directory=wheel_directory,
1.336       versions=["editable"])))
1.336       
1.336       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.336         File
1.336       "/home/app/.cache/uv/builds-v0/.tmpOBnIvn/lib/python3.12/site-packages/hatchling/builders/plugin/interface.py",
1.336       line 92, in build
1.336           self.metadata.validate_fields()
1.336         File
1.336       "/home/app/.cache/uv/builds-v0/.tmpOBnIvn/lib/python3.12/site-packages/hatchling/metadata/core.py",
1.336       line 266, in validate_fields
1.336           self.core.validate_fields()
1.336         File
1.336       "/home/app/.cache/uv/builds-v0/.tmpOBnIvn/lib/python3.12/site-packages/hatchling/metadata/core.py",
1.336       line 1437, in validate_fields
1.336           getattr(self, attribute)
1.336         File
1.336       "/home/app/.cache/uv/builds-v0/.tmpOBnIvn/lib/python3.12/site-packages/hatchling/metadata/core.py",
1.336       line 533, in readme
1.336           raise OSError(message)
1.336       OSError: Readme file does not exist: README.md
1.336 
1.336       hint: This usually indicates a problem with the package or the build
1.336       environment.
------
[+] up 0/2
 ⠙ Image genai_rag_agent_platform-streamlit-app Building                                                                                             4.0s
 ⠙ Image genai_rag_agent_platform-api           Building                                                                                             4.0s
Dockerfile:27

--------------------

  26 |     # Install dependencies AS ROOT (before switching to app user)

  27 | >>> RUN --mount=type=cache,target=/root/.cache/uv \

  28 | >>>     uv sync --frozen --no-dev --package api

  29 |     

--------------------

target api: failed to solve: process "/bin/sh -c uv sync --frozen --no-dev --package api" did not complete successfully: exit code: 1

make: *** [Makefile:3: run-docker-compose] Error 1
(cohort-repo) rayudu@tungsten:~/otherwork_assignment_all_jobs/Todo/genai_rag_agent_platform$ 
=============================================================================================


## Resolution

### Root Cause
The `docker compose up --build` command is failing during the `uv sync` step for both the `api` and `chatbot_ui` images. 
The error output specifically states:
```
OSError: Readme file does not exist: README.md
```

This happens because the `pyproject.toml` files located inside `apps/api/` and `apps/chatbot_ui/` both specify a readme file:
```toml
[project]
...
readme = "README.md"
```
However, there is no `README.md` file present in the `apps/api/` and `apps/chatbot_ui/` directories. When the `hatchling` build backend attempts to build the packages during `uv sync`, it crashes because it cannot find the specified `README.md` files.

### End-to-End Fix

You have two simple options to fix this issue:

**Option 1: Create the missing README.md files (Recommended)**
Simply create an empty (or basic) `README.md` file inside both application directories.

Run the following commands in your terminal:
```bash
touch apps/api/README.md
touch apps/chatbot_ui/README.md
```

**Option 2: Remove the readme requirement from pyproject.toml**
If you don't want to maintain README files for the sub-packages, remove the `readme = "README.md"` line from the `pyproject.toml` configuration files.

1. Open `apps/api/pyproject.toml` and delete line 5: `readme = "README.md"`.
2. Open `apps/chatbot_ui/pyproject.toml` and delete line 5: `readme = "README.md"`.

After applying either option, re-run your build command:
```bash
make run-docker-compose
```
It should now build successfully.===================================================================================================


Hello! How can I assist you today?

hi can you give me best electronics rating above 4.5 earphones

KeyError: 'answer'
Traceback:
File "/app/apps/chatbot_ui/src/chatbot_ui/app.py", line 56, in <module>
    answer = response_data["answer"]
             ~~~~~~~~~~~~~^^^^^^^^^^












FastAPI
 0.1.0 
OAS 3.1
/openapi.json
rag


POST
/rag/
Rag

Parameters
Cancel
Reset
No parameters

Request body

application/json
Edit Value
Schema
{
  "query": "can you give earphones rating above 4.5"
}
Execute
Clear
Responses
Curl

curl -X 'POST' \
  'http://localhost:8000/rag/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "can you give earphones rating above 4.5"
}'
Request URL
http://localhost:8000/rag/
Server response
Code	Details
500
Undocumented
Error: Internal Server Error

Response body
Download
Internal Server Error
Response headers
 content-length: 21 
 content-type: text/plain; charset=utf-8 
 date: Wed,08 Jul 2026 19:27:15 GMT 
 server: uvicorn 
Responses
Code	Description	Links
200	
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
  "request_id": "string",
  "answer": "string"
}
No links
422	
Validation Error

Media type

application/json
Example Value
Schema
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}














make: *** [Makefile:3: run-docker-compose] Error 1
(cohort-repo) rayudu@tungsten:~/otherwork_assignment_all_jobs/Todo/genai_rag_agent_platform$ make run-docker-compose
uv sync
Resolved 182 packages in 1ms
Checked 170 packages in 0.90ms
docker compose up --build
[+] Building 212.6s (26/26) FINISHED                                                                                                                     
 => [internal] load local bake definitions                                                                                                          0.0s
 => => reading from stdin 1.21kB                                                                                                                    0.0s
 => [api internal] load build definition from Dockerfile                                                                                            0.0s
 => => transferring dockerfile: 1.16kB                                                                                                              0.0s
 => [streamlit-app internal] load build definition from Dockerfile                                                                                  0.1s
 => => transferring dockerfile: 1.36kB                                                                                                              0.0s
 => [api internal] load metadata for ghcr.io/astral-sh/uv:python3.12-bookworm-slim                                                                  0.4s
 => [api internal] load .dockerignore                                                                                                               0.0s
 => => transferring context: 93B                                                                                                                    0.0s
 => [api internal] load build context                                                                                                               0.1s
 => => transferring context: 20.54kB                                                                                                                0.0s
 => [streamlit-app stage-0 1/8] FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147  0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa78e58                0.0s
 => [streamlit-app internal] load build context                                                                                                     0.0s
 => => transferring context: 4.98kB                                                                                                                 0.0s
 => CACHED [streamlit-app stage-0 2/8] RUN addgroup --system app &&     adduser --system --ingroup app app &&     mkdir -p /home/app/.streamlit/da  0.0s
 => CACHED [streamlit-app stage-0 3/8] WORKDIR /app                                                                                                 0.0s
 => CACHED [streamlit-app stage-0 4/8] COPY pyproject.toml uv.lock ./                                                                               0.0s
 => CACHED [api stage-0 2/8] RUN addgroup --system app &&     adduser --system --ingroup app app &&     mkdir -p /home/app /app                     0.0s
 => CACHED [api stage-0 3/8] WORKDIR /app                                                                                                           0.0s
 => CACHED [api stage-0 4/8] COPY pyproject.toml uv.lock ./                                                                                         0.0s
 => [streamlit-app stage-0 5/8] COPY apps/chatbot_ui ./apps/chatbot_ui                                                                              0.2s
 => [api stage-0 5/8] COPY apps/api ./apps/api                                                                                                      0.2s
 => [api stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package api                                     3.6s
 => [streamlit-app stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package chatbot_ui                    3.6s
 => [api stage-0 7/8] RUN chown -R app:app /app /home/app                                                                                         145.6s
 => [streamlit-app stage-0 7/8] RUN chown -R app:app /app /home/app                                                                               180.5s
 => [api stage-0 8/8] WORKDIR /app/apps/api/src                                                                                                     0.3s 
 => [api] exporting to image                                                                                                                       11.8s 
 => => exporting layers                                                                                                                             8.5s 
 => => exporting manifest sha256:388acc2f7cb03abac7cf86ee99e254b3af939c2aaae96f6e2181eeb53d8f53e9                                                   0.1s 
 => => exporting config sha256:d0ebadfbfbe91b90aa3b684033eca39f4bfca0153b1de669ca518e35e6c76daf                                                     0.1s 
 => => exporting attestation manifest sha256:97bd7ff15425703c627e35c7c87a8bc813f635263b25393d24f49e54fdf8a61a                                       0.1s 
 => => exporting manifest list sha256:3fe61207e9ade75d59261ff8642f3f48019c45aefdc5ff47bae3a012027828e1                                              0.1s 
 => => naming to docker.io/library/genai_rag_agent_platform-api:latest                                                                              0.0s
 => => unpacking to docker.io/library/genai_rag_agent_platform-api:latest                                                                           2.8s
 => [api] resolving provenance for metadata file                                                                                                    0.0s
 => [streamlit-app stage-0 8/8] WORKDIR /app/apps/chatbot_ui/src                                                                                    0.2s
 => [streamlit-app] exporting to image                                                                                                             27.1s
 => => exporting layers                                                                                                                            21.4s
 => => exporting manifest sha256:379341d9fd13d277d39cfd29c0b623b29639a97e49508c4a3472dadc97eb04a2                                                   0.0s
 => => exporting config sha256:ff12300de927580e61ed4e9591e410bdf98a2d5a1ed06a5fb7f0b9f8aeb6778c                                                     0.0s
 => => exporting attestation manifest sha256:7cb982d60518788ca7323ce3d3502b438351ce5d94b579802c464e100390ccd3                                       0.1s
 => => exporting manifest list sha256:76de7f01e7424a575b4677fb92e8fe994ecb005a01566ef58acd4154417c92d4                                              0.0s
 => => naming to docker.io/library/genai_rag_agent_platform-streamlit-app:latest                                                                    0.0s
 => => unpacking to docker.io/library/genai_rag_agent_platform-streamlit-app:latest                                                                 5.5s
 => [streamlit-app] resolving provenance for metadata file                                                                                          0.0s
[+] up 6/6
 ✔ Image genai_rag_agent_platform-streamlit-app       Built                                                                                        212.7s
 ✔ Image genai_rag_agent_platform-api                 Built                                                                                        212.7s
 ✔ Network genai_rag_agent_platform_default           Created                                                                                        0.0s
 ✔ Container genai_rag_agent_platform-streamlit-app-1 Created                                                                                        1.8s
 ✔ Container genai_rag_agent_platform-qdrant-1        Created                                                                                        1.8s
 ✔ Container genai_rag_agent_platform-api-1           Created                                                                                        1.8s
Attaching to api-1, qdrant-1, streamlit-app-1
qdrant-1  |            _                 _    
qdrant-1  |   __ _  __| |_ __ __ _ _ __ | |_  
qdrant-1  |  / _` |/ _` | '__/ _` | '_ \| __| 
qdrant-1  | | (_| | (_| | | | (_| | | | | |_  
qdrant-1  |  \__, |\__,_|_|  \__,_|_| |_|\__| 
qdrant-1  |     |_|                           
qdrant-1  | 
qdrant-1  | Version: 1.18.2, build: 44ad62f8
qdrant-1  | Access web UI at http://localhost:6333/dashboard
qdrant-1  | Agentic Skills: https://skills.qdrant.tech/
qdrant-1  | 
qdrant-1  | 2026-07-08T19:05:01.660408Z  INFO storage::content_manager::consensus::persistent: Initializing new raft state at ./storage/raft_state.json
qdrant-1  | 2026-07-08T19:05:01.720669Z  INFO qdrant: Distributed mode disabled
qdrant-1  | 2026-07-08T19:05:01.720694Z  INFO qdrant: Telemetry reporting enabled, id: ab74bff0-c445-4d2a-bcd1-7b591610757d
qdrant-1  | 2026-07-08T19:05:01.729612Z  INFO qdrant::actix: REST transport settings: keep_alive=5s, client_request_timeout=5s, client_disconnect_timeout=5s
qdrant-1  | 2026-07-08T19:05:01.729630Z  INFO qdrant::actix: TLS disabled for REST API
qdrant-1  | 2026-07-08T19:05:01.729672Z  INFO qdrant::actix: Qdrant HTTP listening on 6333
qdrant-1  | 2026-07-08T19:05:01.729675Z  INFO actix_server::builder: starting 63 workers
qdrant-1  | 2026-07-08T19:05:01.729678Z  INFO actix_server::server: Actix runtime found; starting in Actix runtime
qdrant-1  | 2026-07-08T19:05:01.729681Z  INFO actix_server::server: starting service: "actix-web-service-0.0.0.0:6333", workers: 63, listening on: 0.0.0.0:6333
qdrant-1  | 2026-07-08T19:05:01.730178Z  INFO qdrant::tonic: Qdrant gRPC listening on 6334
qdrant-1  | 2026-07-08T19:05:01.730193Z  INFO qdrant::tonic: TLS disabled for gRPC API
streamlit-app-1  |    Building chatbot-ui @ file:///app/apps/chatbot_ui
api-1            |    Building api @ file:///app/apps/api
streamlit-app-1  |       Built chatbot-ui @ file:///app/apps/chatbot_ui
streamlit-app-1  | Uninstalled 1 package in 24ms
streamlit-app-1  | Installed 1 package in 0.62ms
streamlit-app-1  | Bytecode compiled 3279 files in 144ms
api-1            |       Built api @ file:///app/apps/api
api-1            | Uninstalled 1 package in 23ms
api-1            | Installed 1 package in 0.82ms
streamlit-app-1  | 
streamlit-app-1  | Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
streamlit-app-1  | 
streamlit-app-1  | 
streamlit-app-1  |   You can now view your Streamlit app in your browser.
streamlit-app-1  | 
streamlit-app-1  |   URL: http://0.0.0.0:8501
streamlit-app-1  | 
api-1            | Bytecode compiled 3032 files in 237ms
api-1            | INFO:     Will watch for changes in these directories: ['/app/apps/api/src']
api-1            | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
api-1            | INFO:     Started reloader process [291] using StatReload
api-1            | 2026-07-08 19:05:06,015 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [293]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
qdrant-1         | 2026-07-08T19:06:20.702772Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard HTTP/1.1" 200 925 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000748
qdrant-1         | 2026-07-08T19:06:20.726847Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/manifest.json HTTP/1.1" 200 248 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000951
qdrant-1         | 2026-07-08T19:06:20.728573Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/index-BG9q9yEd.css HTTP/1.1" 200 24126 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.002544
qdrant-1         | 2026-07-08T19:06:20.787559Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/index-C3k9zy-X.js HTTP/1.1" 200 1452548 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.061676
qdrant-1         | 2026-07-08T19:06:20.971126Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/openapi.json HTTP/1.1" 200 50091 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.003302
qdrant-1         | 2026-07-08T19:06:21.063325Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 62 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000169
qdrant-1         | 2026-07-08T19:06:21.064642Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/cloud/data.json HTTP/1.1" 404 0 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000059
qdrant-1         | 2026-07-08T19:06:21.067573Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/logo-red-black.svg HTTP/1.1" 200 2781 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000908
qdrant-1         | 2026-07-08T19:06:21.081391Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/fonts/Mona_Sans/MonaSans-VariableFont_wdth,wght.ttf HTTP/1.1" 200 209961 "http://localhost:6333/dashboard/assets/index-BG9q9yEd.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.005786
qdrant-1         | 2026-07-08T19:06:21.091958Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/favicon.ico HTTP/1.1" 200 15086 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000333
qdrant-1         | 2026-07-08T19:06:21.092127Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/logo192.png HTTP/1.1" 200 6177 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000192
qdrant-1         | 2026-07-08T19:06:21.115589Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/console.svg HTTP/1.1" 200 10386 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.001180
qdrant-1         | 2026-07-08T19:06:23.376457Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 62 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000176
qdrant-1         | 2026-07-08T19:06:23.377434Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 63 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000119
qdrant-1         | 2026-07-08T19:06:23.385927Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 60 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.004464
qdrant-1         | 2026-07-08T19:06:23.387157Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 60 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000103
qdrant-1         | 2026-07-08T19:11:29.339307Z  INFO storage::content_manager::toc::collection_meta_ops: Creating collection Amazon-items-collection-03
qdrant-1         | 2026-07-08T19:11:29.632488Z  INFO actix_web::middleware::logger: 172.19.0.1 "PUT /collections/Amazon-items-collection-03 HTTP/1.1" 200 57 "-" "python-client/1.16.2 python/3.12.3" 0.298509
qdrant-1         | 2026-07-08T19:12:22.103884Z  INFO actix_web::middleware::logger: 172.19.0.1 "PUT /collections/Amazon-items-collection-03/points?wait=true HTTP/1.1" 200 84 "-" "python-client/1.16.2 python/3.12.3" 0.025708
qdrant-1         | 2026-07-08T19:12:29.973619Z  INFO actix_web::middleware::logger: 172.19.0.1 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 7268 "-" "python-client/1.16.2 python/3.12.3" 0.002699
qdrant-1         | 2026-07-08T19:12:43.256004Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 84 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000200
qdrant-1         | 2026-07-08T19:12:43.257340Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 82 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000144
qdrant-1         | 2026-07-08T19:12:43.257743Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/cloud/data.json HTTP/1.1" 404 0 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000182
qdrant-1         | 2026-07-08T19:12:43.320215Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 60 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000182
qdrant-1         | 2026-07-08T19:12:43.321352Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 59 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000128
qdrant-1         | 2026-07-08T19:12:43.330419Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections/Amazon-items-collection-03 HTTP/1.1" 200 434 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000482
qdrant-1         | 2026-07-08T19:12:43.331313Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections/Amazon-items-collection-03 HTTP/1.1" 200 435 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000200
qdrant-1         | 2026-07-08T19:15:43.760056Z  INFO actix_web::middleware::logger: 172.19.0.1 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 6444 "-" "python-client/1.16.2 python/3.12.3" 0.002328
qdrant-1         | 2026-07-08T19:17:21.773478Z  INFO actix_web::middleware::logger: 172.19.0.1 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 3158 "-" "python-client/1.16.2 python/3.12.3" 0.002571
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [293]
api-1            | 2026-07-08 19:19:14,861 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [357]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [357]
api-1            | 2026-07-08 19:20:05,350 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [421]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [421]
api-1            | 2026-07-08 19:20:08,018 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [485]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [485]
api-1            | 2026-07-08 19:20:12,723 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [549]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [549]
api-1            | 2026-07-08 19:20:37,213 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [613]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [613]
api-1            | 2026-07-08 19:20:44,124 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [677]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [677]
api-1            | 2026-07-08 19:21:14,829 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [741]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [741]
api-1            | 2026-07-08 19:21:19,052 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [805]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 19:25:58,870 - api.api.middleware - INFO - Request started: POST /rag (request_id: 02be46eb-54a4-498a-a7ad-fb40be5329ca)
api-1            | 2026-07-08 19:25:58,870 - api.api.middleware - INFO - Request completed: POST /rag (request_id: 02be46eb-54a4-498a-a7ad-fb40be5329ca)
api-1            | INFO:     172.19.0.2:56910 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 19:25:58,872 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: a1864575-0839-490c-b8ab-fe9f94e514c8)
api-1            | 2026-07-08 19:25:59,131 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | INFO:     172.19.0.2:56910 - "POST /rag/ HTTP/1.1" 500 Internal Server Error
api-1            | ERROR:    Exception in ASGI application
api-1            | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 410, in run_asgi
api-1            |     result = await app(  # type: ignore[func-returns-value]
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
api-1            |     return await self.app(scope, receive, send)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
api-1            |     await super().__call__(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
api-1            |     await self.app(scope, receive, _send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
api-1            |     with recv_stream, send_stream, collapse_excgroups():
api-1            |                                    ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
api-1            |     self.gen.throw(value)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
api-1            |     response = await self.dispatch_func(request, call_next)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/middleware.py", line 20, in dispatch
api-1            |     response = await call_next(request)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
api-1            |     raise app_exc from app_exc.__cause__ or app_exc.__context__
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
api-1            |     await self.app(scope, receive_or_disconnect, send_no_error)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
api-1            |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
api-1            |     await route.handle(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 115, in app
api-1            |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 101, in app
api-1            |     response = await f(request)
api-1            |                ^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 355, in app
api-1            |     raw_response = await run_endpoint_function(
api-1            |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 245, in run_endpoint_function
api-1            |     return await run_in_threadpool(dependant.call, **values)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
api-1            |     return await anyio.to_thread.run_sync(func)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 63, in run_sync
api-1            |     return await get_async_backend().run_sync_in_worker_thread(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2502, in run_sync_in_worker_thread
api-1            |     return await future
api-1            |            ^^^^^^^^^^^^



streamlit-app-1  | 2026-07-08 19:25:59.140 Uncaught app execution
streamlit-app-1  | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run


api-1            |     result = context.run(func, *args)
streamlit-app-1  |   File "/app/.venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 129, in exec_func_with_error_handling


api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^
streamlit-app-1  |     result = func()

api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 26, in rag
streamlit-app-1  |              ^^^^^^


streamlit-app-1  |   File "/app/.venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 672, in code_to_exec
api-1            |     answer = rag_pipeline(payload.query, qdrant_client)
streamlit-app-1  |     exec(code, module.__dict__)  # noqa: S102

streamlit-app-1  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
streamlit-app-1  |   File "/app/apps/chatbot_ui/src/chatbot_ui/app.py", line 56, in <module>




streamlit-app-1  |     answer = response_data["answer"]
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 159, in rag_pipeline
api-1            |     retrieved_context = retrieve_data(question, qdrant_client, top_k)
streamlit-app-1  |              ~~~~~~~~~~~~~^^^^^^^^^^
api-1            |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
streamlit-app-1  | KeyError: 'answer'

api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 50, in retrieve_data
api-1            |     results = qdrant_client.query_points(
api-1            |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_client.py", line 423, in query_points
api-1            |     return self._client.query_points(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_remote.py", line 523, in query_points
api-1            |     query_request = models.QueryRequest(
api-1            |                     ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/pydantic/main.py", line 250, in __init__
api-1            |     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
api-1            |                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            | pydantic_core._pydantic_core.ValidationError: 1 validation error for QueryRequest
api-1            | limit
api-1            |   Input should be a valid integer [type=int_type, input_value=<qdrant_client.qdrant_cli...bject at 0x7c7cd9b480b0>, input_type=QdrantClient]
api-1            |     For further information visit https://errors.pydantic.dev/2.12/v/int_type
api-1            | 2026-07-08 19:26:25,617 - api.api.middleware - INFO - Request started: GET /docs (request_id: 45347161-2d2e-45bd-b6df-c9bc62402078)
api-1            | 2026-07-08 19:26:25,617 - api.api.middleware - INFO - Request completed: GET /docs (request_id: 45347161-2d2e-45bd-b6df-c9bc62402078)
api-1            | INFO:     172.19.0.1:48492 - "GET /docs HTTP/1.1" 200 OK
api-1            | 2026-07-08 19:26:25,737 - api.api.middleware - INFO - Request started: GET /openapi.json (request_id: 2fee2491-7eb5-447f-b519-820f8f2790ae)
api-1            | 2026-07-08 19:26:25,744 - api.api.middleware - INFO - Request completed: GET /openapi.json (request_id: 2fee2491-7eb5-447f-b519-820f8f2790ae)
api-1            | INFO:     172.19.0.1:48492 - "GET /openapi.json HTTP/1.1" 200 OK
api-1            | 2026-07-08 19:27:16,034 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: 948205a0-fddd-46af-84d4-12b58911e857)
api-1            | 2026-07-08 19:27:16,225 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | INFO:     172.19.0.1:48498 - "POST /rag/ HTTP/1.1" 500 Internal Server Error
api-1            | ERROR:    Exception in ASGI application
api-1            | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 410, in run_asgi
api-1            |     result = await app(  # type: ignore[func-returns-value]
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
api-1            |     return await self.app(scope, receive, send)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
api-1            |     await super().__call__(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
api-1            |     await self.app(scope, receive, _send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 93, in __call__
api-1            |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 144, in simple_response
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
api-1            |     with recv_stream, send_stream, collapse_excgroups():
api-1            |                                    ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
api-1            |     self.gen.throw(value)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
api-1            |     response = await self.dispatch_func(request, call_next)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/middleware.py", line 20, in dispatch
api-1            |     response = await call_next(request)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
api-1            |     raise app_exc from app_exc.__cause__ or app_exc.__context__
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
api-1            |     await self.app(scope, receive_or_disconnect, send_no_error)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
api-1            |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
api-1            |     await route.handle(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 115, in app
api-1            |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 101, in app
api-1            |     response = await f(request)
api-1            |                ^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 355, in app
api-1            |     raw_response = await run_endpoint_function(
api-1            |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 245, in run_endpoint_function
api-1            |     return await run_in_threadpool(dependant.call, **values)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
api-1            |     return await anyio.to_thread.run_sync(func)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 63, in run_sync
api-1            |     return await get_async_backend().run_sync_in_worker_thread(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2502, in run_sync_in_worker_thread
api-1            |     return await future
api-1            |            ^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run
api-1            |     result = context.run(func, *args)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 26, in rag
api-1            |     answer = rag_pipeline(payload.query, qdrant_client)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 159, in rag_pipeline
api-1            |     retrieved_context = retrieve_data(question, qdrant_client, top_k)
api-1            |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 50, in retrieve_data
api-1            |     results = qdrant_client.query_points(
api-1            |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_client.py", line 423, in query_points
api-1            |     return self._client.query_points(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_remote.py", line 523, in query_points
api-1            |     query_request = models.QueryRequest(
api-1            |                     ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/pydantic/main.py", line 250, in __init__
api-1            |     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
api-1            |                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            | pydantic_core._pydantic_core.ValidationError: 1 validation error for QueryRequest
api-1            | limit
api-1            |   Input should be a valid integer [type=int_type, input_value=<qdrant_client.qdrant_cli...bject at 0x7c7cd9b480b0>, input_type=QdrantClient]
api-1            |     For further information visit https://errors.pydantic.dev/2.12/v/int_type


=================================================================================================

resolution



### 1. Root Cause Analysis

The logs indicate two cascading failures:

**A. FastAPI / Qdrant ValidationError (Root Cause)**
```
pydantic_core._pydantic_core.ValidationError: 1 validation error for QueryRequest
limit
  Input should be a valid integer [type=int_type, input_value=<qdrant_client.qdrant_cli...bject at 0x7c7cd9b480b0>, input_type=QdrantClient]
```
- **Why it occurred:** In `apps/api/src/api/api/endpoints.py`, the `rag` endpoint calls `rag_pipeline(payload.query, qdrant_client)`. However, the function signature in `apps/api/src/api/agents/retrieval_generation.py` is `def rag_pipeline(question, top_k=5)`. 
- By passing `qdrant_client` as the second argument, `top_k` becomes a `QdrantClient` object instead of an integer. 
- When `rag_pipeline` internally calls `retrieve_data(question, qdrant_client, top_k)`, it passes this `QdrantClient` object as the `k` parameter. Qdrant's `query_points` function expects an integer for the `limit` parameter, causing a Pydantic `ValidationError`.

**B. Streamlit KeyError (Symptom)**
```
KeyError: 'answer'
```
- **Why it occurred:** Because the FastAPI backend crashed with a 500 Internal Server Error (due to the Qdrant validation error above), it returned an error JSON payload (e.g., `{"detail": "Internal Server Error"}`).
- The Streamlit app in `apps/chatbot_ui/src/chatbot_ui/app.py` blindly assumes the API call was successful and attempts to access `response_data["answer"]`. Since the response only contained an error detail, the `'answer'` key did not exist, crashing the UI.

---

### 2. End-to-End Changes Required

To fix this issue completely, we need to correct the function call in FastAPI and handle errors gracefully in Streamlit.

#### Fix 1: Correct the FastAPI Endpoint
File: `apps/api/src/api/api/endpoints.py`

1. Remove the global `qdrant_client` initialization since `rag_pipeline` handles its own Qdrant connection.
2. Call `rag_pipeline` with only the `query`.
3. The `rag_pipeline` function returns a plain string, so we need to assign it directly to `answer` instead of trying to index it as a dictionary.

**Changes:**
```python
# Remove:
# from qdrant_client import QdrantClient
# qdrant_client = QdrantClient(url="http://qdrant:6333")

@rag_router.post("/")
def rag(
    request: Request,
    payload: RAGRequest
) -> RAGResponse:

    # 1. Only pass the query, let the pipeline use its default top_k=5
    answer_text = rag_pipeline(payload.query)

    # 2. Assign the returned string directly
    return RAGResponse(
        request_id=request.state.request_id,
        answer=answer_text
    )
```

#### Fix 2: Add Error Handling in Streamlit UI
File: `apps/chatbot_ui/src/chatbot_ui/app.py`

Update the chat UI to handle cases where the API returns an error, preventing the `KeyError` crash.

**Changes:**
```python
    with st.chat_message("assistant"):
        output = api_call("post", f"{config.API_URL}/rag", json={"query": prompt})
        is_success = output[0]
        response_data = output[1]
        
        # Check if the API call was successful before accessing the answer
        if is_success:
            answer = response_data.get("answer", "No answer provided.")
        else:
            answer = f"⚠️ API Error: {response_data.get('detail', response_data.get('message', 'Unknown error'))}"
            
        st.write(answer)
```


========================================================================================

FastAPI
 0.1.0 
OAS 3.1
/openapi.json
rag


POST
/rag/
Rag

Parameters
Cancel
Reset
No parameters

Request body

application/json
Edit Value
Schema
{
  "query": "give me the earphones rating above 4.5"
}
Execute
Clear
Responses
Curl

curl -X 'POST' \
  'http://localhost:8000/rag/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "give me the earphones rating above 4.5"
}'
Request URL
http://localhost:8000/rag/
Server response
Code	Details
200	
Response body
Download
{
  "request_id": "e3c36e88-d5bf-4cee-8005-22246bf076c3",
  "answer": "Based on the available products, there are no earphones with a rating above 4.5."
}
Response headers
 access-control-allow-credentials: true 
 access-control-allow-origin: http://localhost:8000 
 content-length: 145 
 content-type: application/json 
 date: Wed,08 Jul 2026 19:40:54 GMT 
 server: uvicorn 
 vary: Origin 
 x-request-id: e3c36e88-d5bf-4cee-8005-22246bf076c3 
Responses
Code	Description	Links
200	
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
  "request_id": "string",
  "answer": "string"
}
No links
422	
Validation Error

Media type

application/json
Example Value
Schema
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
No links

Schemas
HTTPValidationErrorExpand allobject
RAGRequestExpand allobject
RAGResponseExpand allobject
ValidationErrorExpand allobject





Hello! How can I assist you today?

get me the earphones of rating above 4.5

I'm sorry, but there are no earphones available with a rating above 4.5.



### 3. Verification & Final Checks

The cURL and Streamlit logs pasted above confirm that the  fix successfully resolved the 500 Internal Server Error. The API is now correctly returning  with the string answer, and Streamlit correctly processes and displays it.

**Is there anything else to check?**
- ✅ **API :** Working as expected.
- ✅ **Streamlit :** Working as expected, and now includes error handling.
- ✅ **:** Checked and updated! I have removed the outdated references to  being passed to  in the master documentation so that the manual correctly matches the actual working code.
- ✅ **:** Checked and updated! I have removed the  argument from the LangSmith evaluation script so that it doesn't crash if you run the evaluation suite later.

The entire platform and its documentation are completely synced and end-to-end operational!

### 3. Verification & Final Checks

The cURL and Streamlit logs pasted above confirm that the `rag_pipeline` fix successfully resolved the 500 Internal Server Error. The API is now correctly returning `200 OK` with the string answer, and Streamlit correctly processes and displays it.

**Is there anything else to check?**
- ✅ **API `endpoints.py`:** Working as expected.
- ✅ **Streamlit `app.py`:** Working as expected, and now includes error handling.
- ✅ **`explination_detail.md`:** Checked and updated! I have removed the outdated references to `qdrant_client` being passed to `rag_pipeline` in the master documentation so that the manual correctly matches the actual working code.
- ✅ **`eval_retriever.py`:** Checked and updated! I have removed the `qdrant_client` argument from the LangSmith evaluation script so that it doesn't crash if you run the evaluation suite later.

The entire platform and its documentation are completely synced and end-to-end operational!

==============================================================================================

  28 | >>>     uv sync --frozen --no-dev --package api

  29 |     

--------------------

target api: failed to solve: process "/bin/sh -c uv sync --frozen --no-dev --package api" did not complete successfully: exit code: 1

make: *** [Makefile:3: run-docker-compose] Error 1
(cohort-repo) rayudu@tungsten:~/otherwork_assignment_all_jobs/Todo/genai_rag_agent_platform$ make run-docker-compose
uv sync
Resolved 182 packages in 1ms
Checked 170 packages in 0.90ms
docker compose up --build
[+] Building 212.6s (26/26) FINISHED                                                                                                                     
 => [internal] load local bake definitions                                                                                                          0.0s
 => => reading from stdin 1.21kB                                                                                                                    0.0s
 => [api internal] load build definition from Dockerfile                                                                                            0.0s
 => => transferring dockerfile: 1.16kB                                                                                                              0.0s
 => [streamlit-app internal] load build definition from Dockerfile                                                                                  0.1s
 => => transferring dockerfile: 1.36kB                                                                                                              0.0s
 => [api internal] load metadata for ghcr.io/astral-sh/uv:python3.12-bookworm-slim                                                                  0.4s
 => [api internal] load .dockerignore                                                                                                               0.0s
 => => transferring context: 93B                                                                                                                    0.0s
 => [api internal] load build context                                                                                                               0.1s
 => => transferring context: 20.54kB                                                                                                                0.0s
 => [streamlit-app stage-0 1/8] FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147  0.0s
 => => resolve ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa78e58                0.0s
 => [streamlit-app internal] load build context                                                                                                     0.0s
 => => transferring context: 4.98kB                                                                                                                 0.0s
 => CACHED [streamlit-app stage-0 2/8] RUN addgroup --system app &&     adduser --system --ingroup app app &&     mkdir -p /home/app/.streamlit/da  0.0s
 => CACHED [streamlit-app stage-0 3/8] WORKDIR /app                                                                                                 0.0s
 => CACHED [streamlit-app stage-0 4/8] COPY pyproject.toml uv.lock ./                                                                               0.0s
 => CACHED [api stage-0 2/8] RUN addgroup --system app &&     adduser --system --ingroup app app &&     mkdir -p /home/app /app                     0.0s
 => CACHED [api stage-0 3/8] WORKDIR /app                                                                                                           0.0s
 => CACHED [api stage-0 4/8] COPY pyproject.toml uv.lock ./                                                                                         0.0s
 => [streamlit-app stage-0 5/8] COPY apps/chatbot_ui ./apps/chatbot_ui                                                                              0.2s
 => [api stage-0 5/8] COPY apps/api ./apps/api                                                                                                      0.2s
 => [api stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package api                                     3.6s
 => [streamlit-app stage-0 6/8] RUN --mount=type=cache,target=/root/.cache/uv     uv sync --frozen --no-dev --package chatbot_ui                    3.6s
 => [api stage-0 7/8] RUN chown -R app:app /app /home/app                                                                                         145.6s
 => [streamlit-app stage-0 7/8] RUN chown -R app:app /app /home/app                                                                               180.5s
 => [api stage-0 8/8] WORKDIR /app/apps/api/src                                                                                                     0.3s 
 => [api] exporting to image                                                                                                                       11.8s 
 => => exporting layers                                                                                                                             8.5s 
 => => exporting manifest sha256:388acc2f7cb03abac7cf86ee99e254b3af939c2aaae96f6e2181eeb53d8f53e9                                                   0.1s 
 => => exporting config sha256:d0ebadfbfbe91b90aa3b684033eca39f4bfca0153b1de669ca518e35e6c76daf                                                     0.1s 
 => => exporting attestation manifest sha256:97bd7ff15425703c627e35c7c87a8bc813f635263b25393d24f49e54fdf8a61a                                       0.1s 
 => => exporting manifest list sha256:3fe61207e9ade75d59261ff8642f3f48019c45aefdc5ff47bae3a012027828e1                                              0.1s 
 => => naming to docker.io/library/genai_rag_agent_platform-api:latest                                                                              0.0s
 => => unpacking to docker.io/library/genai_rag_agent_platform-api:latest                                                                           2.8s
 => [api] resolving provenance for metadata file                                                                                                    0.0s
 => [streamlit-app stage-0 8/8] WORKDIR /app/apps/chatbot_ui/src                                                                                    0.2s
 => [streamlit-app] exporting to image                                                                                                             27.1s
 => => exporting layers                                                                                                                            21.4s
 => => exporting manifest sha256:379341d9fd13d277d39cfd29c0b623b29639a97e49508c4a3472dadc97eb04a2                                                   0.0s
 => => exporting config sha256:ff12300de927580e61ed4e9591e410bdf98a2d5a1ed06a5fb7f0b9f8aeb6778c                                                     0.0s
 => => exporting attestation manifest sha256:7cb982d60518788ca7323ce3d3502b438351ce5d94b579802c464e100390ccd3                                       0.1s
 => => exporting manifest list sha256:76de7f01e7424a575b4677fb92e8fe994ecb005a01566ef58acd4154417c92d4                                              0.0s
 => => naming to docker.io/library/genai_rag_agent_platform-streamlit-app:latest                                                                    0.0s
 => => unpacking to docker.io/library/genai_rag_agent_platform-streamlit-app:latest                                                                 5.5s
 => [streamlit-app] resolving provenance for metadata file                                                                                          0.0s
[+] up 6/6
 ✔ Image genai_rag_agent_platform-streamlit-app       Built                                                                                        212.7s
 ✔ Image genai_rag_agent_platform-api                 Built                                                                                        212.7s
 ✔ Network genai_rag_agent_platform_default           Created                                                                                        0.0s
 ✔ Container genai_rag_agent_platform-streamlit-app-1 Created                                                                                        1.8s
 ✔ Container genai_rag_agent_platform-qdrant-1        Created                                                                                        1.8s
 ✔ Container genai_rag_agent_platform-api-1           Created                                                                                        1.8s
Attaching to api-1, qdrant-1, streamlit-app-1
qdrant-1  |            _                 _    
qdrant-1  |   __ _  __| |_ __ __ _ _ __ | |_  
qdrant-1  |  / _` |/ _` | '__/ _` | '_ \| __| 
qdrant-1  | | (_| | (_| | | | (_| | | | | |_  
qdrant-1  |  \__, |\__,_|_|  \__,_|_| |_|\__| 
qdrant-1  |     |_|                           
qdrant-1  | 
qdrant-1  | Version: 1.18.2, build: 44ad62f8
qdrant-1  | Access web UI at http://localhost:6333/dashboard
qdrant-1  | Agentic Skills: https://skills.qdrant.tech/
qdrant-1  | 
qdrant-1  | 2026-07-08T19:05:01.660408Z  INFO storage::content_manager::consensus::persistent: Initializing new raft state at ./storage/raft_state.json
qdrant-1  | 2026-07-08T19:05:01.720669Z  INFO qdrant: Distributed mode disabled
qdrant-1  | 2026-07-08T19:05:01.720694Z  INFO qdrant: Telemetry reporting enabled, id: ab74bff0-c445-4d2a-bcd1-7b591610757d
qdrant-1  | 2026-07-08T19:05:01.729612Z  INFO qdrant::actix: REST transport settings: keep_alive=5s, client_request_timeout=5s, client_disconnect_timeout=5s
qdrant-1  | 2026-07-08T19:05:01.729630Z  INFO qdrant::actix: TLS disabled for REST API
qdrant-1  | 2026-07-08T19:05:01.729672Z  INFO qdrant::actix: Qdrant HTTP listening on 6333
qdrant-1  | 2026-07-08T19:05:01.729675Z  INFO actix_server::builder: starting 63 workers
qdrant-1  | 2026-07-08T19:05:01.729678Z  INFO actix_server::server: Actix runtime found; starting in Actix runtime
qdrant-1  | 2026-07-08T19:05:01.729681Z  INFO actix_server::server: starting service: "actix-web-service-0.0.0.0:6333", workers: 63, listening on: 0.0.0.0:6333
qdrant-1  | 2026-07-08T19:05:01.730178Z  INFO qdrant::tonic: Qdrant gRPC listening on 6334
qdrant-1  | 2026-07-08T19:05:01.730193Z  INFO qdrant::tonic: TLS disabled for gRPC API
streamlit-app-1  |    Building chatbot-ui @ file:///app/apps/chatbot_ui
api-1            |    Building api @ file:///app/apps/api
streamlit-app-1  |       Built chatbot-ui @ file:///app/apps/chatbot_ui
streamlit-app-1  | Uninstalled 1 package in 24ms
streamlit-app-1  | Installed 1 package in 0.62ms
streamlit-app-1  | Bytecode compiled 3279 files in 144ms
api-1            |       Built api @ file:///app/apps/api
api-1            | Uninstalled 1 package in 23ms
api-1            | Installed 1 package in 0.82ms
streamlit-app-1  | 
streamlit-app-1  | Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
streamlit-app-1  | 
streamlit-app-1  | 
streamlit-app-1  |   You can now view your Streamlit app in your browser.
streamlit-app-1  | 
streamlit-app-1  |   URL: http://0.0.0.0:8501
streamlit-app-1  | 
api-1            | Bytecode compiled 3032 files in 237ms
api-1            | INFO:     Will watch for changes in these directories: ['/app/apps/api/src']
api-1            | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
api-1            | INFO:     Started reloader process [291] using StatReload
api-1            | 2026-07-08 19:05:06,015 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [293]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
qdrant-1         | 2026-07-08T19:06:20.702772Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard HTTP/1.1" 200 925 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000748
qdrant-1         | 2026-07-08T19:06:20.726847Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/manifest.json HTTP/1.1" 200 248 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000951
qdrant-1         | 2026-07-08T19:06:20.728573Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/index-BG9q9yEd.css HTTP/1.1" 200 24126 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.002544
qdrant-1         | 2026-07-08T19:06:20.787559Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/index-C3k9zy-X.js HTTP/1.1" 200 1452548 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.061676
qdrant-1         | 2026-07-08T19:06:20.971126Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/openapi.json HTTP/1.1" 200 50091 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.003302
qdrant-1         | 2026-07-08T19:06:21.063325Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 62 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000169
qdrant-1         | 2026-07-08T19:06:21.064642Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/cloud/data.json HTTP/1.1" 404 0 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000059
qdrant-1         | 2026-07-08T19:06:21.067573Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/logo-red-black.svg HTTP/1.1" 200 2781 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000908
qdrant-1         | 2026-07-08T19:06:21.081391Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/fonts/Mona_Sans/MonaSans-VariableFont_wdth,wght.ttf HTTP/1.1" 200 209961 "http://localhost:6333/dashboard/assets/index-BG9q9yEd.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.005786
qdrant-1         | 2026-07-08T19:06:21.091958Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/favicon.ico HTTP/1.1" 200 15086 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000333
qdrant-1         | 2026-07-08T19:06:21.092127Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/logo192.png HTTP/1.1" 200 6177 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000192
qdrant-1         | 2026-07-08T19:06:21.115589Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/assets/console.svg HTTP/1.1" 200 10386 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.001180
qdrant-1         | 2026-07-08T19:06:23.376457Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 62 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000176
qdrant-1         | 2026-07-08T19:06:23.377434Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 63 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000119
qdrant-1         | 2026-07-08T19:06:23.385927Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 60 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.004464
qdrant-1         | 2026-07-08T19:06:23.387157Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 60 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000103
qdrant-1         | 2026-07-08T19:11:29.339307Z  INFO storage::content_manager::toc::collection_meta_ops: Creating collection Amazon-items-collection-03
qdrant-1         | 2026-07-08T19:11:29.632488Z  INFO actix_web::middleware::logger: 172.19.0.1 "PUT /collections/Amazon-items-collection-03 HTTP/1.1" 200 57 "-" "python-client/1.16.2 python/3.12.3" 0.298509
qdrant-1         | 2026-07-08T19:12:22.103884Z  INFO actix_web::middleware::logger: 172.19.0.1 "PUT /collections/Amazon-items-collection-03/points?wait=true HTTP/1.1" 200 84 "-" "python-client/1.16.2 python/3.12.3" 0.025708
qdrant-1         | 2026-07-08T19:12:29.973619Z  INFO actix_web::middleware::logger: 172.19.0.1 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 7268 "-" "python-client/1.16.2 python/3.12.3" 0.002699
qdrant-1         | 2026-07-08T19:12:43.256004Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 84 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000200
qdrant-1         | 2026-07-08T19:12:43.257340Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections HTTP/1.1" 200 82 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000144
qdrant-1         | 2026-07-08T19:12:43.257743Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /dashboard/cloud/data.json HTTP/1.1" 404 0 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000182
qdrant-1         | 2026-07-08T19:12:43.320215Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 60 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000182
qdrant-1         | 2026-07-08T19:12:43.321352Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /aliases HTTP/1.1" 200 59 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000128
qdrant-1         | 2026-07-08T19:12:43.330419Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections/Amazon-items-collection-03 HTTP/1.1" 200 434 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000482
qdrant-1         | 2026-07-08T19:12:43.331313Z  INFO actix_web::middleware::logger: 172.19.0.1 "GET /collections/Amazon-items-collection-03 HTTP/1.1" 200 435 "http://localhost:6333/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36" 0.000200
qdrant-1         | 2026-07-08T19:15:43.760056Z  INFO actix_web::middleware::logger: 172.19.0.1 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 6444 "-" "python-client/1.16.2 python/3.12.3" 0.002328
qdrant-1         | 2026-07-08T19:17:21.773478Z  INFO actix_web::middleware::logger: 172.19.0.1 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 3158 "-" "python-client/1.16.2 python/3.12.3" 0.002571
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [293]
api-1            | 2026-07-08 19:19:14,861 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [357]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [357]
api-1            | 2026-07-08 19:20:05,350 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [421]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [421]
api-1            | 2026-07-08 19:20:08,018 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [485]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [485]
api-1            | 2026-07-08 19:20:12,723 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [549]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [549]
api-1            | 2026-07-08 19:20:37,213 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [613]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [613]
api-1            | 2026-07-08 19:20:44,124 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [677]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [677]
api-1            | 2026-07-08 19:21:14,829 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [741]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [741]
api-1            | 2026-07-08 19:21:19,052 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [805]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 19:25:58,870 - api.api.middleware - INFO - Request started: POST /rag (request_id: 02be46eb-54a4-498a-a7ad-fb40be5329ca)
api-1            | 2026-07-08 19:25:58,870 - api.api.middleware - INFO - Request completed: POST /rag (request_id: 02be46eb-54a4-498a-a7ad-fb40be5329ca)
api-1            | INFO:     172.19.0.2:56910 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 19:25:58,872 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: a1864575-0839-490c-b8ab-fe9f94e514c8)
api-1            | 2026-07-08 19:25:59,131 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | INFO:     172.19.0.2:56910 - "POST /rag/ HTTP/1.1" 500 Internal Server Error
api-1            | ERROR:    Exception in ASGI application
api-1            | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 410, in run_asgi
api-1            |     result = await app(  # type: ignore[func-returns-value]
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
api-1            |     return await self.app(scope, receive, send)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
api-1            |     await super().__call__(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
api-1            |     await self.app(scope, receive, _send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
api-1            |     with recv_stream, send_stream, collapse_excgroups():
api-1            |                                    ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
api-1            |     self.gen.throw(value)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
api-1            |     response = await self.dispatch_func(request, call_next)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/middleware.py", line 20, in dispatch
api-1            |     response = await call_next(request)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
api-1            |     raise app_exc from app_exc.__cause__ or app_exc.__context__
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
api-1            |     await self.app(scope, receive_or_disconnect, send_no_error)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
api-1            |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
api-1            |     await route.handle(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 115, in app
api-1            |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 101, in app
api-1            |     response = await f(request)
api-1            |                ^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 355, in app
api-1            |     raw_response = await run_endpoint_function(
api-1            |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 245, in run_endpoint_function
api-1            |     return await run_in_threadpool(dependant.call, **values)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
api-1            |     return await anyio.to_thread.run_sync(func)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 63, in run_sync
api-1            |     return await get_async_backend().run_sync_in_worker_thread(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2502, in run_sync_in_worker_thread
api-1            |     return await future
api-1            |            ^^^^^^^^^^^^



streamlit-app-1  | 2026-07-08 19:25:59.140 Uncaught app execution
streamlit-app-1  | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run


api-1            |     result = context.run(func, *args)
streamlit-app-1  |   File "/app/.venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 129, in exec_func_with_error_handling


api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^
streamlit-app-1  |     result = func()

api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 26, in rag
streamlit-app-1  |              ^^^^^^


streamlit-app-1  |   File "/app/.venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 672, in code_to_exec
api-1            |     answer = rag_pipeline(payload.query, qdrant_client)
streamlit-app-1  |     exec(code, module.__dict__)  # noqa: S102

streamlit-app-1  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
streamlit-app-1  |   File "/app/apps/chatbot_ui/src/chatbot_ui/app.py", line 56, in <module>




streamlit-app-1  |     answer = response_data["answer"]
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 159, in rag_pipeline
api-1            |     retrieved_context = retrieve_data(question, qdrant_client, top_k)
streamlit-app-1  |              ~~~~~~~~~~~~~^^^^^^^^^^
api-1            |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
streamlit-app-1  | KeyError: 'answer'

api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 50, in retrieve_data
api-1            |     results = qdrant_client.query_points(
api-1            |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_client.py", line 423, in query_points
api-1            |     return self._client.query_points(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_remote.py", line 523, in query_points
api-1            |     query_request = models.QueryRequest(
api-1            |                     ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/pydantic/main.py", line 250, in __init__
api-1            |     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
api-1            |                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            | pydantic_core._pydantic_core.ValidationError: 1 validation error for QueryRequest
api-1            | limit
api-1            |   Input should be a valid integer [type=int_type, input_value=<qdrant_client.qdrant_cli...bject at 0x7c7cd9b480b0>, input_type=QdrantClient]
api-1            |     For further information visit https://errors.pydantic.dev/2.12/v/int_type
api-1            | 2026-07-08 19:26:25,617 - api.api.middleware - INFO - Request started: GET /docs (request_id: 45347161-2d2e-45bd-b6df-c9bc62402078)
api-1            | 2026-07-08 19:26:25,617 - api.api.middleware - INFO - Request completed: GET /docs (request_id: 45347161-2d2e-45bd-b6df-c9bc62402078)
api-1            | INFO:     172.19.0.1:48492 - "GET /docs HTTP/1.1" 200 OK
api-1            | 2026-07-08 19:26:25,737 - api.api.middleware - INFO - Request started: GET /openapi.json (request_id: 2fee2491-7eb5-447f-b519-820f8f2790ae)
api-1            | 2026-07-08 19:26:25,744 - api.api.middleware - INFO - Request completed: GET /openapi.json (request_id: 2fee2491-7eb5-447f-b519-820f8f2790ae)
api-1            | INFO:     172.19.0.1:48492 - "GET /openapi.json HTTP/1.1" 200 OK
api-1            | 2026-07-08 19:27:16,034 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: 948205a0-fddd-46af-84d4-12b58911e857)
api-1            | 2026-07-08 19:27:16,225 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | INFO:     172.19.0.1:48498 - "POST /rag/ HTTP/1.1" 500 Internal Server Error
api-1            | ERROR:    Exception in ASGI application
api-1            | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 410, in run_asgi
api-1            |     result = await app(  # type: ignore[func-returns-value]
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
api-1            |     return await self.app(scope, receive, send)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
api-1            |     await super().__call__(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
api-1            |     await self.app(scope, receive, _send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 93, in __call__
api-1            |     await self.simple_response(scope, receive, send, request_headers=headers)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 144, in simple_response
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
api-1            |     with recv_stream, send_stream, collapse_excgroups():
api-1            |                                    ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
api-1            |     self.gen.throw(value)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
api-1            |     response = await self.dispatch_func(request, call_next)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/middleware.py", line 20, in dispatch
api-1            |     response = await call_next(request)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
api-1            |     raise app_exc from app_exc.__cause__ or app_exc.__context__
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
api-1            |     await self.app(scope, receive_or_disconnect, send_no_error)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
api-1            |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
api-1            |     await route.handle(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 115, in app
api-1            |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 101, in app
api-1            |     response = await f(request)
api-1            |                ^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 355, in app
api-1            |     raw_response = await run_endpoint_function(
api-1            |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 245, in run_endpoint_function
api-1            |     return await run_in_threadpool(dependant.call, **values)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
api-1            |     return await anyio.to_thread.run_sync(func)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 63, in run_sync
api-1            |     return await get_async_backend().run_sync_in_worker_thread(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2502, in run_sync_in_worker_thread
api-1            |     return await future
api-1            |            ^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run
api-1            |     result = context.run(func, *args)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 26, in rag
api-1            |     answer = rag_pipeline(payload.query, qdrant_client)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 159, in rag_pipeline
api-1            |     retrieved_context = retrieve_data(question, qdrant_client, top_k)
api-1            |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 50, in retrieve_data
api-1            |     results = qdrant_client.query_points(
api-1            |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_client.py", line 423, in query_points
api-1            |     return self._client.query_points(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/qdrant_client/qdrant_remote.py", line 523, in query_points
api-1            |     query_request = models.QueryRequest(
api-1            |                     ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/pydantic/main.py", line 250, in __init__
api-1            |     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
api-1            |                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            | pydantic_core._pydantic_core.ValidationError: 1 validation error for QueryRequest
api-1            | limit
api-1            |   Input should be a valid integer [type=int_type, input_value=<qdrant_client.qdrant_cli...bject at 0x7c7cd9b480b0>, input_type=QdrantClient]
api-1            |     For further information visit https://errors.pydantic.dev/2.12/v/int_type
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [805]
api-1            | Process SpawnProcess-10:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 5, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 172
api-1            |     Resolved 182 packages in 1ms
api-1            |                              ^
api-1            | SyntaxError: invalid decimal literal
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | 2026-07-08 19:29:07,060 - httpx - INFO - HTTP Request: GET http://qdrant:6333 "HTTP/1.1 200 OK"
api-1            | /app/apps/api/src/api/api/endpoints.py:16: UserWarning: Qdrant client version 1.16.2 is incompatible with server version 1.18.2. Major versions should match and minor version difference must not exceed 1. Set check_compatibility=False to skip version check.
api-1            |   qdrant_client = QdrantClient(url="http://qdrant:6333")
api-1            | INFO:     Started server process [934]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/api/endpoints.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [934]
api-1            | INFO:     Started server process [998]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 19:40:17,444 - api.api.middleware - INFO - Request started: POST /rag (request_id: da95a6fb-89fa-4181-adf7-00f6595f8b30)
api-1            | 2026-07-08 19:40:17,444 - api.api.middleware - INFO - Request completed: POST /rag (request_id: da95a6fb-89fa-4181-adf7-00f6595f8b30)
api-1            | INFO:     172.19.0.2:39920 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 19:40:17,446 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: 88942c21-23d2-4ace-a38c-be98537a53fe)
api-1            | 2026-07-08 19:40:17,646 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
qdrant-1         | 2026-07-08T19:40:17.653704Z  INFO actix_web::middleware::logger: 172.19.0.3 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 3164 "-" "python-client/1.16.2 python/3.12.12" 0.002079
api-1            | 2026-07-08 19:40:17,653 - httpx - INFO - HTTP Request: POST http://qdrant:6333/collections/Amazon-items-collection-03/points/query "HTTP/1.1 200 OK"
api-1            | 2026-07-08 19:40:17,654 - google_genai.models - INFO - AFC is enabled with max remote calls: 10.
api-1            | 2026-07-08 19:40:18,860 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
api-1            | 2026-07-08 19:40:18,862 - api.api.middleware - INFO - Request completed: POST /rag/ (request_id: 88942c21-23d2-4ace-a38c-be98537a53fe)
api-1            | INFO:     172.19.0.2:39920 - "POST /rag/ HTTP/1.1" 200 OK
api-1            | 2026-07-08 19:40:54,754 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: e3c36e88-d5bf-4cee-8005-22246bf076c3)
api-1            | 2026-07-08 19:40:54,960 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | 2026-07-08 19:40:54,968 - httpx - INFO - HTTP Request: POST http://qdrant:6333/collections/Amazon-items-collection-03/points/query "HTTP/1.1 200 OK"
qdrant-1         | 2026-07-08T19:40:54.968254Z  INFO actix_web::middleware::logger: 172.19.0.3 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 2660 "-" "python-client/1.16.2 python/3.12.12" 0.002376
api-1            | 2026-07-08 19:40:54,968 - google_genai.models - INFO - AFC is enabled with max remote calls: 10.
api-1            | 2026-07-08 19:40:56,533 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
api-1            | 2026-07-08 19:40:56,535 - api.api.middleware - INFO - Request completed: POST /rag/ (request_id: e3c36e88-d5bf-4cee-8005-22246bf076c3)
api-1            | INFO:     172.19.0.1:52946 - "POST /rag/ HTTP/1.1" 200 OK
api-1            | 2026-07-08 19:49:08,654 - api.api.middleware - INFO - Request started: POST /rag (request_id: 07488384-b652-4eb7-a00b-1b3187086549)
api-1            | 2026-07-08 19:49:08,654 - api.api.middleware - INFO - Request completed: POST /rag (request_id: 07488384-b652-4eb7-a00b-1b3187086549)
api-1            | INFO:     172.19.0.2:58766 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 19:49:08,655 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: db70169f-93ef-4f7f-8d63-08b10cfeb5a9)
api-1            | 2026-07-08 19:49:08,864 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | 2026-07-08 19:49:08,870 - httpx - INFO - HTTP Request: POST http://qdrant:6333/collections/Amazon-items-collection-03/points/query "HTTP/1.1 200 OK"
qdrant-1         | 2026-07-08T19:49:08.870995Z  INFO actix_web::middleware::logger: 172.19.0.3 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 4262 "-" "python-client/1.16.2 python/3.12.12" 0.002187
api-1            | 2026-07-08 19:49:08,871 - google_genai.models - INFO - AFC is enabled with max remote calls: 10.
api-1            | 2026-07-08 19:49:11,487 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
api-1            | 2026-07-08 19:49:11,489 - api.api.middleware - INFO - Request completed: POST /rag/ (request_id: db70169f-93ef-4f7f-8d63-08b10cfeb5a9)
api-1            | INFO:     172.19.0.2:58766 - "POST /rag/ HTTP/1.1" 200 OK
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [998]
api-1            | INFO:     Started server process [1063]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1063]
api-1            | Process SpawnProcess-14:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 22
api-1            |     gemini_client = genai.Client(api_key=GOOGLE_API_KEY)
api-1            |     ^^^^^^^^^^^^^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-15:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 23
api-1            |     gemini_client = genai.Client(api_key=GOOGLE_API_KEY)
api-1            |     ^^^^^^^^^^^^^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-16:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 22
api-1            |     gemini_client = genai.Client(api_key=GOOGLE_API_KEY)
api-1            |     ^^^^^^^^^^^^^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [1130]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1130]
api-1            | INFO:     Started server process [1194]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1194]
api-1            | INFO:     Started server process [1258]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1258]
api-1            | INFO:     Started server process [1322]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1322]
api-1            | INFO:     Started server process [1386]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1386]
api-1            | INFO:     Started server process [1450]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 20:29:12,685 - api.api.middleware - INFO - Request started: POST /rag (request_id: d3e11267-1bc6-4c1e-ab2d-51428b388c7f)
api-1            | 2026-07-08 20:29:12,685 - api.api.middleware - INFO - Request completed: POST /rag (request_id: d3e11267-1bc6-4c1e-ab2d-51428b388c7f)
api-1            | INFO:     172.19.0.2:38152 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 20:29:12,686 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: fc31bed8-a85c-4ff2-baf4-ab7d1a41ae00)
api-1            | 2026-07-08 20:29:12,867 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | 2026-07-08 20:29:12,875 - httpx - INFO - HTTP Request: POST http://qdrant:6333/collections/Amazon-items-collection-03/points/query "HTTP/1.1 200 OK"
qdrant-1         | 2026-07-08T20:29:12.875694Z  INFO actix_web::middleware::logger: 172.19.0.3 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 2956 "-" "python-client/1.16.2 python/3.12.12" 0.002033
api-1            | 2026-07-08 20:29:12,877 - google_genai.models - INFO - AFC is enabled with max remote calls: 10.
api-1            | 2026-07-08 20:29:14,038 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
api-1            | 2026-07-08 20:29:14,041 - api.api.middleware - INFO - Request completed: POST /rag/ (request_id: fc31bed8-a85c-4ff2-baf4-ab7d1a41ae00)
api-1            | INFO:     172.19.0.2:38152 - "POST /rag/ HTTP/1.1" 200 OK
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1450]
api-1            | Process SpawnProcess-23:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 190
api-1            |     @
api-1            |      ^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [1649]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 20:41:25,452 - api.api.middleware - INFO - Request started: POST /rag (request_id: 4481550a-a79e-4a9f-8d49-1aff750a1ab6)
api-1            | 2026-07-08 20:41:25,452 - api.api.middleware - INFO - Request completed: POST /rag (request_id: 4481550a-a79e-4a9f-8d49-1aff750a1ab6)
api-1            | INFO:     172.19.0.2:57748 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 20:41:25,454 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: f38e609a-6850-4604-8a6d-d1cb10d1d2fb)
api-1            | 2026-07-08 20:41:25,682 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | 2026-07-08 20:41:25,691 - httpx - INFO - HTTP Request: POST http://qdrant:6333/collections/Amazon-items-collection-03/points/query "HTTP/1.1 200 OK"
qdrant-1         | 2026-07-08T20:41:25.691420Z  INFO actix_web::middleware::logger: 172.19.0.3 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 4119 "-" "python-client/1.16.2 python/3.12.12" 0.002342
api-1            | 2026-07-08 20:41:25,693 - google_genai.models - INFO - AFC is enabled with max remote calls: 10.
api-1            | 2026-07-08 20:41:29,318 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
api-1            | 2026-07-08 20:41:29,321 - api.api.middleware - INFO - Request completed: POST /rag/ (request_id: f38e609a-6850-4604-8a6d-d1cb10d1d2fb)
api-1            | INFO:     172.19.0.2:57748 - "POST /rag/ HTTP/1.1" 200 OK
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1649]
api-1            | Process SpawnProcess-25:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 25
api-1            |     @traceable)
api-1            |               ^
api-1            | SyntaxError: unmatched ')'
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-26:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 25
api-1            |     @traceable())
api-1            |                 ^
api-1            | SyntaxError: unmatched ')'
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [1849]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1849]
api-1            | Process SpawnProcess-28:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 25, in <module>
api-1            |     @traceable(name)
api-1            |                ^^^^
api-1            | NameError: name 'name' is not defined
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [1977]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [1977]
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [2041]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [2105]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [2169]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | Process SpawnProcess-33:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 25
api-1            |     @traceable(name="embed_query", 
api-1            |               ^
api-1            | SyntaxError: '(' was never closed
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-34:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 25
api-1            |     @traceable(name="embed_query"), 
api-1            |                                   ^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-35:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 26
api-1            |     , 
api-1            |     ^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-36:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 26
api-1            |     , run_type="embedding", metadata={"ls_provider": "google", "ls_model_name": "gemini-embedding-001"})
api-1            |                                                                                                        ^
api-1            | SyntaxError: unmatched ')'
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [2237]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2237]
api-1            | INFO:     Started server process [2301]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2301]
api-1            | INFO:     Started server process [2365]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2365]
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-40:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 80, in <module>
api-1            |     @traceable
api-1            | NameError: name 'traceableretrieve_data' is not defined
api-1            | INFO:     Started server process [2493]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2493]
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-42:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 80, in <module>
api-1            |     @traceable
api-1            | NameError: name 'traceableretrieve_data' is not defined
api-1            | INFO:     Started server process [2621]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2621]
api-1            | INFO:     Started server process [2685]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2685]
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [2749]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | INFO:     Started server process [2813]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2813]
api-1            | INFO:     Started server process [2877]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2877]
api-1            | Process SpawnProcess-48:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 91
api-1            |     @traceable(name="build_prompt",r)
api-1            |                                     ^
api-1            | SyntaxError: positional argument follows keyword argument
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [2942]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [2942]
api-1            | INFO:     Started server process [3006]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3006]
api-1            | INFO:     Started server process [3070]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3070]
api-1            | INFO:     Started server process [3134]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3134]
api-1            | INFO:     Started server process [3198]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 20:55:37,325 - api.api.middleware - INFO - Request started: POST /rag (request_id: 6adb7913-e587-4da6-aef2-9d9f308e68c7)
api-1            | 2026-07-08 20:55:37,325 - api.api.middleware - INFO - Request completed: POST /rag (request_id: 6adb7913-e587-4da6-aef2-9d9f308e68c7)
api-1            | INFO:     172.19.0.2:55908 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 20:55:37,327 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: 1930d254-cbd3-414d-8855-fcb85391479a)
api-1            | 2026-07-08 20:55:37,517 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | 2026-07-08 20:55:37,526 - httpx - INFO - HTTP Request: POST http://qdrant:6333/collections/Amazon-items-collection-03/points/query "HTTP/1.1 200 OK"
qdrant-1         | 2026-07-08T20:55:37.526510Z  INFO actix_web::middleware::logger: 172.19.0.3 "POST /collections/Amazon-items-collection-03/points/query HTTP/1.1" 200 2667 "-" "python-client/1.16.2 python/3.12.12" 0.002139
api-1            | 2026-07-08 20:55:37,528 - google_genai.models - INFO - AFC is enabled with max remote calls: 10.
api-1            | 2026-07-08 20:55:39,859 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
api-1            | 2026-07-08 20:55:39,862 - api.api.middleware - INFO - Request completed: POST /rag/ (request_id: 1930d254-cbd3-414d-8855-fcb85391479a)
api-1            | INFO:     172.19.0.2:55908 - "POST /rag/ HTTP/1.1" 200 OK
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3198]
api-1            | Process SpawnProcess-54:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 25
api-1            |     @traceable(name="embed_query",, run_type="embedding", metadata={"ls_provider": "google", "ls_model_name": "gemini-embedding-001"})
api-1            |                                   ^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [3397]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3397]
api-1            | Process SpawnProcess-56:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 41
api-1            |     current_run = get_current_run_tree()
api-1            | IndentationError: unexpected indent
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [3462]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3462]
api-1            | INFO:     Started server process [3526]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3526]
api-1            | INFO:     Started server process [3590]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3590]
api-1            | INFO:     Started server process [3654]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3654]
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [3718]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | INFO:     Started server process [3782]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3782]
api-1            | INFO:     Started server process [3846]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3846]
api-1            | INFO:     Started server process [3910]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3910]
api-1            | Process SpawnProcess-65:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 196
api-1            |     def rag_pipeline(question, top_k=5):
api-1            |                                         ^
api-1            | IndentationError: unindent does not match any outer indentation level
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [3975]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [3975]
api-1            | INFO:     Started server process [4039]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [4039]
api-1            | Process SpawnProcess-68:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 154
api-1            |     @traceable  name="rag_pipeline"
api-1            |                 ^^^^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-69:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 154
api-1            |     @traceable () name="rag_pipeline"
api-1            |                   ^^^^
api-1            | SyntaxError: invalid syntax
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | Process SpawnProcess-70:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 4, in <module>
api-1            |     from api.agents.retrieval_generation import rag_pipeline
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 154
api-1            |     @traceable ( name="rag_pipeline"
api-1            |                ^
api-1            | SyntaxError: '(' was never closed
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Started server process [4106]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [4106]
api-1            | INFO:     Started server process [4170]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/agents/retrieval_generation.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [4170]
api-1            | INFO:     Started server process [4234]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/api/endpoints.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [4234]
api-1            | Process SpawnProcess-74:
api-1            | Traceback (most recent call last):
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
api-1            |     self.run()
api-1            |   File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
api-1            |     self._target(*self._args, **self._kwargs)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
api-1            |     target(sockets=sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
api-1            |     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
api-1            |     return runner.run(main)
api-1            |            ^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
api-1            |     return self._loop.run_until_complete(task)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
api-1            |     return future.result()
api-1            |            ^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
api-1            |     await self._serve(sockets)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
api-1            |     config.load()
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
api-1            |     self.loaded_app = import_from_string(self.app)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
api-1            |     module = importlib.import_module(module_str)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
api-1            |     return _bootstrap._gcd_import(name[level:], package, level)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
api-1            |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
api-1            |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
api-1            |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
api-1            |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
api-1            |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
api-1            |   File "/app/apps/api/src/api/app.py", line 5, in <module>
api-1            |     from api.api.endpoints import api_router
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 27
api-1            |     answer=answer[]
api-1            |            ^^^^^^^^
api-1            | SyntaxError: invalid syntax. Perhaps you forgot a comma?
api-1            | WARNING:  StatReload detected changes in 'api/api/endpoints.py'. Reloading...
api-1            | INFO:     Started server process [4299]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | WARNING:  StatReload detected changes in 'api/api/endpoints.py'. Reloading...
api-1            | INFO:     Shutting down
api-1            | INFO:     Waiting for application shutdown.
api-1            | INFO:     Application shutdown complete.
api-1            | INFO:     Finished server process [4299]
api-1            | INFO:     Started server process [4363]
api-1            | INFO:     Waiting for application startup.
api-1            | INFO:     Application startup complete.
api-1            | 2026-07-08 22:11:35,155 - api.api.middleware - INFO - Request started: POST /rag (request_id: c96757f0-0800-44df-9c41-3183b94ac687)
api-1            | 2026-07-08 22:11:35,156 - api.api.middleware - INFO - Request completed: POST /rag (request_id: c96757f0-0800-44df-9c41-3183b94ac687)
api-1            | INFO:     172.19.0.2:45318 - "POST /rag HTTP/1.1" 307 Temporary Redirect
api-1            | 2026-07-08 22:11:35,157 - api.api.middleware - INFO - Request started: POST /rag/ (request_id: a1a15e51-2d09-4018-b772-d93f0fb4a500)
api-1            | 2026-07-08 22:11:35,374 - httpx - INFO - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:batchEmbedContents "HTTP/1.1 200 OK"
api-1            | INFO:     172.19.0.2:45318 - "POST /rag/ HTTP/1.1" 500 Internal Server Error
api-1            | ERROR:    Exception in ASGI application
api-1            | Traceback (most recent call last):
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/protocols/http/h11_impl.py", line 410, in run_asgi
api-1            |     result = await app(  # type: ignore[func-returns-value]
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
api-1            |     return await self.app(scope, receive, send)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
api-1            |     await super().__call__(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
api-1            |     await self.app(scope, receive, _send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/cors.py", line 85, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
api-1            |     with recv_stream, send_stream, collapse_excgroups():
api-1            |                                    ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
api-1            |     self.gen.throw(value)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
api-1            |     response = await self.dispatch_func(request, call_next)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/middleware.py", line 20, in dispatch
api-1            |     response = await call_next(request)
api-1            |                ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
api-1            |     raise app_exc from app_exc.__cause__ or app_exc.__context__
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
api-1            |     await self.app(scope, receive_or_disconnect, send_no_error)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
api-1            |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
api-1            |     await self.middleware_stack(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
api-1            |     await route.handle(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
api-1            |     await self.app(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 115, in app
api-1            |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
api-1            |     raise exc
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
api-1            |     await app(scope, receive, sender)
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 101, in app
api-1            |     response = await f(request)
api-1            |                ^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 355, in app
api-1            |     raw_response = await run_endpoint_function(
api-1            |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/fastapi/routing.py", line 245, in run_endpoint_function
api-1            |     return await run_in_threadpool(dependant.call, **values)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
api-1            |     return await anyio.to_thread.run_sync(func)
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/to_thread.py", line 63, in run_sync
api-1            |     return await get_async_backend().run_sync_in_worker_thread(
api-1            |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2502, in run_sync_in_worker_thread
api-1            |     return await future
api-1            |            ^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run
api-1            |     result = context.run(func, *args)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/api/endpoints.py", line 23, in rag
api-1            |     answer = rag_pipeline(payload.query)
api-1            |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 159, in rag_pipeline
api-1            |     retrieved_context = retrieve_data(question, qdrant_client, top_k)
api-1            |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 59, in retrieve_data
api-1            |     query_embedding = get_embedding(query)
api-1            |                       ^^^^^^^^^^^^^^^^^^^^
api-1            |   File "/app/apps/api/src/api/agents/retrieval_generation.py", line 45, in get_embedding
api-1            |     "input_tokens": response.usage.prompt_tokens,
api-1            |                     ^^^^^^^^^^^^^^
api-1            |   File "/app/.venv/lib/python3.12/site-packages/pydantic/main.py", line 1026, in __getattr__
api-1            |     raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}')
api-1            | AttributeError: 'EmbedContentResponse' object has no attribute 'usage'



## ISSUE 3: AttributeError in EmbedContentResponse ('usage' attribute missing)

### **The Issue End-to-End:**
Following the previous fixes, when the API received a `/rag` request, it successfully initiated the `rag_pipeline`. The first step of the pipeline involves generating an embedding for the user's query using the `get_embedding()` function.

However, the backend immediately threw a fatal error:
```python
AttributeError: 'EmbedContentResponse' object has no attribute 'usage'
```

### **Why It Occurred:**
In `apps/api/src/api/agents/retrieval_generation.py`, within the `get_embedding` function, there was code attempting to extract token usage for LangSmith telemetry:
```python
current_run.metadata["usage_metadata"] = {
    "input_tokens": response.usage.prompt_tokens,
    "total_tokens": response.usage.total_tokens,
}
```
While models like `gemini-2.5-flash` return a `GenerateContentResponse` that *does* include a `usage_metadata` object for token counting, the `google-genai` SDK's `embed_content` endpoint returns an `EmbedContentResponse`. In the current SDK version, this response object **does not** contain a `usage` attribute. Because Python encountered an object without the expected property, it raised an `AttributeError` and crashed the entire RAG pipeline before any vector search could occur.

Additionally, the logs show that multiple attempts were made to fix this, resulting in various `SyntaxError`s (unmatched parentheses, missing imports, etc.) because the file was edited while the Uvicorn server was hot-reloading.

### **The Resolution:**
To rectify this, we removed the unsafe attribute access block completely. 

**Changes Made:**
1. Modified `apps/api/src/api/agents/retrieval_generation.py` to remove the code attempting to read `response.usage`.
2. Added a comment explaining that token tracking for the embedding model is skipped because the SDK doesn't expose it natively on that response object.

**Note on Telemetry:** LangSmith will still automatically trace the duration, latency, and success/failure of the embedding call because we retained the `@traceable` decorator with the `run_type="embedding"` configuration.

The pipeline is now stabilized and the `get_embedding` function returns the vectors cleanly, allowing the semantic search against Qdrant to proceed.
