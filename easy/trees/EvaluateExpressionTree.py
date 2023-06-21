import BinaryTree

#time O(n)
#space O(n)
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    leftVal = evaluateExpressionTree(tree.left)
    rightVal = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftVal + rightVal
    if tree.value == -2:
        return leftVal - rightVal

    if tree.value == -3:
        return int(leftVal / rightVal)
    return leftVal * rightVal

tree = BinaryTree.create_binary_tree({"nodes": [{"id": "1", "left": "2", "right": "3", "value": -1},
                                                {"id": "2", "left": None, "right": None, "value": 2},
                                                {"id": "3", "left": None, "right": None, "value": 3}], "root": "1"})

BinaryTree.display_binary_tree(tree)

expression_tree = evaluateExpressionTree(tree)
print(expression_tree)
