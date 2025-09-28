# Deployment

## Docker Compose

1. Copy `.env.example` to `.env` and set values
2. `docker compose up -d --build`
3. Open `http://localhost` (nginx → web, api on `/api`)

## Configuration

- External tools: `BAYWALK_BASE_URL`, `PERCEPTIONLAB_BASE_URL`, etc.
- Webhooks: set `WEBHOOK_SECRET` and configure sources to call `/webhooks/:source`
- Auth: set `OAUTH_*` and `ALLOW_LOCAL_LOGIN=false` for production
- CORS: `ALLOWED_CORS_ORIGINS` comma-separated

## Database

- Postgres 15 by default in compose
- Apply Alembic migrations:
  - `alembic -c api/migrations/alembic.ini upgrade head`

## Health

- API: `/health`
- Nginx: `/health` returns `ok`

## Images

- Built via GitHub Actions on tags to `ghcr.io/<org>/operain-api` and `operain-web`
