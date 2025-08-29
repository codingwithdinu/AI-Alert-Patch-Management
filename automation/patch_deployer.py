"""
Not used directly because we embed a scheduler in the API.
Left here for CLI testing if you want to run once.
"""
from datetime import datetime
from pathlib import Path
import sqlite3

DB = Path(__file__).resolve().parents[1] / "backend" / "data.db"

def run_once():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("UPDATE patches SET deployed=1 WHERE scheduled_at IS NOT NULL AND scheduled_at <= datetime('now');")
    con.commit()
    con.close()

if __name__ == "__main__":
    run_once()
