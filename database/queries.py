import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def select_all_feedbacks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback_results")
    rows = cur.fetchall()
    return rows


def select_feedbacks_by_rating(conn, rating):
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedback_results WHERE rating = ?", (rating,))
    rows = cur.fetchall()
    return rows


def delete_feedback_by_id(conn, id):
    sql = "DELETE FROM feedback_results WHERE id = ?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print(f"Feedback with id {id} deleted successfully")


def main():
    database = r"your_database.db"  
    conn = create_connection(database)
    if conn is not None:
        
        all_feedbacks = select_all_feedbacks(conn)
        print("All feedbacks:")
        for feedback in all_feedbacks:
            print(feedback)

       
        rating = 5
        specific_feedbacks = select_feedbacks_by_rating(conn, rating)
        print(f"\nFeedbacks with rating {rating}:")
        for feedback in specific_feedbacks:
            print(feedback)

     
        feedback_id_to_delete = 1
        delete_feedback_by_id(conn, feedback_id_to_delete)

        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
