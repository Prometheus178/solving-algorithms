import Graphs


def dfs(node, array, visited):
    array.append(node.name)
    children = node.children
    for ch in children:
        visited.append(ch)
    if len(visited) != 0:
        nextNode = visited.pop()
        dfs(nextNode, array, visited)


# time O(n)
# space O(n)
def depthFirstSearch(self, array):
    visited = []
    dfs(self, array, visited)


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

start_node = Graphs.create_graph(data)
array = []
depthFirstSearch(start_node, array)
print(array)