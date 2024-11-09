# voice_runllm.py

import signal
import sys
import time
from stt import WhisperSTT
from tts import TTS
from runllm import TheraxusAI
from config import LOGGING_CONFIG
import logging

# ===========================
# Logger Setup
# ===========================

# Configure logging based on settings in config.py
logging.basicConfig(
    filename=LOGGING_CONFIG['LOG_FILE'],
    level=logging.getLevelName(LOGGING_CONFIG['LOG_LEVEL']),
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)

# ===========================
# VoiceInterface Class
# ===========================

class VoiceInterface:
    def __init__(self, user_id="default_user"):
        """Initialize voice interface with STT, TTS, and AI components."""
        try:
            self.user_id = user_id  # Placeholder for multi-user support
            self.stt = WhisperSTT()
            self.tts = TTS()
            self.ai = TheraxusAI()
            self.running = True
            logger.info(f"Voice Interface initialized successfully for user: {user_id}")
        except Exception as e:
            logger.error(f"Voice Interface initialization error for user {user_id}: {e}")
            sys.exit(1)
    
    def exit_gracefully(self, signum, frame):
        """Handle graceful exit on Ctrl+C."""
        print("\nExiting voice interface...")
        logger.info("Voice Interface terminated by user.")
        self.cleanup()
        sys.exit(0)
    
    def start_voice_chat(self):
        """Start the voice chat loop."""
        signal.signal(signal.SIGINT, self.exit_gracefully)
        print("Voice Interface Ready! Speak into your microphone.")
        self.tts.speak("Hello! I'm ready to assist you.")
        
        while self.running:
            try:
                print("\nListening...")
                user_input, success = self.stt.process_audio()
                
                if success and user_input:
                    print(f"You: {user_input}")
                    response = self.ai.generate_response(user_input, user_id=self.user_id)
                    print(f"AI: {response}")
                    self.tts.speak(response)
                else:
                    print("AI: I didn't catch that. Please try again.")
                    self.tts.speak("I didn't catch that. Please try again.")
                
                time.sleep(1)  # Short pause before next listening
                
            except Exception as e:
                logger.error(f"Voice chat error for user {self.user_id}: {e}")
                print("AI: I encountered an error. Please try again.")
                self.tts.speak("I encountered an error. Please try again.")
    
    def cleanup(self):
        """Cleanup resources."""
        try:
            if self.stt:
                self.stt.cleanup()
            if self.tts:
                self.tts.cleanup()
            logger.info("Voice Interface cleanup completed.")
        except Exception as e:
            logger.error(f"Cleanup error for user {self.user_id}: {e}")

# ===========================
# Main Function for Voice-Based Chat
# ===========================

def main():
    """Main function to start the voice interface."""
    # Placeholder for selecting or assigning user_id, currently default_user
    user_id = "default_user"  # Future: Implement mechanism to assign user_id based on voice input or session
    interface = VoiceInterface(user_id=user_id)
    interface.start_voice_chat()

# ===========================
# Entry Point
# ===========================

if __name__ == "__main__":
    main()

# ===========================
# Instructions for Modifications
# ===========================

# This script serves as the main entry point for the voice-based chat interface of Theraxus AI.
# To modify:
# - Enhance the voice command recognition to handle specific commands like 'load', 'docs', etc.
# - Integrate multi-user support by handling user IDs based on voice input or separate sessions.
# - Improve error handling and feedback mechanisms for better user experience.
# - Implement voice prompts or confirmations as needed.
