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

data3 = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 2},
        {"id": "1-3", "next": "2", "value": 3},
        {"id": "2", "next": "3", "value": 4},
        {"id": "3", "next": "3-2", "value": 5},
        {"id": "3-2", "next": "3-3", "value": 6},
        {"id": "3-3", "next": "4", "value": 7},
        {"id": "4", "next": None, "value": 8}
    ]
}
head3 = LinkedList.create_linked_list(data3)

# slow and fast pointers technic
# time O(n)
# space O(1)
def middleNode2(linkedList):
    slow = linkedList
    fast = linkedList
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

print(middleNode2(head3).value)