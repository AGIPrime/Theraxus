# rag_optimizer.py

import hnswlib
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import numpy as np
from config import CACHE_DIR, RAG_CONFIG
from database_manager import DatabaseManager
import json
import logging

# ===========================
# Logger Setup
# ===========================

logger = logging.getLogger(__name__)

# ===========================
# RAGOptimizer Class
# ===========================

class RAGOptimizer:
    def __init__(self):
        """Initialize the RAG Optimizer with embedding model and vector index."""
        self.db_manager = DatabaseManager()
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # You can change the model as needed
        self.dim = self.embedding_model.get_sentence_embedding_dimension()
        self.index = hnswlib.Index(space='cosine', dim=self.dim)
        self.index_file = CACHE_DIR / 'hnsw_index.bin'
        self.id_to_doc = {}
        
        if self.index_file.exists():
            # Load existing index and ID mappings
            self.index.load_index(str(self.index_file))
            with open(CACHE_DIR / 'id_to_doc.json', 'r') as f:
                self.id_to_doc = json.load(f)
            logger.info("Loaded existing HNSW index and ID mappings.")
        else:
            # Initialize a new HNSW index
            self.index.init_index(max_elements=10000, ef_construction=200, M=16)
            self.index.set_ef(RAG_CONFIG['TOP_K'])
            logger.info("Initialized new HNSW index.")
            # Build index with a placeholder for multi-user support
            self.build_index()

    # ===========================
    # Build Index for Multi-User (Placeholder)
    # ===========================
    
    def build_index(self, user_id: str = "global"):
        """
        Build the vector index from uploaded documents for a specific user.
        
        :param user_id: Unique identifier for the user. Default is "global" for shared access.
        """
        documents = self.db_manager.get_documents(user_id)
        doc_names = list(documents.keys())
        if not doc_names:
            logger.warning(f"No documents found to build the index for user {user_id}.")
            return
        
        # Generate embeddings for all documents
        embeddings = self.embedding_model.encode([documents[doc]['content'] for doc in doc_names])
        embeddings = np.array(embeddings).astype('float32')
        
        # Add embeddings to the HNSW index
        self.index.add_items(embeddings, range(len(doc_names)))
        self.id_to_doc = {str(idx): doc for idx, doc in enumerate(doc_names)}
        
        # Save the index and ID mappings for future use
        self.index.save_index(str(self.index_file))
        with open(CACHE_DIR / 'id_to_doc.json', 'w') as f:
            json.dump(self.id_to_doc, f, indent=4)
        logger.info(f"HNSW index built and saved for user {user_id}.")

    # ===========================
    # Search Documents for Multi-User (Placeholder)
    # ===========================
    
    def search_documents(self, query: str, user_id: str = "global") -> List[str]:
        """
        Search for top K relevant documents based on the query for a specific user.
        
        :param query: The query string.
        :param user_id: Unique identifier for the user. Default is "global" for shared access.
        :return: List of relevant document names.
        """
        try:
            # Generate embedding for the query
            query_embedding = self.embedding_model.encode([query]).astype('float32')
            
            # Perform KNN search
            labels, distances = self.index.knn_query(query_embedding, k=RAG_CONFIG['TOP_K'])
            
            # Retrieve document names based on labels
            top_docs = [self.id_to_doc[str(label)] for label in labels[0]]
            logger.info(f"Retrieved top {RAG_CONFIG['TOP_K']} documents for user {user_id} and query: {query}")
            return top_docs
        except Exception as e:
            logger.error(f"Error searching documents for user {user_id}: {e}")
            return []

    # ===========================
    # Update Index for New Documents (Multi-User Placeholder)
    # ===========================
    
    def update_index_for_user(self, user_id: str):
        """
        Update the index for a specific user when new documents are added.
        
        :param user_id: Unique identifier for the user.
        """
        logger.info(f"Updating index for user {user_id}...")
        # Placeholder: Implement the logic to only update the index incrementally for specific users.
        # Current implementation builds from scratch; needs incremental update support.

    # ===========================
    # Instructions for Modifications
    # ===========================
    
    # This class handles the Retrieval-Augmented Generation (RAG) by embedding documents and performing searches.
    # Enhancements made:
    # - Introduced placeholders for multi-user support in indexing and searching.
    # - Improved logging for clarity in user-specific document processing.
    # - Methods can be extended to handle incremental updates for new documents.

    # To extend functionality:
    # - Change the embedding model by initializing SentenceTransformer with a different model name.
    # - Implement an incremental index update method (`update_index_for_user`) for improved efficiency.
    # - Adjust HNSW index parameters (`ef_construction`, `M`) in the `__init__` method as needed.
