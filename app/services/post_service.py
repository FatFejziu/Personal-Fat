from app.db import init_db
from app.models.post import Post
import logging

class PostService:
    def __init__(self, app):
        self.app = app
    
    def create_post(self, title, content, user_id):
        """
        Creates a new post.
        """
        conn = sqlite3.connect(self.app['config'].DATABASE_URI.split('///')[1])
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO posts (title, content, user_id)
            VALUES (?, ?, ?)
        ''', (title, content, user_id))
        
        conn.commit()
        conn.close()
        
        logging.info(f"Post '{title}' created successfully.")
    
     def get_all_posts(self):
        conn = sqlite3.connect(self.app['config'].DATABASE_URI.split('///')[1])
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        
        conn.close()
        
        # Convert rows to Post objects
        post_objects = []
        for post in posts:
            post_objects.append(Post(post[0], post[1], post[2], post[3]))
        
        return post_objects