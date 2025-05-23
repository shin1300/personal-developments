def split_text_into_chunks(text, max_length=3000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_length, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += max_length - overlap  # 少し重複させて文脈維持
    return chunks
