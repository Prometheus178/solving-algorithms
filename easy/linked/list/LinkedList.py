class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(data):
    # Create nodes
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Set next pointers
    for node_data in data["nodes"]:
        if node_data["next"]:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    # Set head
    head = nodes[data["head"]]

    return head


def iterate_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next
