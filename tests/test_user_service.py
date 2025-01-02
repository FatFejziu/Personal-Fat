import unittest
from app.services.user_service import UserService
from app.config import Config

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.app = {'config': Config()}
        self.user_service = UserService(self.app)

    def test_create_user(self):
        self.user_service.create_user("Alice", 25, "alice@example.com")
        # Check if user exists in the database (assertions)

if __name__ == "__main__":
    unittest.main()
