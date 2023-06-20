import BinaryTree


# time O(N)
# space O(N)
def depths(root, store, count):
    count = count + 1
    if root.left is not None:
        store.update({root.value: count})
        depths(root.left, store, count)
    if root.right is not None:
        store.update({root.value: count})
        depths(root.right, store, count)
    if root.left is None and root.right is None:
        store.update({root.value: count})
        return


def nodeDepths(root):
    # Write your code here.
    depth = {}
    if root.left is not None:
        depths(root.left, depth, 0)
    if root.right is not None:
        depths(root.right, depth, 0)
    sumDepth = 0
    for x in depth.values():
        sumDepth = sumDepth + x
    return sumDepth


tree = BinaryTree.create_binary_tree({"nodes": [{"id": "1", "left": "2", "right": "3", "value": 1},
                                                {"id": "2", "left": "4", "right": "5", "value": 2},
                                                {"id": "3", "left": "6", "right": "7", "value": 3},
                                                {"id": "4", "left": "8", "right": "9", "value": 4},
                                                {"id": "5", "left": None, "right": None, "value": 5},
                                                {"id": "6", "left": None, "right": None, "value": 6},
                                                {"id": "7", "left": None, "right": None, "value": 7},
                                                {"id": "8", "left": None, "right": None, "value": 8},
                                                {"id": "9", "left": None, "right": None, "value": 9}], "root": "1"})

BinaryTree.display_binary_tree(tree)
print(nodeDepths(tree))
