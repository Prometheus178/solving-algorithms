import LinkedList


# find middle of linked list if between 2 nums return greater one

# time O(n)
# space O(1)
def middleNode(linkedList):
    count = 0
    cur = linkedList
    while cur.next is not None:
        count += 1
        cur = cur.next
    mid_node = linkedList
    for _ in range(count // 2):
        mid_node = mid_node.next

    if count % 2 == 0:
        return mid_node
    return mid_node.next



data = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "1-3", "value": 7},
        {"id": "1-3", "next": "2", "value": 3},
        {"id": "2", "next": None, "value": 5}
    ]
}
head = LinkedList.create_linked_list(data)
print(middleNode(head).value)
data1 = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "1-3", "value": 7},
        {"id": "1-3", "next": None, "value": 3},
    ]
}
head1 = LinkedList.create_linked_list(data1)
print(middleNode(head1).value)
