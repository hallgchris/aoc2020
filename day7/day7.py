from enum import Enum, auto
import os
import string
import networkx as nx

class State(Enum):
    FIRST_COLOUR = auto(),
    FIRST_DESC = auto(),
    FIRST_BAG = auto(),
    COLOUR = auto(),
    DESC = auto(),
    BAG = auto(),
    CONTAIN = auto(),
    NUMBER = auto(),
    FINAL = auto(),

def parse_line(line: str):
    tokens = line.strip() \
        .translate(str.maketrans("", "", string.punctuation)) \
        .split(" ")
    bag = ""
    contents = []
    contents_qty = []
    state: State = State.FIRST_DESC
    for token in tokens:
        if state == State.FINAL:
            break
        elif state == State.FIRST_DESC:
            bag += token
            state = State.FIRST_COLOUR
        elif state == State.FIRST_COLOUR:
            bag += " " + token
            state = State.FIRST_BAG
        elif state == State.FIRST_BAG:
            state = State.CONTAIN
        elif state == State.CONTAIN:
            state = State.NUMBER
        elif state == State.NUMBER:
            if token == "no":
                state = State.FINAL
            else:
                contents_qty.append(int(token))
                state = State.DESC
        elif state == State.DESC:
            contents.append(token)
            state = State.COLOUR
        elif state == state.COLOUR:
            contents[-1] += " " + token
            state = State.BAG
        elif state == state.BAG:
            state = State.NUMBER
    return bag, contents, contents_qty

def bfs_product(graph: nx.DiGraph, node: str):
    sum = 0
    for succ in graph.successors(node):
        sum += G.get_edge_data(node, succ)["weight"] * (bfs_product(graph, succ) + 1)
    return sum

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file = os.path.join(script_dir, "input.txt")

    nodes = []
    contains_edges = []
    contained_by_edges = []

    with open(input_file) as file:
        for line in file:
            bag, contents, contents_qty = parse_line(line)
            nodes.append(bag)
            for i in range(len(contents)):
                edge_attributes = {"weight": contents_qty[i]}
                contains_edges.append((bag, contents[i], edge_attributes))
                contained_by_edges.append((contents[i], bag, edge_attributes))

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(contained_by_edges)

    print("Number of bags containing the shiny gold bag:", len(nx.descendants(G, "shiny gold")))

    G.clear_edges()
    G.add_edges_from(contains_edges)

    shiny_gold_contents = bfs_product(G, "shiny gold")
    print("Number of bags in a shiny gold bag:", shiny_gold_contents)
