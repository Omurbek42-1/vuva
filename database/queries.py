class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            genre TEXT
        )
    """
    DROP_GENRES_TABLE = "DROP TABLE IF EXISTS genres"
    DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books"
    CREATE_GENRES_TABLE = """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """