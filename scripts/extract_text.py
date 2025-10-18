import os
import fitz  # PyMuPDF

input_folder = "data/docs/almaty"
output_folder = "data/text/almaty"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        text_path = os.path.join(output_folder, filename.replace(".pdf", ".txt"))

        print(f"🔹 Extracting: {filename}")
        text = ""

        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text")

        with open(text_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Saved: {text_path}")

print("\n✅ All PDFs processed successfully!")
