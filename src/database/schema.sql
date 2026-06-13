CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    artist TEXT,
    album TEXT,
    date TEXT,
    genre TEXT,
    duration INTEGER NOT NULL,
    deleted INTEGER NOT NULL
)