import unittest
from app.services.post_service import PostService
from app.config import Config
import sqlite3

class TestPostService(unittest.TestCase):
    def setUp(self):
        """
        Set up the necessary configurations for testing.
        """
        self.app = {'config': Config()}
        self.post_service = PostService(self.app)
    
    def test_create_post(self):
        """
        Test the creation of a new post.
        """
        self.post_service.create_post("My First Post", "This is the content", 1)
        
        # Check if the post is saved in the database
        conn = sqlite3.connect(self.app['config'].DATABASE_URI.split('///')[1])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE title = 'My First Post'")
        post = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(post)
        self.assertEqual(post[1], "My First Post")
        self.assertEqual(post[2], "This is the content")
        self.assertEqual(post[3], 1)
    
    def test_get_all_posts(self):
        """
        Test fetching all posts.
        """
        posts = self.post_service.get_all_posts()
        self.assertIsInstance(posts, list)

if __name__ == "__main__":
    unittest.main()
