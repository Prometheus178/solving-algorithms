import BinaryTree


# time O(N)
# space O(N)
def branchSums(nodes):
    res = []
    calculateBranchSum(nodes, 0, res)
    return res


def calculateBranchSum(nodes, counter, res):
    count = counter + nodes.value
    if nodes.left is None and nodes.right is None:
        res.append(count)
        return
    calculateBranchSum(nodes.left, count, res)
    if nodes.right is not None:
        calculateBranchSum(nodes.right, count, res)


root = {
    "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": "10", "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9},
        {"id": "10", "left": None, "right": None, "value": 10}
    ],
    "root": "1"
}

tree = BinaryTree.create_binary_tree(root)
print(branchSums(tree))
