from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from app.engine.graph import Graph, Runner
from app.nodes.split import split_text
from app.nodes.summarize import summarize_chunks, merge_summaries
from app.nodes.refine_summary import refine_summary
from app.nodes.refine_edge import refine_edge
from app.memory.memory import load_graphs, save_graphs, load_runs, save_runs

app = FastAPI(title="Option B - Summary Refinement Engine")
graphs = load_graphs()
runs = load_runs()


def next_graph_id():
    return str(len(graphs) + 1)


def build_summary_graph():
    return Graph(
        nodes={
            "split_text": split_text,
            "summarize_chunks": summarize_chunks,
            "merge_summaries": merge_summaries,
            "refine_summary": refine_summary,
        },
        edges={
            "split_text": "summarize_chunks",
            "summarize_chunks": "merge_summaries",
            "merge_summaries": "refine_summary",
            "refine_summary": refine_edge
        },
        e_node="split_text",
    )


@app.get("/", response_class= PlainTextResponse)
def home():
    return ("Welcome to the Summary Refinement Workflow Engine.\n\n"
            "A 'graph' is a workflow that defines how text is processed. "
            "You can create a graph once and reuse it many times.\n\n"
            "Every time you execute a graph, a new 'run' is created. "
            "A run stores the input, the output, and all intermediate states.\n\n"
            "Graphs define the workflow. "
            "Runs record the execution of that workflow.\n\n"
            "Use this engine to create graphs, run them, and retrieve refined summaries.")


@app.post("/graphs/create")
def create_graph():
    graph_id = next_graph_id()
    graphs[graph_id] = {
        "type": "summary_refinement",
        "run_counter": 0
    }
    save_graphs(graphs)
    return {"graph_id": graph_id}


@app.post("/graphs/{graph_id}/graph_run")
def run_graph(graph_id: str, payload: dict):
    if graph_id not in graphs:
        return {"error":"Graph not found"}
    graph_obj = build_summary_graph()
    runner = Runner(graph_obj)
    run_number = graphs[graph_id]["run_counter"]
    graphs[graph_id]["run_counter"] += 1
    save_graphs(graphs)

    run_id = f"{graph_id}-{run_number}"
    result = runner.run(payload)
    runs[run_id] = {
        "graph_id": graph_id,
        "run_number": run_number,
        "result": result
    }
    save_runs(runs)

    return {
        "run_id": run_id,
        "graph_id": graph_id,
        "run_number": run_number,
        "result": result
    }


@app.get("/graphs")
def list_graphs():
    return graphs


@app.get("/graphs/{graph_id}")
def get_graph(graph_id: str):
    return graphs.get(graph_id, {"error":"Graph not found"})


@app.get("/runs")
def list_runs():
    return runs


@app.get("/runs/{run_id}")
def get_run(run_id: str):
    return runs.get(run_id, {"error":"Run not found"})

@app.get("/runs/{run_id}/final_result")
def get_result(run_id: str):
    if run_id not in runs:
        return {"error":"Run not found"}
    run_item = runs.get(run_id)
    run_result = run_item.get("result")
    run_final_state = run_result["final_state"]
    return run_final_state
