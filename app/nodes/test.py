from app.engine.graph import Graph, Runner
from split import split_text
from summarize import summarize_chunks
from summarize import merge_summaries
from refine_summary import refine_summary
from refine_edge import refine_edge

graph = Graph(
    nodes={
        "split_text": split_text,
        "summarize_chunks": summarize_chunks,
        "merge_summaries": merge_summaries,
        "refine_summary": refine_summary
    },
    edges={
        "split_text": "summarize_chunks",
        "summarize_chunks": "merge_summaries",
        "merge_summaries": "refine_summary",
        "refine_summary": refine_edge
    },
    e_node="split_text"
)
runner = Runner(graph)
initial_state = {
    "text": "This is a long text that we want to summarize. "
            "It contains multiple sentences with important information.",
    "chunk_size": 5,
    "max_length": 15
}

result = runner.run(initial_state)

print("Final Summary:\n", result["final_state"])
print("\nExecution Log:")
for log in result["log"]:
    print(log)
