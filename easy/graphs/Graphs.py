class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self


def create_graph(data):
    nodes = {}

    # Create nodes
    for node_data in data["nodes"]:
        node = Node(node_data["value"])
        nodes[node_data["id"]] = node

    # Set children
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        for child_id in node_data["children"]:
            child_node = nodes[child_id]
            node.addChild(child_node)

    # Set start node

    return nodes.get(data["startNode"])

