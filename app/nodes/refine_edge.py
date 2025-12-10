def refine_edge(state):
    if len(state.get("final_summary", "").split()) <= state.get("max_length", 30):
        return "end"
    return "refine_summary"
