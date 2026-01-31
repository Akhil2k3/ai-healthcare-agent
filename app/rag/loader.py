from pathlib import Path

def load_documents(data_dir: str):
    documents = []

    for file_path in Path(data_dir).glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append({
            "text": text,
            "source": file_path.name
        })

    return documents