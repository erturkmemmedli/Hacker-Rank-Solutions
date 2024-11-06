# Array and simple queries


# Enter your code here. Read input from STDIN. Print output to STDOUT

from array import array

def array_queries(arr: array[int], queries: list[list[int]]) -> None:
    for t, i, j in queries:
        if t == 1:
            arr = arr[i-1:j] + arr[:i-1] + arr[j:]
        else:
            arr = arr[:i-1] + arr[j:] + arr[i-1:j]
    
    print(abs(arr[0] - arr[-1]))
    print(*arr)


if __name__ == '__main__':
    first = list(map(int, input().split()))
    N, M = first[0], first[1]
    arr = array('i', [int(val) for val in input().split()])
    queries = [list(map(int, input().split())) for _ in range(M)]
    array_queries(arr, queries)

# Alternative solution

import random

class Node:
    def __init__(self, val=-1):
        self.val = val
        self.siz = 1
        self.pri = random.randint(0, 1000000000)
        self.left = None
        self.right = None

def size(tree):
    return tree.siz if tree else 0

def update(tree):
    if tree:
        tree.siz = size(tree.left) + 1 + size(tree.right)

def split(tree, key, lcount=0):
    if not tree:
        return None, None
    if lcount + 1 + size(tree.left) <= key:
        l, r = split(tree.right, key, lcount + 1 + size(tree.left))
        tree.right = l
        update(tree)
        return tree, r
    else:
        l, r = split(tree.left, key, lcount)
        tree.left = r
        update(tree)
        return l, tree

def merge(l, r):
    if not l or not r:
        return l if l else r
    if l.pri > r.pri:
        l.right = merge(l.right, r)
        update(l)
        return l
    else:
        r.left = merge(l, r.left)
        update(r)
        return r

def getmin(tree):
    if tree.left:
        return getmin(tree.left)
    return tree.val

def getmax(tree):
    if tree.right:
        return getmax(tree.right)
    return tree.val

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.val, end=' ')
        inorder(tree.right)

class Treap:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = merge(self.root, Node(val))

    def query1(self, l, r):
        temp1, temp2 = split(self.root, r)
        temp3, temp4 = split(temp1, l - 1)
        self.root = merge(temp3, temp2)
        self.root = merge(self.root, temp4)

    def query2(self, l, r):
        temp1, temp2 = split(self.root, r)
        temp3, temp4 = split(temp1, l - 1)
        self.root = merge(temp3, temp2)
        self.root = merge(temp4, self.root)

    def get_min_max_diff(self):
        return abs(getmax(self.root) - getmin(self.root))

    def inorder_print(self):
        inorder(self.root)
        print()


if __name__ == "__main__":
    n, m = map(int, input().split())
    treap = Treap()
    
    for num in map(int, input().split()):
        treap.insert(num)

    for _ in range(m):
        query_type, l, r = map(int, input().split())
        if query_type & 1:
            treap.query2(l, r)
        else:
            treap.query1(l, r)

    print(treap.get_min_max_diff())
    treap.inorder_print()
