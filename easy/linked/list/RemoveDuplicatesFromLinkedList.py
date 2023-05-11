# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


data = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6}
    ]
}


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


head = create_linked_list(data)

def removeDuplicatesFromLinkedList(linkedList):
    cur = head
    while cur.next is not None:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return linkedList


linked_list = removeDuplicatesFromLinkedList(head)
iterate_linked_list(linked_list)
