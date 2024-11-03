# No Prefix Set


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.is_end:
                return False
        node.is_end = True
        if node.children:
            return False
        return True


def noPrefix(words):
    # Write your code here
    trie = Trie()
    for word in words:
        if not trie.insert(word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
        

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
