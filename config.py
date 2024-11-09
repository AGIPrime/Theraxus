# config.py

import os
from pathlib import Path

# ===========================
# Base Directory Configuration
# ===========================

# Base Directory: The root directory of the project
BASE_DIR = Path(__file__).resolve().parent

# ===========================
# Data Directories Configuration
# ===========================

# Data Directories: Where different types of data are stored
DATA_DIR = BASE_DIR / 'data'
AUDIO_DIR = DATA_DIR / 'audio'
DOCS_DIR = DATA_DIR / 'docs'
CONVERSATIONS_DIR = DATA_DIR / 'conversations'
VECTOR_DB_DIR = DATA_DIR / 'vector_db'
CACHE_DIR = DATA_DIR / 'cache'

# ===========================
# Multi-User Data Configuration
# ===========================

# Multi-User Support: Base directory for all users
USERS_DIR = DATA_DIR / 'users'
USER_SPECIFIC_DIRS = ['audio', 'docs', 'conversations', 'vector_db', 'cache']

# ===========================
# Models Directory Configuration
# ===========================

# Models Directory: Where pre-trained models are stored
MODELS_DIR = BASE_DIR / 'models'

# ===========================
# Logs Directory Configuration
# ===========================

# Logs Directory: Where log files are stored
LOGS_DIR = BASE_DIR / 'logs'

# ===========================
# Ensure All Directories Exist
# ===========================

# Automatically create directories if they don't exist
for directory in [DATA_DIR, AUDIO_DIR, DOCS_DIR, CONVERSATIONS_DIR, VECTOR_DB_DIR, CACHE_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Create a base directory for multi-user support
USERS_DIR.mkdir(parents=True, exist_ok=True)

# Placeholder: Automatically create user-specific directories if they don't exist
def ensure_user_directories(user_id: str):
    user_base_dir = USERS_DIR / user_id
    for sub_dir in USER_SPECIFIC_DIRS:
        (user_base_dir / sub_dir).mkdir(parents=True, exist_ok=True)

# ===========================
# Whisper STT Configuration
# ===========================

STT_CONFIG = {
    'MODEL_NAME': 'base',      # Whisper model size: 'tiny', 'base', 'small', 'medium', 'large'
    'SAMPLE_RATE': 16000,      # Audio sample rate in Hz
    'CHANNELS': 1,              # Number of audio channels (1 for mono, 2 for stereo)
    'CHUNK_SIZE': 1024,         # Size of audio chunks for processing
}

# ===========================
# TTS Configuration
# ===========================

TTS_CONFIG = {
    'RATE': 150,                # Speech rate (words per minute)
    'VOLUME': 1.0,              # Volume level (0.0 to 1.0)
}

# ===========================
# RAG Configuration
# ===========================

RAG_CONFIG = {
    'TOP_K': 5,                 # Number of top documents to retrieve for context
}

# ===========================
# Logging Configuration
# ===========================

LOGGING_CONFIG = {
    'LOG_FILE': LOGS_DIR / 'theraxus.log',  # Log file path
    'LOG_LEVEL': 'INFO',                    # Logging level: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
}

# ===========================
# Instructions for Modifications
# ===========================

# You can modify the above configurations to customize the behavior of Theraxus AI.
# For example:
# - To change the Whisper model size, adjust 'MODEL_NAME' in STT_CONFIG.
# - To alter the speech rate or volume, modify 'RATE' and 'VOLUME' in TTS_CONFIG.
# - To retrieve a different number of documents, change 'TOP_K' in RAG_CONFIG.
# - To support a new user, call ensure_user_directories(user_id) to set up user-specific directories.
