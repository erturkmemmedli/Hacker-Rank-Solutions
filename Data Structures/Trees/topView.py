# Tree : Top View


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque

def topView(root):
    #Write your code here
    position_map = {0: root.info}
    queue = deque([(root, 0)])
    
    while queue:
        node, dist = queue.popleft()
        if dist not in position_map:
            position_map[dist] = node.info
        
        if node.left:
            queue.append((node.left, dist - 1))
        if node.right:
            queue.append((node.right, dist + 1))
    
    res = sorted([(key, val) for key, val in position_map.items()], key=lambda x: x[0])
    print(*[v for k, v in res])



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
