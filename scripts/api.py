from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from numpy.linalg import norm

app = FastAPI(title="RCA — Almaty Semantic Search API")

# Загружаем эмбеддинги и модель
with open("data/embeddings/almaty_embeddings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

# Преобразуем эмбеддинги в numpy для быстрого сравнения
embeddings = np.array([np.array(item["embedding"]) for item in data])

class Answer(BaseModel):
    question: str
    answer: str
    sources: list

def search_similar(query, top_k=3):
    query_vec = model.encode(query)
    scores = np.dot(embeddings, query_vec) / (norm(embeddings, axis=1) * norm(query_vec))
    best_idx = np.argsort(scores)[::-1][:top_k]
    results = []
    for i in best_idx:
        item = data[i]
        results.append({
            "source": item["source"],
            "text": item["text"][:500] + "..."
        })
    return results

@app.get("/ask", response_model=Answer)
def ask(question: str = Query(..., description="Введите вопрос")):
    results = search_similar(question)
    answer_text = " ".join([r["text"] for r in results])
    return {
        "question": question,
        "answer": answer_text,
        "sources": results
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
