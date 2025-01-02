from app.db import init_db
from app.models.user import User
import logging

class UserService:
    def __init__(self, app):
        self.app = app
    
    def create_user(self, name, age, email):
        """
        Creates a new user and stores it in the database.
        """
        conn = sqlite3.connect(self.app['config'].DATABASE_URI.split('///')[1])
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO users (name, age, email)
            VALUES (?, ?, ?)
        ''', (name, age, email))
        
        conn.commit()
        conn.close()
        
        logging.info(f"User {name} created successfully.")
    def get_all_users(self):
        conn = sqlite3.connect(self.app['config'].DATABASE_URI.split('///')[1])
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        conn.close()
        
        # Convert rows to User objects
        user_objects = []
        for user in users:
            user_objects.append(User(user[0], user[1], user[2], user[3]))
        
        return user_objects