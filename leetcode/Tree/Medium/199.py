# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        # traverse to right most
        list = []
        self.rightUtil(root, list)
        return list
        
    def rightUtil(self, root, list):
        if root is None:
            return
        else:
            list.append(root.val)
            if root.right:
                self.rightUtil(root.right, list)
            else:
                self.rightUtil(root.left, list)
            