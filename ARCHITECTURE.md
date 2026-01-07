# Floryder — Architecture (MVP)

Overview:
- SPA frontend (React)
- Backend service (Python/Node) exposing REST endpoints
- Redis cache + lightweight DB (SQLite/Postgres)
- External APIs: balldontlie, API-NBA (RapidAPI), DraftKings snapshot

Components:
- Fetchers (stat, lineup, lines)
- Candidate generator
- Risk filters (Safe/Normal/Moonshot)
- Confidence scorer
- Parlay assembler
- Backtester & Monte Carlo simulator
- Caching layer & rate limiter
- Monitoring & logging

Caching TTLs:
- player_stats: 15m
- team_defense: 2h
- lineup: 5m
- parlay_response: 60s
- backtest_result: 15m