import os
import sqlite3


def get_connection():
    db_path = os.environ.get("DB_PATH", "data/app.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
