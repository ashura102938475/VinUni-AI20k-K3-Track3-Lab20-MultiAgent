# Local Langfuse

The repository includes `docker-compose.langfuse.yml` for local development.
Langfuse's current self-hosting guide recommends Docker Compose for local or
low-scale deployments; this repository uses the official v4 web, worker,
Postgres, ClickHouse, Redis, and MinIO services.

Start the local UI/API:

```bash
docker compose -f docker-compose.langfuse.yml up -d
```

Open `http://localhost:3001`, create a project, and copy its public/secret
keys into `.env`:

```env
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=http://localhost:3001
```

Then run the lab with the same shell environment:

```bash
set -a; source .env; set +a
uv run python -m multi_agent_research_lab.cli multi-agent \
  --query "When should multi-agent systems be used?"
```

Stop it with `docker compose -f docker-compose.langfuse.yml down`.
Do not commit `.env`, Langfuse keys, or provider keys.
