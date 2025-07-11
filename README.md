# 🤖 Repot — Chat with Any GitHub Repository

GitHubRepoChat is a local, offline, containerizable LLM-powered app that lets you **chat with any GitHub repository** using **LangChain**, **Llama.cpp**, and **Mistral-7B**. Paste a repo URL, and it downloads, indexes, and allows natural language Q&A about the codebase.

It supports **offline inference**, making it lightweight, fast, and private — ideal for local developers, auditors, or students learning new codebases.

![Screenshot 1](https://github.com/ashittis/repot/blob/main/Screenshot%202025-07-11%20191020.png) 
![Screenshot 2](https://github.com/ashittis/repot/blob/main/Screenshot%202025-07-11%20191613.png)

---

## 🔖 Table of Contents

- [✨ Features](#-features)
- [🧠 How It Works](#-how-it-works)
- [🛠️ Tech Stack](#-tech-stack)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📸 Screenshots](#-screenshots)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## ✨ Features

- 🧠 **Chat with any GitHub repo** using natural language
- 🧾 **LangChain + Llama.cpp** backed local LLM chat engine
- 📦 **Supports Mistral-7B Instruct Q4 GGUF**
- 📂 Automatically clones + parses `.py`, `.md`, `.txt`, `.rst` files
- 📚 Displays indexed document sources and vectorstore size
- 💬 Includes built-in test query ("What is this repo about?")
- ⚡ **Works locally without internet** once setup
- 🎛️ Lightweight Streamlit UI
  
---

## 🧠 How It Works

1. Paste a GitHub repo URL.
2. App clones the repo to `data/downloaded_repos/`
3. Files are parsed, chunked, and indexed with FAISS
4. A **ConversationalRetrievalChain** is set up using LangChain
5. Your queries are answered using a local LLM (e.g., Mistral-7B)

---

## 🛠️ Tech Stack

**Frontend**

- Streamlit
- Python
- Minimal dark theme

**Backend / LLM**

- LangChain
- LlamaCpp (Mistral-7B-instruct GGUF)
- FAISS vector store
- HuggingFace Tokenizers
- dotenv for env vars

**DevOps**

- Docker (WIP)
- Logging with custom folder
- Modular `utils/` structure

---

## 📦 Installation (Local)

> Requires: Python 3.10+, `pip`, and a quantized GGUF model like Mistral

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/githubrepochat.git
cd githubrepochat

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place your quantized model
# Put mistral-7b-instruct-v0.1.Q4_0.gguf inside models/

# 5. Run the app
streamlit run app.py
````

---

## 🚀 Usage

1. Paste a GitHub repo URL like:

   ```
   https://github.com/karpathy/micrograd
   ```

2. App will download and index the repo files.

3. Once indexed, you’ll see:

   * Loaded documents
   * Vectorstore size
   * Answer to "What is this repo about?"

4. Then ask your own questions like:

   * "What does `engine.py` do?"
   * "How is backpropagation implemented?"
   * "List the key functions used in training"

---

## 📸 Screenshots

![Indexing](https://github.com/ashittis/repot/blob/main/Screenshot%202025-07-11%20191820.png)
![Chat](https://github.com/ashittis/repot/blob/main/Screenshot%202025-07-11%20192107.png)

---
---

## 📬 Contact

For questions, collaboration or feedback:

* 🧑‍💻 **Author**: Akash Subramanian
* 📧 **Email**: [iamakashsubramanian@gmail.com](mailto:iamakashsubramanian@gmail.com)
* 🌐 **GitHub**: [ashittis](https://github.com/ashittis)

```
