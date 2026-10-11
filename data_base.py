from datetime import datetime
import sqlite3

def init_db():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS long_term (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_messages(role , content):
    db = sqlite3.connect("memory.db")
    cur = db.cursor()

    cur.execute(
        """INSERT INTO messages(role , content , created_at) VALUES (? , ? , ?)""",(role , content , datetime.now().isoformat())
    )

    db.commit()
    db.close()


def recent_messages(limit=8):
    db = sqlite3.connect("memory.db")
    cur = db.cursor()

    cur.execute(
        """SELECT role , content FROM messages ORDER BY id DESC LIMIT ? """,
        (limit,)
    )

    rows = cur.fetchall()
    
    messages = []
    for role , content in reversed(rows):
        messages.append({"role" : role , "content" : content})

    db.close()
    return messages
    
def clear_old_messages(limit=20):
    db = sqlite3.connect("memory.db")
    cur = db.cursor()

    cur.execute(
        """DELETE FROM messages WHERE id NOT IN (SELECT id FROM messages ORDER BY id DESC LIMIT ?)""",(limit,)
    )

    db.commit()
    db.close()