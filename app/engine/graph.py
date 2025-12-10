class Graph:
    def __init__(self, nodes: dict, edges: dict, e_node: str):
        self.nodes = nodes
        self.edges = edges
        self.e_node = e_node


class Runner:
    def __init__(self, graph, iters: int = 10):
        self.graph = graph
        self.max_iter = iters

    def run(self, ini_state: dict):
        state = ini_state
        curr = self.graph.e_node
        log = []

        iteration = 0

        while curr != "end":
            iteration += 1
            if iteration > self.max_iter:
                log.append({"error": "Max iterations reached"})
                break
            node_fn = self.graph.nodes[curr]
            state = node_fn(state)
            log.append({"node": curr, "state": state.copy()})
            edge = self.graph.edges.get(curr)
            if edge is None:
                break
            if callable(edge):
                curr = edge(state)
            else:
                curr = edge

        return {"final_state": state, "log": log}
