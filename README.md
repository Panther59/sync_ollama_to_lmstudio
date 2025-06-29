# Ollama to LM Studio Model Sync Tool

This Python script allows you to synchronize large language model (LLM) files from your local [Ollama](https://ollama.com) cache into a format compatible with [LM Studio](https://lmstudio.ai). Instead of duplicating files, it creates symbolic links to avoid unnecessary disk usage.

---

## 🔧 What It Does

- Reads `latest` manifest files from Ollama's local model registry.
- Extracts model metadata (user, model name, tag, digest).
- Finds the associated model blob from Ollama’s storage.
- Creates symbolic links (symlinks) to these blobs in a new directory layout for LM Studio.
- Cleans and prepares the target directory every time it's run.

---

## 📂 Example Directory Structure

**Ollama Base Directory (input):**
```
F:/ollama_models/
├── blobs/
│ └── sha256-abc123...
├── manifests/
│ └── registry.ollama.ai/
│ └── user/model/tag/latest
```

**LM Studio Target Directory (output):**
```
F:/Models/llm_studio/
└── user/
│ └── model/
│   └── model-abc123... (symlink to blob)
```

---

## ⚙️ Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux
- On **Windows**, symbolic link creation may require admin privileges or Developer Mode enabled

---

## 🚀 How to Use

1. Make sure Ollama has downloaded models to a known location (e.g., `F:/ollama_models`).
2. Save the Python script (`sync_ollama_to_lmstudio.py`) locally.
3. Open a terminal or command prompt.
4. Run the script:

   ```bash
   python sync_ollama_to_lmstudio.py

5. When prompted, enter:

Base Ollama model directory (e.g. F:/ollama_models)

Target LM Studio directory (e.g. F:/Models/llm_studio)

## ⚠️ Notes
All existing contents in the LM Studio target directory will be deleted before syncing.

If a model's blob file is not found, a warning will be printed.

Symbolic links improve efficiency but may behave differently on cloud drives or restricted folders.

## 📄 License
MIT License — Free to use, modify, and share.

## 🤝 Contributing
Feel free to open issues or pull requests if you'd like to improve this tool!

---

Let me know if you want this saved as a downloadable `README.md` file or added alongside the Python script!
