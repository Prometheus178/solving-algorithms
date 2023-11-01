class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            elem = queue.pop(0)
            array.append(elem.name)
            if len(elem.children) > 0:
                for child in elem.children:
                    queue.append(child)
        return array

{
    "graph": {
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
}

nodeA = Node("A")

nodeA.addChild("B")
nodeA.addChild("C")
nodeA.addChild("D")

nodeB = nodeA.children[0]
nodeB.addChild("E")
nodeB.addChild("F")

nodeD = nodeA.children[2]
nodeD.addChild("G")
nodeD.addChild("H")

nodeF = nodeB.children[1]
nodeF.addChild("I")
nodeF.addChild("J")

nodeG = nodeD.children[0]
nodeG.addChild("K")

visited = list()

res = Node.breadthFirstSearch(nodeA, visited)
print(res)
