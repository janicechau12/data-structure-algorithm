# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # DFS preorder to get sorted array and reverse it
        if root is None: return root
        
        list = []
        
        def dfs(node):
            if node is None: return 
            
            dfs(node.left)
            list.append(node)
            dfs(node.right)
        
        dfs(root)
        
        def Reverse(list):
            return [ele.val for ele in reversed(list)]
        
        tempVal = Reverse(list)
        
        for i in range(len(list)):
            list[i].val = tempVal[i]
    
        return root
    