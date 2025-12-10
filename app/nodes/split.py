def split_text(state):
    text = state.get("text", "")
    cs = state.get("chunk_size", 50)

    words = text.split()
    for i in range(0, len(words),cs):
        chunks = [" ".join(words[i:i+cs])]
    state["chunks"] = chunks

    return state
