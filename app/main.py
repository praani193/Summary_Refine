from fastapi import FastAPI
from uuid import uuid4

from app.engine.graph import Graph, Runner
from app.nodes.split import split_text
from app.nodes.summarize import summarize_chunks,merge_summaries
from app.nodes.refine_summary import refine_summary
from app.nodes.refine_edge import refine_edge

app = FastAPI(title="Summary Refinement Workflow Engine")

# In-memory stores
GRAPHS = {}
RUNS = {}


def build_summary_graph():
    """
    Creates a predefined summarization + refinement workflow.
    """
    return Graph(
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


@app.post("/graph/create")
def create_graph():
    """
    Creates a new workflow graph.
    (Currently maps to a predefined workflow.)
    """
    graph_id = str(uuid4())
    GRAPHS[graph_id] = build_summary_graph()
    return {"graph_id": graph_id}


@app.post("/graph/run")
def run_graph(payload: dict):
    """
    Runs the summarization workflow with initial state.
    """
    graph = build_summary_graph()
    runner = Runner(graph)

    run_id = str(uuid4())
    result = runner.run(payload)

    RUNS[run_id] = result

    return {
        "run_id": run_id,
        "result": result
    }


@app.get("/graph/state/{run_id}")
def get_run_state(run_id: str):
    """
    Returns execution state for a given run.
    """
    return RUNS.get(run_id, {"error": "Run not found"})
