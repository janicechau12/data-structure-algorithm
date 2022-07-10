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
        
        temp = []
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            temp.append(node)
            dfs(node.right)
        
        dfs(root)
        
        sortedNum = sorted(n.val for n in temp)
        
        for i in range(len(sortedNum)):
            temp[i].val = sortedNum[i]

# Solution - https://www.youtube.com/watch?v=bJBwOMPhe6Y