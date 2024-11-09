# tts.py

import pyttsx3
import threading
from config import TTS_CONFIG
import logging

# ===========================
# Logger Setup
# ===========================

logger = logging.getLogger(__name__)

# ===========================
# TTS Class
# ===========================

class TTS:
    def __init__(self):
        """Initialize the pyttsx3 TTS engine."""
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', TTS_CONFIG['RATE'])
            self.engine.setProperty('volume', TTS_CONFIG['VOLUME'])
            # Optionally, set voice (male/female) here
            # voices = self.engine.getProperty('voices')
            # self.engine.setProperty('voice', voices[0].id)  # Change index for different voices
            logger.info("pyttsx3 TTS engine initialized successfully.")
        except Exception as e:
            logger.error(f"TTS initialization error: {e}")
            raise

    def speak(self, text: str):
        """Convert text to speech."""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            logger.debug(f"TTS speaking: {text[:50]}...")
        except Exception as e:
            logger.error(f"TTS speaking error: {e}")

    def speak_async(self, text: str):
        """Speak text asynchronously to avoid blocking."""
        thread = threading.Thread(target=self.speak, args=(text,))
        thread.start()

    def cleanup(self):
        """Cleanup the TTS engine."""
        try:
            self.engine.stop()
            logger.info("pyttsx3 TTS engine stopped.")
        except Exception as e:
            logger.error(f"TTS cleanup error: {e}")

# ===========================
# Instructions for Modifications
# ===========================

# This class handles the Text-to-Speech (TTS) functionality using pyttsx3.
# To modify:
# - Change the speech rate or volume by updating 'RATE' and 'VOLUME' in TTS_CONFIG within config.py.
# - Select different voices by uncommenting and modifying the voice selection lines.
# - Implement additional TTS features like changing language if supported by pyttsx3.
