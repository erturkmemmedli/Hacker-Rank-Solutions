# Is This a Binary Search Tree?


""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    return dfs(root.left, -float('inf'), root.data) and dfs(root.right, root.data, float('inf'))

def dfs(root, minimum, maximum):
    if not root:
        return True
    
    if root.data <= minimum or root.data >= maximum:
        return False
    
    return dfs(root.left, minimum, root.data) and dfs(root.right, root.data, maximum)
