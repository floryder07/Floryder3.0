-- Minimal SQL schema for MVP
CREATE TABLE players (
  id INTEGER PRIMARY KEY,
  name TEXT,
  team TEXT,
  pos TEXT,
  last_updated TIMESTAMP
);
CREATE TABLE games (
  id INTEGER PRIMARY KEY,
  date DATE,
  home_team TEXT,
  away_team TEXT
);
CREATE TABLE player_game_logs (
  id INTEGER PRIMARY KEY,
  player_id INTEGER,
  game_id INTEGER,
  pts REAL,
  reb REAL,
  ast REAL,
  usage REAL,
  minutes REAL,
  lineup_flag BOOLEAN,
  FOREIGN KEY(player_id) REFERENCES players(id)
);
CREATE TABLE draftkings_lines (
  id INTEGER PRIMARY KEY,
  game_id INTEGER,
  player_id INTEGER,
  market TEXT,
  line REAL,
  odds INTEGER,
  snapshot_ts TIMESTAMP
);