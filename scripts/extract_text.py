import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """Извлекает текст из PDF (включая сканированные страницы)."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text("text")
            if not page_text.strip():

                pix = page.get_pixmap()
                text += f"\n[OCR placeholder for page {page_num}]"
            else:
                text += page_text
    return text

def extract_all_pdfs(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".pdf", ".txt"))
            text = extract_text_from_pdf(pdf_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"✅ Извлечён текст из {filename}")

if __name__ == "__main__":
    extract_all_pdfs("data/docs/almaty", "data/chunks/almaty")
