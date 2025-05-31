# 🤖 Custom ChatBot

Build a custom chatbot powered by Large Language Models (LLMs) using your own knowledge base. This project enables **context-specific retrieval** for more accurate and relevant responses.

---

## 🧰 Features

- 🔍 Contextual Retrieval using your own content
- 🌐 Flask-based REST API server
- 🐳 Dockerized setup for easy deployment
- 🔐 API Key-based access to OpenAI or compatible models

---

## 📦 Getting Started

Follow the steps below to set up and run the chatbot locally using Docker.

---

### 1. Clone This Repository

```bash
git clone https://github.com/SadineniAbhi/CustomChatbot.git
cd CustomChatbot
```
---

### 2. Build the Docker Image

```bash
docker build -t custom-chatbot .
```
---
### 3. Run the Docker Container

Mount your own **text file** as a volume to provide custom context data that the chatbot can use for grounding responses:

```bash
docker run -d \
  -p 5000:5000 \
  -e OPENAI_API_KEY="your_openai_api_key" \
  -v /absolute/path/to/your/content.txt:/ChatBot/rag/content.txt \
  custom-chatbot
```
---

## 🌐 Access the API

Once running, the chatbot will be available at:


You can interact with it using HTTP requests (e.g., `curl`, Postman, or from a frontend app).



