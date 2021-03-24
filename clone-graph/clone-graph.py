"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', visited = {}) -> 'Node':
        #Time: O(V + E) where V is the number of vertices and E is the number of edge
        #Space: O(V)
        
        if not node:
            return
        
        if node in visited:
            return visited[node]
        
        clone_node = Node(node.val)
        visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(child, visited) for child in node.neighbors]
        return clone_node