* * * * *

🤖✨ Theraxus AI 🚀
==================

Welcome to **Theraxus AI** - Your cutting-edge conversational AI companion, blending simplicity with powerful features to deliver an experience like no other! Whether it's chatting via text or voice, managing your documents, or using advanced **Retrieval-Augmented Generation (RAG)** capabilities, **Theraxus AI** has you covered. Dive in and explore a seamless, intelligent assistant designed to be highly functional, customizable, and super cool! 😎🌟

* * * * *

🌟 **Why Theraxus?** 💬
-----------------------

Because **Theraxus** isn't just an AI - it's **YOUR AI**. Built to run locally and supercharge your life, it's designed to keep you connected, informed, and entertained, all while offering powerful customization for developers and enthusiasts. Whether you want a **text buddy**, an **audio companion**, or a **knowledge retriever**, Theraxus is built to adapt to your needs. 💡

* * * * *

🔥 **Features** 🔥
------------------

-   **🗣️ Speech-to-Text (STT)**: Effortlessly convert spoken words to text with **OpenAI's Whisper**. Talk naturally; Theraxus listens. 🎤

-   **🗨️ Text-to-Speech (TTS)**: Want to hear your assistant's voice? With **pyttsx3**, Theraxus AI can read things back to you smoothly. 🗣️

-  ** Multi-User Profile**: Seamlessly switch and manage multiple user identities 👥 for a personalized and dynamic AI experience! 🔄

-   **📚 Document Management**:
    -   **Upload Documents**: Keep your files handy - add and manage text-based documents effortlessly.
    -   **View Summaries**: Get quick, **concise summaries** of your uploaded files.

-   **🔍 Retrieval-Augmented Generation (RAG)**: Turbocharge your assistant's responses by intelligently retrieving the most relevant content from your document repository. ⚙️📖

-   **📝 Chat History**: Keep track of your past conversations with **dedicated chat histories**, so you never miss a beat. 📜

-   **🔄 Modular and Customizable**: Everything's designed in modules for easy customization. **Add features, tweak behaviors**, or integrate new models - make Theraxus truly yours! 🔧🛠️

* * * * *

💻 **Get Started in Minutes!** ⏱️
---------------------------------

### Step 1️⃣: Clone the Repository

Start by grabbing **Theraxus AI**:

`git clone https://github.com/yourusername/theraxus
cd theraxus`

### Step 2️⃣: Set Up Your Virtual Environment 🌐

(Recommended) Create a virtual environment to keep everything neat:

`python -m venv venv`

Activate it with:

-   **Windows**: `venv\Scripts\activate`
-   **macOS/Linux**: `source venv/bin/activate`

### Step 3️⃣: Install Dependencies 🛠️

Theraxus relies on some system-level libraries:

-   **PortAudio**: Install using Chocolatey (`choco install portaudio`) for Windows, or Homebrew (`brew install portaudio`) for macOS. Use APT (`sudo apt-get install portaudio19-dev`) for Linux.
-   **libsndfile**: Same install path as **PortAudio** for each system.

Now, install Python dependencies:

`pip install -r requirements.txt`

### Step 4️⃣: Add the Required Models 📥

**LLaMA** and **Whisper** models are needed for full functionality:

-   Place **LLaMA models** (e.g. `.gguf`) in the `models/` directory.
-   **Whisper models** download automatically when you start using **STT**.

### Step 5️⃣: Launch Theraxus! 🚀

Choose between:

-   **Text-Based Chat**: `python runllm.py`
-   **Voice-Based Chat**: `python voice_runllm.py`

* * * * *
**Directory Structure
**

Theraxus/
├── config.py
├── database_manager.py
├── rag_optimizer.py
├── runllm.py
├── stt.py
├── tts.py
├── voice_runllm.py
├── requirements.txt
├── README.md
├── models/
│   └── **Yourmodel**
├── data/
│   ├── audio/
│   ├── docs/
│   ├── conversations/
│   ├── vector_db/
│   │   ├── index/
│   │   └── embeddings/
│   └── cache/
│       ├── whisper_models/
│       └── transformers_models/
├── logs/
│   └── theraxus.log
└── .gitignore

* * * * *

📝 **Usage Examples** 🚀
------------------------

### 💬 **Text Chat** Example:

`Welcome to Theraxus AI! Type 'exit' to quit.`

`You: load`
`Processing files... Added 'document1.txt'. Added 'document2.pdf`
`You: Explain this file to me`
`AI: Based on your input, here's a summary...`

### 🗣️ **Voice Chat** Example:

`Voice Interface Ready! Speak into your microphone.
Listening...
You: load [File selection dialog opens]
You: Sumaarize the file for me
AI: Based on your input, here's a summary...`

* * * * *

✨ **Customization & Extension** ✨
---------------------------------

**Theraxus AI** is built for **YOU** to customize! 🛠️ Add more TTS/STT features, swap **Models** without breaking the code choose, **Mistral**, **Gemma**, **LLama** or **Anymodel** for richer responses, expand the **RAG** capabilities - the sky's the limit! 🌌

Change configurations in `config.py`:

`STT_CONFIG = {
    'MODEL_NAME': 'small',  # Modify to 'small' or 'medium' for Whisper.
    'SAMPLE_RATE': 16000
}`

`TTS_CONFIG = {
    'RATE': 180,  # Faster speech rate
    'VOLUME': 0.8,  # Lower volume
}`

* * * * *

📊 **Logging & Debugging** 🛑
-----------------------------

Logs are stored in `logs/theraxus.log` 📂, where you can monitor everything happening under the hood. 🛠️

**Sample Log**:

`2024-04-27 15:30:45,123:INFO:Created new database file: data\conversations\conversations.json
2024-04-27 15:30:45,789:INFO:Generated response for input: Hello`

* * * * *

💡 **Contributing** 🤝
----------------------

I'd **love** for you to contribute! Make **Theraxus AI** even better. Fork it, add features, or report issues - let's build something amazing together! 🛠️

**How to Contribute**:

-   Fork the Project 🍴
-   Create a Feature Branch (`git checkout -b feature/AmazingFeature`) 🌱
-   Commit your Changes (`git commit -m 'Add some AmazingFeature'`) 💬
-   Push to the Branch (`git push origin feature/AmazingFeature`) 📤
-   Open a Pull Request 📨

* * * * *

📜 **License** 📜
-----------------

Distributed under the Apache License. See `LICENSE` for more information.

**📝 Note**: Please remember to credit Theraxus AI whenever you use or build on its capabilities. Sharing knowledge is caring! 🤗

* * * * *

🙏 **Acknowledgements** 🙏
--------------------------

Big shout-out to:

-   **OpenAI Whisper** for making STT possible. 🎙️
-   **pyttsx3** for TTS. 🗣️
-   **Llama** for Llama.cpp
-   **Hugging Face** for models
-   **hnswlib** for efficient document retrieval. 📚
-   **Sentence-Transformers** for meaningful sentence embeddings. 💡

* * * * *

✨ **Enjoy Theraxus AI!** 🚀💬🗣️✨
---------------------------------

Let's make your conversations smarter, your documents more accessible, and your AI experience truly awesome! 🥳
