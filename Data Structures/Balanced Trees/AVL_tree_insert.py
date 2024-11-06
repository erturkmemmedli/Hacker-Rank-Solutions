# Self Balancing Tree


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.ht = None

def insert(root, new_val):
    if root is None:
        root = TreeNode(new_val)
        root.ht = set_height(root)
        return root
    
    if new_val < root.val:
        root.left = insert(root.left, new_val)
    else:
        root.right = insert(root.right, new_val)
    
    balance = height(root.left) - height(root.right)
    
    if balance > 1:
        if height(root.left.left) >= height(root.left.right):
            root = right_rotation(root)
        else:
            root.left = left_rotation(root.left);
            root = right_rotation(root);
    elif balance < -1:
        if height(root.right.right) >= height(root.right.left):
            root = left_rotation(root)
        else:
            root.right = right_rotation(root.right)
            root = left_rotation(root)   
    else:
        root.ht = set_height(root)
        
    return root

def right_rotation(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    root.ht = set_height(root)
    new_root.ht = set_height(new_root)
    return new_root

def left_rotation(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    root.ht = set_height(root)
    new_root.ht = set_height(new_root)
    return new_root

def height(root):
    return -1 if root == None else root.ht

def set_height(root):
    return -1 if root == None else 1 + max(height(root.left), height(root.right))

def inorder(root):
    if root:
        inorder(root.left)
        balance_factor = height(root.left) - height(root.right)
        print ("%d(BF=%d)" % (root.val, balance_factor), end = " ")
        inorder(root.right)
        
def preorder(root):
    if root:
        balance_factor = height(root.left) - height(root.right)
        print ("%d(BF=%d)" % (root.val, balance_factor), end = " ")        
        preorder(root.left)
        preorder(root.right)        
        

if __name__ == "__main__":
    t = int(input())
    arr = list(map(int, input().split()))
    root = None
    
    for i in range(t):
        root = insert(root, arr[i])
        
    root = insert(root, int(input()))
    
    inorder(root)
    print()
    preorder(root)
