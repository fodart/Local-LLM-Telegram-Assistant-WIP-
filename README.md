# Local-LLM-Telegram-Assistant-WIP-
 A work-in-progress local AI assistant built around a self-hosted LLM, a Flask core service, and a Telegram bot interface.

 The project is focused on clean architecture, separation of concerns, and stability, rather than quick hacks.
 It is designed to be extended step by step into a more capable AI agent.

# ✨ Key Ideas

 **🧩 Decoupled architecture**

* Telegram bot acts only as a transport layer
 * Flask acts as the core logic / brain
 * LLM is accessed only through the core service

 **🧠 Local-first**
 
 * Uses a locally running LLM (via Ollama)
* No external AI APIs required

**🔁 Conversation memory**

* Per-chat session memory
* Context is explicitly managed and passed to the model

**⚙️ Async-safe Telegram handling**

* Long-running LLM requests do not block Telegram polling
* Background tasks are used for processing and replies

# 🏗️ Current Architecture
```
Telegram User
     ↓
Telegram Bot (async, lightweight)
     ↓ HTTP POST
Flask Core Service
     ↓
Local LLM (Ollama)
     ↓
Flask JSON response
     ↓
Telegram Bot sends reply
```

# 📦 Components

* Telegram Bot

  - Receives messages

  - Sends them to the core service

  - Delivers responses back to the user

* Flask Core

  - Handles message routing

  - Manages conversation sessions

  - Communicates with the local LLM

* LLM

  - Runs locally via Ollama

  - Can be swapped or extended
 
# 🚧 Project Status

**This project is under active development.**

**Implemented:**

* Basic Telegram ↔ Flask communication
* Local LLM integration
* Per-chat memory (in-memory)
* Async-safe message processing

**Planned / in progress:**
* Better memory management (limits, reset, persistence)
* Action / tool execution layer
* Multiple interaction modes (chat vs actions)
* Improved error handling and logging
* Optional web or CLI interface

# ⚠️ Notes

* This is not a production-ready system yet.
* In-memory sessions will reset on restart.
* APIs and internal structure may change.

# 🎯 Goals

The long-term goal is to evolve this project into a flexible local AI agent core that can be connected to different interfaces (Telegram, web, CLI) while keeping the core logic isolated and testable.

# 📄 License

**MIT**
