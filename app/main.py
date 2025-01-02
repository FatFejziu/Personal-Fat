from app.config import Config
from app.db import init_db
from app.services.user_service import UserService
from app.services.post_service import PostService
import logging
import os
import logging

# Ensure logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize logger
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

def create_app():
    """
    Initializes the app, connects to the database, and sets up services.
    """
    app = {}
    
    # Configure settings
    app['config'] = Config()
    
    # Initialize database
    init_db(app)
    
    # Set up services
    user_service = UserService(app)
    post_service = PostService(app)
    
    logging.info("App created successfully with User and Post services.")
    return app

def main():
    """
    The main entry point for starting the application.
    """
    app = create_app()
    logging.info("Application started.")
    
    # Example of using services
    user_service = app.get('user_service')
    user_service.create_user("John", 28, "john@example.com")
    
    post_service = app.get('post_service')
    post_service.create_post("John's First Post", "Hello, World!", 1)
    
if __name__ == '__main__':
    main()