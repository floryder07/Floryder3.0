# API Spec (MVP)

POST /generate-parlay
- Request body (JSON):
  - risk: "safe" | "normal" | "moonshot"
  - legs: integer 1..8
  - statFocus: "PTS" | "REB" | "AST" (optional)
  - venueSensitivity: boolean (optional)
  - maxOddsPerLeg: integer (optional)

- Response: JSON with parlay summary and legs. Example leg object: