# KGRAG — Private Knowledge Graph RAG
## Quickstart (fully local, nothing leaves your network)
cp .env.example .env
# Add any of: CONFLUENCE_TOKEN, NOTION_TOKEN, SLACK_TOKEN etc
docker-compose up -d
# First sync runs automatically. Check source status:
GET /api/sources → { confluence: ok, notion: ok, ... }
## Query via LLM tool call
POST /v1/query { "query": "what did we decide about rate limits" }
→ { answer, sources: [{url, title}], graph_path: [...] }
## Connect to any LLM
Set tool endpoint to http://localhost:8000/v1/query
Works with: LangChain, LlamaIndex, OpenAI function calling, any framework that supports tool/function call pattern
## Adding a Source
Add env var → restart → ConnectorManager auto-detects + syncs
