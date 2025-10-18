import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

input_folder = "data/chunks/almaty"
output_path = "data/embeddings/almaty_embeddings.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

all_embeddings = []

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        for chunk in chunks:
            text = chunk["text"]
            embedding = model.encode(text).tolist()

            all_embeddings.append({
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "text": text,
                "embedding": embedding
            })

        print(f"✅ Processed: {filename}")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_embeddings, f, ensure_ascii=False, indent=2)

print(f"\n✅ All embeddings saved to: {output_path}")
