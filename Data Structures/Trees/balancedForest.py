# Balanced Forest


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

class TreeNode:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.total_sum = None
    
    def __repr__(self):
        return f"TreeNode({self.value}, {self.total_sum})"


def build_tree(tree_values, tree_edges):
    tree_nodes = [TreeNode(v, set()) for v in tree_values]
    
    for node_from, node_to in tree_edges:
        # The tree input is undirected, so add them as both children and parent.
        # Later, clean the tree up while doing DFS over the tree.
        tree_nodes[node_from - 1].children.add(tree_nodes[node_to - 1])
        tree_nodes[node_to - 1].children.add(tree_nodes[node_from - 1])
        
    return tree_nodes[0]


def is_even_number(value):
    return not value & 1


def populate_tree_sums(root):
    stack = (root, None)
    visited = set()
    
    while stack:
        selected_node = stack[0]
        
        if selected_node not in visited:
            visited.add(selected_node)
            
            for child in selected_node.children:
                # Remove non-children nodes for cleaning out the "bad" inputs.
                # The tree has undirected edges so when we convert it
                # back to a proper tree, it's easier to work with.
                child.children.remove(selected_node)
                # Populate the stack.
                stack = (child, stack)
                
        else:
            stack = stack[-1]
            # Calculate the total sum of the current node before going up the tree.
            selected_node.total_sum = sum([x.total_sum for x in selected_node.children]) + selected_node.value


def find_best_balanced_forest(root):
    stack = (root, None)
    # visited -> visited nodes.
    # visited_sums -> sums that are currently visited.
    # root_complement_sums -> complement sums (total_value - parent) on the way
    # to the down the tree and decreased when going up the tree, it is okay to
    # do that because the sums are always unique in the root_complement_sums.
    visited, visited_sums, root_complement_sums = set(), set(), set()
    min_result_value = math.inf
    
    while stack:
        selected_node = stack[0]
        
        if selected_node not in visited:
            visited.add(selected_node)
            
            # Populate stack with children all at once
            for child in selected_node.children:
                stack = (child, stack)
                
            # This is a complement sum: TOTAL - current_sum
            # Calculate it while going down the tree, so when going up, use
            # those values in the root_complement_sums to check for existance.
            selected_sum_comp = root.total_sum - selected_node.total_sum
            root_complement_sums.add(selected_sum_comp)
            
            # Yes, no bitwise shifts.
            # selected_node.total_sum * 3 >= root.total_sum is checking that if the cut is
            # made in selected subtree and the visited subtree (in case the comp or sum
            # exists in the visited sums), the remaining subtree sum is equal or less
            # than the sums (which are equal) of the current and the visited subtrees.
            # This is just part of the requirement, so the remaining
            # tree can be balanced only with 0 or positive elements.
            cond_1 = (selected_node.total_sum * 2) in visited_sums
            cond_2 = (root.total_sum - selected_node.total_sum * 2) in visited_sums
            cond_3 = selected_node.total_sum * 3 >= root.total_sum
            
            if (cond_1 or cond_2) and cond_3:
                # Get the candidate value and update min_result_value if it's less.
                candidate_value = selected_node.total_sum * 3 - root.total_sum
                if candidate_value < min_result_value:
                    min_result_value = candidate_value
                    
        else:
            # This is a case where two even halfs are found.
            if (selected_node.total_sum * 2) == root.total_sum:
                candidate_value = selected_node.total_sum
                
                # In this case, a balanced forest is these two halfs + a new node as a
                # separate tree with the same value as the half of the existing tree sum.
                if candidate_value < min_result_value:
                    min_result_value = candidate_value
                    
            # Check visited sums and root complements.
            # Root complements are the sums on the way from root to the
            # selected nodes taken from its parents if we have a tree.
            #         (1)
            #       /  |  \
            #      /   |   \
            #     /    |    \
            #   (2)   (3)   (4)
            #   /\     |     /\
            # (5)(6)  (7)  (8)(9)
            # At the node 8, we have the { TOTAL - (8).sum, TOTAL - (4).sum }.
            # At the node 9, we have the { TOTAL - (9).sum, TOTAL - (4).sum }.
            # At the node 2, we have the { TOTAL - (2).sum }.
            cond_1 = selected_node.total_sum in visited_sums
            cond_2 = selected_node.total_sum in root_complement_sums
            cond_3 = selected_node.total_sum * 3 >= root.total_sum
            
            if (cond_1 or cond_2) and cond_3:
                # Candidate split.
                candidate_value = selected_node.total_sum * 3 - root.total_sum
                
                if candidate_value < min_result_value:
                    min_result_value = candidate_value
                    
            selected_sum_comp = root.total_sum - selected_node.total_sum
            
            if is_even_number(selected_sum_comp):
                selected_sum_comp_half = selected_sum_comp // 2
                cond_1 = selected_sum_comp_half > selected_node.total_sum
                cond_2 = selected_sum_comp_half in visited_sums
                cond_3 = selected_sum_comp_half in root_complement_sums
                
                if cond_1 and (cond_2 or cond_3):
                    # Same candidate value.
                    candidate_value = selected_sum_comp_half - selected_node.total_sum
                    
                    if candidate_value < min_result_value:
                        min_result_value = candidate_value
                        
            # Remove selected complement from root while going up the tree.
            root_complement_sums.remove(selected_sum_comp)
            # Add to the visited sums while going up the tree.
            visited_sums.add(selected_node.total_sum)
            # Stack pop.
            stack = stack[-1]

    if min_result_value == math.inf:
        min_result_value = -1
        
    return min_result_value


def balancedForest(tree_values, tree_edges):
    root = build_tree(tree_values, tree_edges)
    populate_tree_sums(root)
    return find_best_balanced_forest(root)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
