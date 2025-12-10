def summarize_chunks(state):
    summaries = []
    for chunk in state.get("chunks", []):
        words = chunk.split()
        summary = " ".join(words[:10])
        summaries.append(summary)

    state["summaries"] = summaries
    return state

def merge_summaries(state):
    state["final_summary"] = " ".join(state.get("summaries", []))
    return state
