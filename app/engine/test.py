from graph import Graph,Runner
def node_a(state):
    state["value"] = state.get("value", 0) + 1
    print("node_a executed, value =", state["value"])
    return state

def node_b(state):
    state["value"] *= 2
    print("node_b executed, value =", state["value"])
    return state

def loop_edge(state):
    if state["value"] >= 10:
        return "end"
    return "node_a"


graph = Graph(
    nodes={
        "node_a": node_a,
        "node_b": node_b
    },
    edges={
        "node_a": "node_b",
        "node_b": loop_edge
    },
    e_node="node_a"
)

runner = Runner(graph)
initial_state = {"value": 1}
result = runner.run(initial_state)

print("\nFinal State:", result["final_state"])
print("\nExecution Log:")
for log in result["log"]:
    print(log)

