import sqlite3


def create_book(title, author, price, category):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, author, price, category) VALUES (?, ?, ?, ?)",(title, author, price, category))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Books 
                (id INTEGER PRIMARY KEY 
                AUTOINCREMENT,title TEXT,author TEXT,price 
                REAL,category TEXT)''')
    conn.commit()
    conn.close()
    create_book("Book 1", "Author 1", 9.99, "Fiction")

