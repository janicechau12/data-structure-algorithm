# 671. Second Minimum Node In a Binary Tree
# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return -1
    
        min, secondMin = root.val, -1
        
        def dfs(root):
            if root is None: return
            
            if root.left is not None and root.right is not None:
                secondMin = max(root.left.val, root.right.val)
            
            if secondMin == min:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        if secondMin == min:
            return -1
        return secondMin
        