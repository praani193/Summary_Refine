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
        current_node = self.graph.e_node
        execution_log = []

        iteration = 0

        while current_node != "end":
            iteration += 1
            if iteration > self.max_iter:
                execution_log.append({"error": "Max iterations reached"})
                break
            node_fn = self.graph.nodes[current_node]
            state = node_fn(state)
            execution_log.append({"node": current_node, "state": state.copy()})
            edge = self.graph.edges.get(current_node)
            if edge is None:
                break
            if callable(edge):
                current_node = edge(state)
            else:
                current_node = edge

        return {"final_state": state, "log": execution_log}
