class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def __repr__(self):
        return "name " + self.name

    # def __repr__(self):
    #     children_str = ', '.join(repr(child) for child in self.children)
    #     return f"Node(name='{self.name}', children=[{children_str}])"


# time O(n)
# space O(n)

# Implementation of Depth First Search method on the Node class, which takes in an empty array, traverses the tree
# using depth first search, storing the nodes visited in the array and returning the array
def depthFirstSearch(self, array):
    array.append(self.name)
    if len(self.children) == 0:
        return array

    for x in self.children:
        depthFirstSearch(x, array)
    return array


data = {
    "nodes": [
        {"children": ["B", "C", "D"], "id": "A", "value": "A"},
        {"children": ["E", "F"], "id": "B", "value": "B"},
        {"children": [], "id": "C", "value": "C"},
        {"children": ["G", "H"], "id": "D", "value": "D"},
        {"children": [], "id": "E", "value": "E"},
        {"children": ["I", "J"], "id": "F", "value": "F"},
        {"children": ["K"], "id": "G", "value": "G"},
        {"children": [], "id": "H", "value": "H"},
        {"children": [], "id": "I", "value": "I"},
        {"children": [], "id": "J", "value": "J"},
        {"children": [], "id": "K", "value": "K"}
    ],
    "startNode": "A"
}
nodeA = Node("A")

nodeB = nodeA.addChild("B")
nodeA.addChild("C")
nodeB.addChild("E")
nodeF = nodeB.addChild("F")
nodeF.addChild("I")
nodeF.addChild("J")

nodeD = nodeA.addChild("D")
nodeD.addChild("H")
nodeG = nodeD.addChild("G")
nodeG.addChild("K")

visited = list()

res = depthFirstSearch(nodeA, visited)
print(res)
