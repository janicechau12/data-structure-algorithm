# 99. Recover Binary Search Tree

# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # DFS
        # need one pointer at root
        if root is None:
            return
        
        top = root
        self.leftTraversal(root.left, top)
        self.rightTraversal(root.right, top)
        
        
    def leftTraversal(self, root, top):
        if root is None:
            return
        
        self.leftTraversal(root.left, top)
        if root.val > top.val:
            temp = top.val
            top.val = root.val
            root.val = temp
        self.leftTraversal(root.right, top)
    
    def rightTraversal(self, root, top):
        if root is None:
            return
        
        self.rightTraversal(root.left, top)
        if root.val < top.val:
            temp = top.val
            top.val = root.val
            root.val = temp
        self.rightTraversal(root.right, top)