import BinaryTree


def findClosestValue(tree, target, closest_nums):
    if not closest_nums:
        closest_nums.append(tree.value)
    diff = abs(tree.value - target)
    closest_diff = abs(closest_nums[0] - target)

    if diff < closest_diff:
        closest_nums[0] = tree.value

    if tree.left is not None:
        findClosestValue(tree.left, target, closest_nums)
    if tree.right is not None:
        findClosestValue(tree.right, target, closest_nums)
    if tree.left is None and tree.right is None:
        return


# time O(n)
# space O(n)
def findClosestValueInBst(nodes, target):
    closest_nums = []
    findClosestValue(nodes, target, closest_nums)
    return closest_nums[0]


tree = BinaryTree.create_binary_tree({"nodes": [{"id": "10", "left": "5", "right": "15", "value": 10},
                                                {"id": "15", "left": "13", "right": "22", "value": 15},
                                                {"id": "22", "left": None, "right": None, "value": 22},
                                                {"id": "13", "left": None, "right": "14", "value": 13},
                                                {"id": "14", "left": None, "right": None, "value": 14},
                                                {"id": "5", "left": "2", "right": "5-2", "value": 5},
                                                {"id": "5-2", "left": None, "right": None, "value": 5},
                                                {"id": "2", "left": "1", "right": None, "value": 2},
                                                {"id": "1", "left": None, "right": None, "value": 1}], "root": "10"})

print(findClosestValueInBst(tree, 12))
