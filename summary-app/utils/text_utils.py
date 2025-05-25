def split_text_into_chunks(text, max_length=3000, overlap=200):
    """
    長文テキストを指定した最大長さでチャンクに分割する関数。
    チャンク間は重複部分を設けて文脈のつながりを維持する。

    Args:
        text (str): 分割対象のテキスト
        max_length (int): 1チャンクあたりの最大文字数（デフォルト3000）
        overlap (int): チャンク間で重複する文字数（デフォルト200）

    Returns:
        list[str]: 分割後のテキストチャンクのリスト
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + max_length, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        # 次のチャンク開始位置はmax_lengthからoverlap分戻すことで重複を作る
        start += max_length - overlap

    return chunks
