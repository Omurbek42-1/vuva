import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(e)


def insert_feedback(conn, user_id, feedback_text, rating):
    sql = """
        INSERT INTO feedback_results (user_id, feedback_text, rating)
        VALUES (?, ?, ?)
    """
    cur = conn.cursor()
    cur.execute(sql, (user_id, feedback_text, rating))
    conn.commit()
    print("Feedback data inserted successfully")


def create_db_structure(db_file):
    sql_create_table = """
        CREATE TABLE IF NOT EXISTS feedback_results (
            id INTEGER PRIMARY KEY,
            user_id TEXT NOT NULL,
            feedback_text TEXT NOT NULL,
            rating INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """

    
    conn = create_connection(db_file)
    if conn is not None:
        
        create_table(conn, sql_create_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    database = r"your_database.db"  
    create_db_structure(database)
