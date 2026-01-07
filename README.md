# Floryder3.0# Floryder3.0 (MVP)

This PR seeds the repository with the initial architecture docs, API spec, SQL schema, a small pick engine prototype, and basic CI/Docker scaffolding.

Files included:
- ARCHITECTURE.md
- API_SPEC.md
- DATA_MODELS.sql
- pick_logic_sample.py
- README.md
- .github/workflows/ci.yml
- Dockerfile
- .gitignore
- src/__init__.py
- tests/test_pick_logic.py

Next steps:
- Implement backend fetchers and caching
- Implement /generate-parlay endpoint
- Build frontend SPA

See ARCHITECTURE.md and API_SPEC.md for design details.