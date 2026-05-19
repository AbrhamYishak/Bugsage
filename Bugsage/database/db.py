import sqlite3
conn = sqlite3.connect("errors.db")
cursor = conn.cursor()
def create():
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS errors (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,

    #     error_type TEXT NOT NULL,
    #     package TEXT,
    #     pattern TEXT,

    #     explanation TEXT NOT NULL,
    #     fix TEXT,
    #     example TEXT,

    #     severity TEXT,
    #     category TEXT,

    #     docs_url TEXT,

    #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    # )
    # """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS error_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    error_type_id INTEGER NOT NULL,

    case_name TEXT,

    explanation_beginner TEXT NOT NULL,
    explanation_intermediate TEXT,
    explanation_advanced TEXT,

    fix TEXT,
    example TEXT,

    severity_override TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (error_type_id) REFERENCES error_types(id));
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS error_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    error_type TEXT NOT NULL,
    package TEXT,

    category TEXT,
    severity TEXT,
    general_explanation TEXT,
    general_fix TEXT,
    docs_url TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()

def search(errorType, errorCase):
    print(errorType, type(errorType))
    cursor.execute("""
    SELECT * FROM error_cases
    WHERE case_name = ?
    """, (errorCase,))
    errorcase = cursor.fetchone()
    if not errorcase:
        cursor.execute("""
        SELECT * FROM error_types
        WHERE error_type = ?
        """, (errorType,))
        errorType = cursor.fetchone()
        return errorType
    return errorcase