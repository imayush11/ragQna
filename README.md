# 🧠 LLM-Based Query Engine

This repository showcases a powerful **LLM-based Query Engine** built using `llama-index`, **StableLM** from Hugging Face, and a **vector store index** for efficient document querying. 📝💡

## 🚀 Project Structure

Here’s how the project is organized for maintainability and ease of use:

```bash
|── data/                      # 📂 Folder containing the documents to query (includes a demo.pdf).
|   |── demo.pdf               # 🎯 Example document for testing the query system.
|
|── query_engine/               # 📦 Folder containing modules to manage the query system.
|   |── __init__.py             # 🛠️ Makes this folder a Python package.
|   |── document_loader.py      # 📄 Handles document loading from the data folder.
|   |── llm_service.py          # 🔧 Manages the LLM configuration and settings.
|   |── index_manager.py        # 📊 Manages the creation and querying of the index.
|   |── query_interface.py      # 💬 Handles user interaction for querying the system.
|
|── your_script.py              # 🎬 Entry point script to initialize and run the query engine.
|
|── README.md                   # 📖 Documentation file.


## ✨ Features
🗂️ Document Loader: Automatically loads all files from the data/ directory and prepares them for querying.
🤖 LLM Integration: Uses Hugging Face’s StableLM for advanced language model querying.
🔍 Vector Store Index: Implements a vector-based index for optimized search.
🔄 Interactive Query Loop: Allows users to query documents interactively until they choose to exit.

## 🛠️ How It Works
The engine uses documents from the data/ folder to create an index, allowing users to ask questions based on the content of those documents. The LLM (Language Model) provides answers using the indexed data.

1) document_loader.py loads all documents into the system.
2) llm_service.py configures the StableLM model for queries.
3) index_manager.py creates a vector store index for efficient searching.
4) query_interface.py handles user input, facilitating an interactive querying experience.

## 🏃 How to Run
1) Clone the repository and install dependencies:

```
git clone https://github.com/imayush11/rag-qna.git
```
```
cd rag-qna
```
pip install -r requirements.txt
```

2) Add your documents to the data/ folder (a sample document ./data/qna_1.pdf is already provided).

3) Run the script to start querying:

```
python qna.py
```

4) Start querying: Type your questions when prompted and receive answers based on the loaded documents! 🎤🧠 To exit the query loop, simply type quit.

## 🤝 Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please feel free to submit issues or pull requests. Your input is valuable for improving the project!

