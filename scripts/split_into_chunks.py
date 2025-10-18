import os
import json

input_folder = "data/text/almaty"
output_folder = "data/chunks/almaty"
os.makedirs(output_folder, exist_ok=True)

def split_text(text, max_words=300):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i+max_words])

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = list(split_text(text))
        output_data = []
        for i, chunk in enumerate(chunks):
            output_data.append({
                "source": filename,
                "chunk_id": i,
                "text": chunk
            })

        output_path = os.path.join(output_folder, filename.replace(".txt", "_chunks.json"))
        with open(output_path, "w", encoding="utf-8") as out:
            json.dump(output_data, out, ensure_ascii=False, indent=2)

        print(f"✅ Created chunks: {output_path}")

print("\n✅ All text files processed successfully!")
