# Determining DNA Health


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict 
from bisect import bisect_left, bisect_right

def dHealth(first, last, largest, d, geneDict, subStrs): 
    result = 0
    for item in range(len(d)):
        #we only need to check sub-strings if they are smaller or 
        #equal to the size of the largest sub string in geneDict
        for subItem in range(1, largest+1): 
             #break if we would go over the last character in the string
            if item+subItem > len(d):
                break
            #our range for subItem is 1 to largest+1, because this does not include the end index.
            subStr = d[item:item+subItem] 
            #the set subStrs includes partial matches, so if our current subStr 
            #is not in subStrs, then we know no larger subStr will be in geneDict. 
            #It is much faster to search a set than the dict.
            if subStr not in subStrs:
                break 
            if subStr not in geneDict:
                continue
            genes = geneDict[subStr][0]
            healthScores = geneDict[subStr][1]
            #bisect right gives us the total value of all the matches in geneDict, up to our last value. 
            #bisect left gives us the total value of all the matches before our first value.
            result += healthScores[bisect_right(genes, last)] - healthScores[bisect_left(genes, first)]
    return result 

if __name__ == '__main__': 
    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input())
    
    #defaultdict is just like a dictionary, except it will not raise a KeyError, 
    #and provides a default value for keys that do not exist.
    geneDict = defaultdict(lambda: [[],[0]]) 
    subStrs = set()

    for item in range(len(genes)):
        geneDict[genes[item]][0].append(item)
        for i in range(1, len(genes[item])+1):
            #our range for i is 1 to len(genes[item]+1, because this does not include the end index.
            subStrs.add(genes[item][:i]) 

    for item in geneDict.values():
        for i in range(len(item[0])):
            #This builds a list of ascending values when there are multiple instances of the same gene.
            item[1].append(item[1][i] + health[item[0][i]]) 

    largest = max(map(len, genes))
    minR = math.inf
    maxR = 0

    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        result = dHealth(first, last, largest, d, geneDict, subStrs)
        minR = min(minR, result)
        maxR = max(maxR, result)

    print(minR, maxR)


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


# Only one test case failing Aho Corasick Algorithm
import bisect
from collections import defaultdict
import sys

# https://www.hackerrank.com/challenges/determining-dna-health


class TreeNode:
    __slots__ = (
        "is_dictionary_node",
        "longest_suffix",
        "dict_suffix",
        "children",
        "health",
        "health_calculated",
        "gene_number",
        "gene_health",
    )

    def __init__(self):
        # Aho-Corasick Trie
        self.is_dictionary_node = False
        self.children = defaultdict(TreeNode)
        # Health Data
        self.health_calculated = False


health_tree_root = TreeNode()
calculated_dictionary_nodes = []


def find_suffix_nodes():
    _health_tree_root = health_tree_root
    _health_tree_root.longest_suffix = None
    _health_tree_root.dict_suffix = None

    health_nodes = [_health_tree_root]

    for health_node in health_nodes:
        for child_gene_char in health_node.children:
            child_health_node = health_node.children[child_gene_char]
            # Suffix Node
            suffix_node = health_node.longest_suffix
            while suffix_node and child_gene_char not in suffix_node.children:
                suffix_node = suffix_node.longest_suffix
            child_health_node.longest_suffix = (
                suffix_node.children[child_gene_char]
                if suffix_node and child_gene_char in suffix_node.children
                else _health_tree_root
            )
            # Dict Node
            suffix_node = child_health_node.longest_suffix
            if suffix_node:
                if suffix_node.is_dictionary_node:
                    child_health_node.dict_suffix = suffix_node
                else:
                    child_health_node.dict_suffix = suffix_node.dict_suffix
            # Children
            health_nodes.append(child_health_node)


def create_tree():
    _ = input()  # n that we don't use
    _health_tree_root = health_tree_root
    health_node = _health_tree_root

    def get_gene_health():
        for gene_health in input().split(" "):
            yield int(gene_health)

    genes = input().split(" ")
    get_gene_health = get_gene_health()
    gene_number = 0
    for gene in genes:
        health_node = _health_tree_root
        for gene_char in gene:
            health_node = health_node.children[gene_char]
        gene_health = next(get_gene_health)
        try:
            health_node.gene_number.append(gene_number)
            health_node.gene_health.append(gene_health)
        except AttributeError:
            health_node.is_dictionary_node = True
            health_node.gene_number = [gene_number]
            health_node.gene_health = [gene_health]
        gene_number += 1


def match_search(first, last, strand):
    total = 0
    _health_tree_root = health_tree_root
    _calculated_dictionary_nodes = calculated_dictionary_nodes
    health_node = _health_tree_root

    for strand_char in strand:
        while (health_node != _health_tree_root) and (
            strand_char not in health_node.children
        ):
            health_node = health_node.longest_suffix

        if strand_char in health_node.children:
            health_node = health_node.children[strand_char]
            dict_node = (
                health_node
                if health_node.is_dictionary_node
                else health_node.dict_suffix
            )
            while dict_node and dict_node != _health_tree_root:
                if not dict_node.health_calculated:
                    health = 0
                    first_health = max(
                        bisect.bisect_left(dict_node.gene_number, first), 0
                    )
                    last_health = bisect.bisect_right(dict_node.gene_number, last)
                    health = sum(dict_node.gene_health[first_health:last_health])
                    dict_node.health_calculated = True
                    dict_node.health = health
                    _calculated_dictionary_nodes.append(dict_node)

                total += dict_node.health
                dict_node = dict_node.dict_suffix

    for node in _calculated_dictionary_nodes:
        node.health_calculated = False

    _calculated_dictionary_nodes.clear()

    return total


if __name__ == "__main__":
    create_tree()

    find_suffix_nodes()

    s = int(input().strip())

    # strands = []
    total_min = sys.maxsize
    total_max = 0

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        strand = first_multiple_input[2]

        total = match_search(first, last, strand)
        if total > total_max:
            total_max = total
        if total < total_min:
            total_min = total

    print(total_min, total_max)
