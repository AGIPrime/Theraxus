import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread
from voice_runllm import VoiceInterface
from runllm import TheraxusAI
import os

class TheraxusApp:
    def __init__(self, root, user_id="default_user"):
        self.root = root
        self.root.title("Theraxus - Advanced Text and Voice Interface")
        self.root.geometry("800x600")
        
        # User-specific identifier
        self.user_id = user_id

        # Initialize TheraxusAI for text mode with user_id
        self.theraxus_text = TheraxusAI(user_id=self.user_id)
        
        # Initialize VoiceInterface for voice mode with user_id
        self.voice_interface = VoiceInterface(user_id=self.user_id)

        # Track current mode and active threads
        self.current_mode = "Text"
        self.voice_thread = None
        
        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Mode switch button
        self.mode_button = tk.Button(self.root, text="Switch to Voice Mode", command=self.toggle_mode)
        self.mode_button.pack(pady=10)

        # Text mode components
        self.text_frame = tk.Frame(self.root)
        self.text_input = tk.Entry(self.text_frame, width=50)
        self.text_input.pack(side=tk.LEFT, padx=10)
        self.send_button = tk.Button(self.text_frame, text="Send", command=self.handle_text_input)
        self.send_button.pack(side=tk.LEFT)
        self.text_frame.pack()

        self.response_area = tk.Text(self.root, wrap="word", width=90, height=20, state="disabled")
        self.response_area.pack(pady=10)

        # Voice mode components (initially hidden)
        self.voice_frame = tk.Frame(self.root)
        self.voice_info_label = tk.Label(self.voice_frame, text="Voice mode is active. Speak to interact.")
        self.voice_info_label.pack(pady=10)
        self.start_voice_button = tk.Button(self.voice_frame, text="Start Voice Chat", command=self.start_voice_thread)
        self.start_voice_button.pack(pady=5)
        self.stop_voice_button = tk.Button(self.voice_frame, text="Stop Voice Chat", command=self.stop_voice_chat)
        self.stop_voice_button.pack(pady=5)

        # Document Management components
        self.doc_frame = tk.Frame(self.root)
        self.upload_button = tk.Button(self.doc_frame, text="Upload Document", command=self.upload_document)
        self.upload_button.pack(side=tk.LEFT, padx=10)
        self.view_docs_button = tk.Button(self.doc_frame, text="View Documents", command=self.view_documents)
        self.view_docs_button.pack(side=tk.LEFT, padx=10)
        self.doc_frame.pack(pady=10)

    def toggle_mode(self):
        # Toggle between Text and Voice modes
        if self.current_mode == "Text":
            self.switch_to_voice_mode()
        else:
            self.switch_to_text_mode()

    def switch_to_text_mode(self):
        # Switch to text mode, stopping any active voice sessions
        if self.voice_thread and self.voice_thread.is_alive():
            self.voice_interface.stop_event.set()  # Signal to stop the voice chat
            self.voice_thread.join()  # Wait for the thread to finish

        self.current_mode = "Text"
        self.mode_button.config(text="Switch to Voice Mode")
        self.voice_frame.pack_forget()
        self.text_frame.pack()
        self.display_response("Switched to Text Mode. You may start typing.")

    def switch_to_voice_mode(self):
        # Switch to voice mode, ensuring any text operations are stopped
        self.current_mode = "Voice"
        self.mode_button.config(text="Switch to Text Mode")
        self.text_frame.pack_forget()
        self.voice_frame.pack()
        self.display_response("Switched to Voice Mode. Click 'Start Voice Chat' to begin.")

    def handle_text_input(self):
        # Handle text input from the user in text mode
        user_input = self.text_input.get().strip()
        if not user_input:
            return
        self.display_response(f"You: {user_input}")
        response = self.theraxus_text.generate_response(user_input)
        self.display_response(f"Theraxus: {response}")
        self.text_input.delete(0, tk.END)

    def start_voice_thread(self):
        # Start voice chat in a separate thread to avoid GUI freezing
        self.voice_interface.stop_event.clear()  # Ensure the stop event is cleared
        self.voice_thread = Thread(target=self.start_voice_chat, daemon=True)
        self.voice_thread.start()

    def start_voice_chat(self):
        # Start voice chat session in voice mode
        try:
            self.display_response("Voice Chat Started. Speak after each response.")
            while not self.voice_interface.stop_event.is_set():
                # Transcribe user input
                user_input, success = self.voice_interface.stt.process_audio()
                if not success or not user_input.strip():
                    continue
                
                # Display user’s transcribed input
                self.display_response(f"You: {user_input}")
                
                # Generate AI response
                ai_response = self.theraxus_text.generate_response(user_input)
                
                # Display AI response in GUI
                self.display_response(f"Theraxus: {ai_response}")
                
                # Speak the response
                self.voice_interface.tts.speak(ai_response)

        except Exception as e:
            messagebox.showerror("Voice Chat Error", f"Failed to start voice chat: {e}")

    def stop_voice_chat(self):
        # Stop the voice chat session
        self.voice_interface.stop_event.set()
        if self.voice_thread and self.voice_thread.is_alive():
            self.voice_thread.join()  # Ensure the thread is fully stopped
        messagebox.showinfo("Voice Mode", "Voice chat stopped.")

    def upload_document(self):
        # Upload a document and add to the system
        file_path = filedialog.askopenfilename(title="Select a Document", filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
        if file_path:
            try:
                # Placeholder for actual document processing logic
                self.display_response(f"Document '{os.path.basename(file_path)}' uploaded successfully.")
                # Add actual logic here to integrate with DatabaseManager with user_id
                # Example: self.theraxus_text.db_manager.add_document(self.user_id, os.path.basename(file_path), content)
            except Exception as e:
                messagebox.showerror("Upload Error", f"Failed to upload document: {e}")

    def view_documents(self):
        # View available documents (placeholder logic)
        try:
            # Placeholder for document retrieval logic
            documents = self.theraxus_text.db_manager.get_documents(self.user_id)  # Retrieve documents for the user
            document_names = [doc for doc in documents.keys()]
            self.display_response("Available Documents: " + ", ".join(document_names))
        except Exception as e:
            messagebox.showerror("View Documents Error", f"Failed to retrieve documents: {e}")

    def display_response(self, text):
        # Display response in the text area
        self.response_area.config(state="normal")
        self.response_area.insert(tk.END, text + "\n")
        self.response_area.config(state="disabled")
        self.response_area.see(tk.END)

    def on_close(self):
        # Cleanup and exit
        self.stop_voice_chat()  # Ensure voice chat is stopped if closing during voice mode
        self.voice_interface.cleanup()  # Cleanup voice resources
        self.root.destroy()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    user_id = "default_user"  # Placeholder: This should be dynamically assigned or fetched
    app = TheraxusApp(root, user_id=user_id)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
