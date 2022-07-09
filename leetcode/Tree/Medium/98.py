# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INT_MIN = -4294967296
        INT_MAX = 4294967296
        
        return self.isBSTUtil(root, INT_MIN, INT_MAX)
        
    def isBSTUtil(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val > minVal and root.val < maxVal and self.isBSTUtil(root.left, minVal, root.val) and self.isBSTUtil(root.right, root.val, maxVal):
                return True
        return False