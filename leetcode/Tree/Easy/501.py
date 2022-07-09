# 501. Find Mode in Binary Search Tree

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        hash = {}
        results = []
        self.findModeUtil(root, hash)
        
        # get max occurance
        maxOccurance = max(hash.values())
        
        for key in hash.keys():
            if hash[key] == maxOccurance:
                results.append(key)
        
        return results
        
    def findModeUtil(self, root, hash):
            # preorder travesal (root -> left -> right)

            # Base case
            if root is None:
                return

            # Process root
            if root.val not in hash:
                hash[root.val] = 1
            else:
                hash[root.val] += 1

            # Recursively find the rest of left, right subtree
            self.findModeUtil(root.left, hash)
            self.findModeUtil(root.right, hash)
    
        
        
        