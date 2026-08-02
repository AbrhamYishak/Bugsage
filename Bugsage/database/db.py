import sqlite3
conn = sqlite3.connect("errors.db")
cursor = conn.cursor()
def create():
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
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AiMODEL (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ModelName TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );            
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS API (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        APIKey TEXT NOT NULL,
        model_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (model_id) REFERENCES AiMODEL(id) ON DELETE CASCADE
    ); """)
    cursor.execute("""    
        CREATE TABLE IF NOT EXISTS CurrentSelection (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_id INTEGER NOT NULL,
        model_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (model_id) REFERENCES AiMODEL(id) ON DELETE CASCADE
        FOREIGN KEY (api_id) REFERENCES API(id) ON DELETE CASCADE           
    ); """)
    conn.commit()
    # conn.close()
def search(errorType, errorCase):
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
def getAPIKeys():
    cursor.execute("""
        SELECT API.id, API.APIKey, AiMODEL.ModelName
        FROM API
        JOIN AiMODEL
        ON API.model_id = AiMODEL.id
    """)
    return cursor.fetchall()


def addAPIKey(apikey, modelname):
    # Get model id
    cursor.execute("""
        SELECT id FROM AiMODEL
        WHERE ModelName = ?
    """, (modelname,))
    
    model = cursor.fetchone()

    if not model:
        raise Exception("Model does not exist")

    model_id = model[0]

    cursor.execute("""
        INSERT INTO API(APIKey, model_id)
        VALUES (?, ?)
    """, (apikey, model_id))

    conn.commit()


def removeAPIKey(apikey):
    cursor.execute("""
        DELETE FROM API
        WHERE APIKey = ?
    """, (apikey,))

    conn.commit()


def updateAPIKey(old_key, new_key):
    cursor.execute("""
        UPDATE API
        SET APIKey = ?
        WHERE APIKey = ?
    """, (new_key, old_key))

    conn.commit()

def getModels():
    cursor.execute("""
        SELECT *
        FROM AiMODEL
    """)
    return cursor.fetchall()


def addModel(modelname):
    cursor.execute("""
        INSERT INTO AiMODEL(ModelName)
        VALUES (?)
    """, (modelname,))

    conn.commit()


def removeModel(modelname):
    cursor.execute("""
        DELETE FROM AiMODEL
        WHERE ModelName = ?
    """, (modelname,))

    conn.commit()


def updateModel(old_name, new_name):
    cursor.execute("""
        UPDATE AiMODEL
        SET ModelName = ?
        WHERE ModelName = ?
    """, (new_name, old_name))

    conn.commit()
def selectModel(model_id):
    # Find an API for this model
    cursor.execute("""
        SELECT id
        FROM API
        WHERE model_id = ?
        LIMIT 1
    """, (model_id,))

    api = cursor.fetchone()

    if api is None:
        raise Exception("No API keys found for this model.")

    api_id = api[0]

    # Check if a selection already exists
    cursor.execute("SELECT id FROM CurrentSelection LIMIT 1")
    selection = cursor.fetchone()

    if selection is None:
        # No row exists, create one
        cursor.execute("""
            INSERT INTO CurrentSelection (id, model_id, api_id)
            VALUES (1, ?, ?)
        """, (model_id, api_id))
    else:
        # Update the existing row
        cursor.execute("""
            UPDATE CurrentSelection
            SET model_id = ?, api_id = ?
            WHERE id = ?
        """, (model_id, api_id, selection[0]))

    conn.commit()
def selectAPIKey(api_id):
    # Find which model owns this API
    cursor.execute("""
        SELECT model_id
        FROM API
        WHERE id = ?
    """, (api_id,))

    model = cursor.fetchone()

    if model is None:
        raise Exception("API key not found.")

    model_id = model[0]

    # Check if a selection already exists
    cursor.execute("SELECT id FROM CurrentSelection LIMIT 1")
    selection = cursor.fetchone()

    if selection is None:
        # No row exists, create one
        cursor.execute("""
            INSERT INTO CurrentSelection (id, model_id, api_id)
            VALUES (1, ?, ?)
        """, (model_id, api_id))
    else:
        # Update the existing row
        cursor.execute("""
            UPDATE CurrentSelection
            SET model_id = ?, api_id = ?
            WHERE id = ?
        """, (model_id, api_id, selection[0]))

    conn.commit()
def getSelectedAPIKey():
    cursor.execute("""
        SELECT API.APIKey
        FROM CurrentSelection
        JOIN API
        ON CurrentSelection.api_id = API.id
    """)
    result = cursor.fetchone()
    return result[0] if result else None
def getSelectedModel():
    cursor.execute("""
        SELECT AiMODEL.ModelName
        FROM CurrentSelection
        JOIN AiMODEL
        ON CurrentSelection.model_id = AiMODEl.id
    """)
    result = cursor.fetchone()
    return result[0] if result else None
