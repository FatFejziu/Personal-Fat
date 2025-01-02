import sqlite3
import os

def init_db(app):
    """
    Initializes the SQLite database and ensures tables are created.
    """
    db_path = app['config'].DATABASE_URI.split('///')[1]
    
    # Check if database exists; if not, create it
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            email TEXT UNIQUE NOT NULL)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL,
                            user_id INTEGER,
                            FOREIGN KEY (user_id) REFERENCES users(id))''')
        
        conn.commit()
        conn.close()
        logging.info("Database initialized.")