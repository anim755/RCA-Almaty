# Regulatory Clarity Agent (RCA) — Almaty MVP
**The purpose of the project:**  
Make an understandable tool for quickly searching for rules and permits in official documents of the city of Almaty.
**What does RCA do:**  
- Finds the necessary regulatory texts from a PDF (for example, how to get permission for reconstruction).  
- Explains them in simple words.  
- Shows the source: document, page, and quote.
**MVP focus:**  
The city of Almaty — permits for construction and reconstruction.
**Current documents (folder `data/docs/almaty'):**
- _gluster_2021_12_7_ab931a0c7d593e8445197da7001036b6_original.16487 (1).pdf
- _gluster_2022_9_12_2d126f4d495351c44faaf79d51f54d88_original.3981909.pdf
- 4e6f7656b96d7ba736e4ec71d3b64328_original.292507.pdf
- sbornik_kr_stola_cpm_2_marta_2017.pdf
- v23r0001736.22-08-2023.rus.pdf
- v23r0001751.29-12-2023.rus.pdf
- v24r0179702.25-12-2024.rus.pdf
- Appendix 1 to the Administrative Regulations.pdf
**Next development steps:**  
1. Add a script for reading PDF and splitting text into chunks.
2. Generate embeddings and build a meaning search (FAISS).  
3. Create the API `/ask` (FastAPI) — returns the response + source.  
4. Make a simple interface: question → answer + quotes.
**Contact:**  
Danyal Bauyrzhan — +77471125085 , danyal.bauyrzhan28@fizmat.kz

