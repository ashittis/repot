from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


def load_and_split(repo_path):
    allowed_exts = (".py", ".md", ".txt", ".json", ".rst")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(allowed_exts):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                        splits = splitter.split_text(text)
                        for chunk in splits:
                            documents.append(
                                Document(
                                    page_content=chunk,
                                    metadata={
                                        "source": os.path.relpath(file_path, repo_path)
                                    },
                                )
                            )
                except Exception as e:
                    print(f"[!] Skipped {file_path}: {e}")
                    continue

    return documents
