import json
import os

base = "app/memory"
graph_file = f"{base}/graphs.json"
runs_file = f"{base}/runs.json"


def _load(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def _save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def load_graphs():
    return _load(graph_file)


def save_graphs(graphs):
    _save(graph_file, graphs)


def load_runs():
    return _load(runs_file)


def save_runs(runs):
    _save(runs_file, runs)
