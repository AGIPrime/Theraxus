# stt.py

import whisper
import numpy as np
import sounddevice as sd
import queue
from config import STT_CONFIG
import logging

# ===========================
# Logger Setup
# ===========================

logger = logging.getLogger(__name__)

# ===========================
# WhisperSTT Class
# ===========================

class WhisperSTT:
    def __init__(self):
        """Initialize the Whisper STT model."""
        try:
            self.model = whisper.load_model(STT_CONFIG['MODEL_NAME'])  # e.g., 'base'
            self.sample_rate = STT_CONFIG['SAMPLE_RATE']
            self.channels = STT_CONFIG['CHANNELS']
            self.chunk_size = STT_CONFIG['CHUNK_SIZE']
            self.audio_queue = queue.Queue()
            self.recording = False
            logger.info(f"Whisper STT model '{STT_CONFIG['MODEL_NAME']}' loaded successfully.")
        except Exception as e:
            logger.error(f"Whisper STT initialization error: {e}")
            raise

    def _audio_callback(self, indata, frames, time_info, status):
        """Callback function to capture audio input."""
        if status:
            logger.warning(f"Audio status: {status}")
        self.audio_queue.put(indata.copy())

    def record_audio(self, duration: int = 5) -> np.ndarray:
        """Record audio from the microphone."""
        try:
            with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, callback=self._audio_callback):
                logger.info(f"Recording audio for {duration} seconds...")
                frames = []
                for _ in range(0, int(self.sample_rate / self.chunk_size * duration)):
                    data = self.audio_queue.get()
                    frames.append(data)
                audio_data = np.concatenate(frames, axis=0)
                return audio_data
        except Exception as e:
            logger.error(f"Audio recording error: {e}")
            return np.array([])

    def process_audio(self) -> (str, bool):
        """Process the recorded audio and transcribe it."""
        try:
            audio = self.record_audio()
            if audio.size == 0:
                return "", False
            logger.info("Transcribing audio...")
            result = self.model.transcribe(audio)
            transcription = result["text"].strip()
            logger.debug(f"Transcription: {transcription}")
            return transcription, True
        except Exception as e:
            logger.error(f"Audio processing error: {e}")
            return "", False

    def cleanup(self):
        """Cleanup resources if any."""
        try:
            logger.info("Whisper STT cleanup completed.")
        except Exception as e:
            logger.error(f"Whisper STT cleanup error: {e}")

# ===========================
# Instructions for Modifications
# ===========================

# This class manages the Speech-to-Text (STT) functionality using OpenAI's Whisper model.
# To modify:
# - Change the Whisper model by updating 'MODEL_NAME' in STT_CONFIG within config.py.
# - Adjust the recording duration by modifying the 'duration' parameter in the record_audio method.
# - Implement additional audio preprocessing steps if needed before transcription.
