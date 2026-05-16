import sqlite3
conn = sqlite3.connect("errors.db")
cursor = conn.cursor()
def create():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS errors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        error_type TEXT NOT NULL,
        package TEXT,
        pattern TEXT,

        explanation TEXT NOT NULL,
        fix TEXT,
        example TEXT,

        severity TEXT,
        category TEXT,

        docs_url TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def search(errorType):
    print(errorType, type(errorType))
    cursor.execute("""
    SELECT * FROM errors
    WHERE error_type = ?
    """, (errorType,))
    result = cursor.fetchone()
    return result