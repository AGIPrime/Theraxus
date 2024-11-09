# database_manager.py

import json
from pathlib import Path
from typing import List, Dict
from config import DATA_DIR, CONVERSATIONS_DIR, DOCS_DIR, VECTOR_DB_DIR, CACHE_DIR, LOGGING_CONFIG
import logging

# ===========================
# Logger Setup
# ===========================

# Configure logging based on settings in config.py
logging.basicConfig(
    filename=LOGGING_CONFIG['LOG_FILE'],
    level=getattr(logging, LOGGING_CONFIG['LOG_LEVEL']),
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)

# ===========================
# DatabaseManager Class
# ===========================

class DatabaseManager:
    def __init__(self):
        """Initialize the Database Manager with necessary file paths."""
        self.conversations_path = CONVERSATIONS_DIR / 'conversations.json'
        self.docs_path = DOCS_DIR / 'documents.json'
        self.vector_db_path = VECTOR_DB_DIR / 'vector_db.json'

        # Initialize JSON files if they don't exist
        for path in [self.conversations_path, self.docs_path, self.vector_db_path]:
            if not path.exists():
                with open(path, 'w') as f:
                    json.dump({}, f)
                logger.info(f"Created new database file: {path}")

    # ===========================
    # Chat History Management (Multi-User)
    # ===========================

    def get_chat_history(self, user_id: str) -> List[Dict]:
        """
        Retrieve chat history for a specific user.
        
        :param user_id: The unique identifier for the user.
        :return: List of dictionaries containing chat history.
        """
        try:
            with open(self.conversations_path, 'r') as f:
                data = json.load(f)
            # Log retrieval for specific user
            logger.info(f"Retrieved chat history for user {user_id}")
            return data.get(user_id, [])
        except Exception as e:
            logger.error(f"Error retrieving chat history for user {user_id}: {e}")
            return []

    def add_chat(self, user_id: str, role: str, content: str):
        """
        Add a chat entry for a specific user.
        
        :param user_id: The unique identifier for the user.
        :param role: The role of the speaker ('user' or 'assistant').
        :param content: The content of the message.
        """
        try:
            with open(self.conversations_path, 'r') as f:
                data = json.load(f)
            
            # Initialize user chat history if it doesn't exist
            if user_id not in data:
                data[user_id] = []
            
            # Add new chat message to the user's chat history
            data[user_id].append({'role': role, 'content': content})
            
            with open(self.conversations_path, 'w') as f:
                json.dump(data, f, indent=4)
            
            logger.info(f"Added {role} message for user {user_id}")
        except Exception as e:
            logger.error(f"Error adding chat for user {user_id}: {e}")

    # ===========================
    # Document Management (Multi-User Placeholder)
    # ===========================

    def get_documents(self, user_id: str = "global") -> Dict:
        """
        Retrieve all uploaded documents, with a placeholder for multi-user support.
        
        :param user_id: The unique identifier for the user (or "global" for shared documents).
        :return: Dictionary containing all documents.
        """
        try:
            with open(self.docs_path, 'r') as f:
                data = json.load(f)
            
            # Placeholder for user-specific documents (currently retrieving all)
            # In the future, document retrieval can be tailored per user by storing documents separately.
            logger.info(f"Retrieved documents for user {user_id}")
            return data
        except Exception as e:
            logger.error(f"Error retrieving documents for user {user_id}: {e}")
            return {}

    def add_document(self, doc_name: str, content: str, user_id: str = "global"):
        """
        Add a new document for a user or globally accessible.
        
        :param doc_name: The name of the document to be added.
        :param content: The content of the document.
        :param user_id: The unique identifier for the user (or "global" for shared documents).
        """
        try:
            with open(self.docs_path, 'r') as f:
                data = json.load(f)
            
            # Placeholder for user-specific document management
            # Currently, documents are shared across users; can be changed to manage user-specific documents.
            data[doc_name] = {'content': content}

            with open(self.docs_path, 'w') as f:
                json.dump(data, f, indent=4)
            
            logger.info(f"Added new document: {doc_name} for user {user_id}")
        except Exception as e:
            logger.error(f"Error adding document {doc_name} for user {user_id}: {e}")

    # ===========================
    # Vector Database Management (Multi-User Placeholder)
    # ===========================

    def save_vector_db(self, vectors: Dict, user_id: str = "global"):
        """
        Save the vector database for a user or globally accessible.
        
        :param vectors: The dictionary containing vector data to be saved.
        :param user_id: The unique identifier for the user (or "global" for shared vector data).
        """
        try:
            # Placeholder for saving user-specific vector database
            # Currently, all vectors are saved in one file; can be adapted for user-specific vector databases.
            with open(self.vector_db_path, 'w') as f:
                json.dump(vectors, f)
            logger.info(f"Vector database updated for user {user_id}")
        except Exception as e:
            logger.error(f"Error saving vector database for user {user_id}: {e}")

    def load_vector_db(self, user_id: str = "global") -> Dict:
        """
        Load the vector database for a user or globally accessible.
        
        :param user_id: The unique identifier for the user (or "global" for shared vector data).
        :return: Dictionary containing the vector database.
        """
        try:
            with open(self.vector_db_path, 'r') as f:
                data = json.load(f)
            logger.info(f"Vector database loaded for user {user_id}")
            return data
        except Exception as e:
            logger.error(f"Error loading vector database for user {user_id}: {e}")
            return {}

    # ===========================
    # Instructions for Modifications
    # ===========================

    # This class manages all database interactions, including chat histories and document storage.
    # Enhancements made:
    # - Added placeholders for multi-user support in chat histories, document management, and vector database.
    # - Improved logging to clearly indicate which user actions are being performed.

    # To extend functionality:
    # - Implement additional methods for deleting chats or documents.
    # - Enhance user-specific document management by creating a dedicated document structure per user.
    # - Integrate with a more robust database system like SQLite or PostgreSQL if needed for scalability.
