class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_binary_tree(data):
    nodes = {}

    # Create nodes
    for node_data in data["nodes"]:
        node = BinaryTree(node_data["value"])
        nodes[node_data["id"]] = node

    # Set left and right pointers
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"]:
            node.left = nodes[node_data["left"]]
        if node_data["right"]:
            node.right = nodes[node_data["right"]]

    # Set root
    root = nodes[data["root"]]

    return root


def display_binary_tree(root):
    def display_helper(node, level):
        if node is None:
            return

        display_helper(node.right, level + 1)
        print("    " * level + str(node.value))
        display_helper(node.left, level + 1)

    display_helper(root, 0)
