# Determining DNA Health



# Following Aho Corasick Algortihm results in TlE.

import math
import os
import random
import re
import sys

from collections import deque


class TrieNode:
    def __init__(self):
        # Initialize TrieNode attributes
        self.children = {}
        self.output = []
        self.fail = None


class Trie:
    def __init__(self):
        # Initialize root node of the trie
        self.root = TrieNode()

    def insert_into_trie(self, word):
        node = self.root
        # Traverse the trie and create nodes for each character
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Add keyword to the output list of the final node
        node.output.append(word)
        
    def build_trie(self, words):
        # Build the trie
        for word in words:
            self.insert_into_trie(word)
        
    def build_fails(self):
        # Build failure links using BFS
        queue = deque()
        # Start from root's children
        for node in self.root.children.values():
            queue.append(node)
            node.fail = self.root
        # Breadth-first traversal of the trie
        self.bfs_trie(queue)
            
    def bfs_trie(self, queue):
        while queue:
            current_node = queue.popleft()
            # Traverse each child node
            for key, next_node in current_node.children.items():
                queue.append(next_node)
                # Determine the failure node for the current node
                fail_node = current_node.fail
                # Find the longest proper suffix that is also a prefix
                while fail_node and key not in fail_node.children:
                    fail_node = fail_node.fail
                # Set failure link of the current node
                next_node.fail = fail_node.children[key] if fail_node else self.root
                # Add output patterns of failure node to current node's output
                next_node.output.extend(next_node.fail.output)
    
class AhoCorasick:
    def __init__(self, words):
        # Build the Aho-Corasick automaton
        self.trie = Trie()
        self.words = words
        self.trie.build_trie(words)
        self.trie.build_fails()
    
    def search_text(self, text):
        root = self.trie.root
        # Initialize result dictionary with modification -> set() instead of list()
        result = {word: set() for word in self.words}
        current_node = root
        # Traverse the text
        for i, char in enumerate(text):
            # Follow failure links until a match is found
            while current_node and char not in current_node.children:
                current_node = current_node.fail
            # Return to root if case of reaching to leaf node
            if not current_node:
                current_node = root
                continue
            # Move to the next node based on current character
            current_node = current_node.children[char]
            # Record matches found at this position
            for word in current_node.output:
                result[word].add(i - len(word) + 1)
        # Return all start indices of matching cases
        return result
        

def dna_health(genes, health, strands):
    # Initialize Aho Corasick automation
    aho_corasick = AhoCorasick(genes)
    # Initialize min and max total health for strands
    min_total_health = math.inf
    max_total_health = -math.inf
    total_health = 0
    # Loop for each strand
    for start, end, text in strands:
        # Search text with Aho Corasick Algorithm
        matches = aho_corasick.search_text(text)
        # Add health points for the selected genes
        for i in range(start, end + 1):
            total_health += len(matches[genes[i]]) * health[i]
        # Determine min and max total health for strands
        min_total_health = min(min_total_health, total_health)
        max_total_health = max(max_total_health, total_health)
        total_health = 0

    # Return min and max total health of DNA strands
    return [min_total_health, max_total_health]
    

if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    
    strands = []
    
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        
        strands.append((first, last, d))
        
    health = dna_health(genes, health, strands)
    print(*health)
