def split_text(state):
    text = state.get("text", "")
    cs = state.get("chunk_size", 50)

    words = text.split()
    chunks = []

    for i in range(0, len(words), cs):
        chunk = " ".join(words[i:i + cs])
        chunks.append(chunk)

    state["chunks"] = chunks
    return state
