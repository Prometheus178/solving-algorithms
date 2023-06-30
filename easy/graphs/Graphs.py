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
    start_node = nodes[data["startNode"]]

    return start_node



def display_graph(start_node):
    def display_helper(node, level):
        print("    " * level + "|-- " + str(node.name))

        for child in node.children:
            display_helper(child, level + 1)

    display_helper(start_node, 0)
