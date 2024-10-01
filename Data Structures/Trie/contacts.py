# Contacts


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        node.count += 1
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        
        node.is_end = True
    
    def find(self, partial):
        node = self.root
        
        for char in partial:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.count
        

def contacts(queries):
    # Write your code here
    trie = Trie()
    result = []
    
    for op, word in queries:
        if op == 'add':
            trie.insert(word)
        else:
            result.append(trie.find(word))
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
