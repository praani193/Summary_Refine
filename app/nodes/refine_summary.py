def refine_summary(state):
    summary = state.get("final_summary", "")
    max_length = state.get("max_length", 30)

    words = summary.split()
    if len(words) > max_length:
        words = words[:max_length]

    state["final_summary"] = " ".join(words)
    return state
