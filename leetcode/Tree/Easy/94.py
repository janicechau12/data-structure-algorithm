# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.inorderUtil(root, list)
        return list
    
    def inorderUtil(self, root, list):
        if root is not None:
            self.inorderUtil(root.left, list)
            list.append(root.val)
            self.inorderUtil(root.right, list)
        