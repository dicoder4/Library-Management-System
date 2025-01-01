import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                isbn TEXT,
                                available BOOLEAN)''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT)''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                user_id INTEGER,
                                book_id INTEGER,
                                status TEXT,
                                FOREIGN KEY(user_id) REFERENCES users(id),
                                FOREIGN KEY(book_id) REFERENCES books(id))''')
        self.conn.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
