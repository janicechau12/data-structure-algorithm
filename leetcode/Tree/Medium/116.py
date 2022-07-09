# 116. Populating Next Right Pointers in Each Node

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Solution: https://www.youtube.com/watch?v=U4hFQCa1Cq0    

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # setup current and next pointer
        current, next = root, root.left if root else None
        
        # as long as the current and next pointer is not null, we will continue BFS
        while current and next:
            # connect children of current node
            current.left.next = current.right
            
            if current.next is not None:
                # connect the children from different ancestor
                current.right.next = current.next.left
                # move current pointer to right
                current = current.next
            else:
            # move pointer if current.next is NULL (means reach to the right)
                current = next
                next = current.left
                
        return root
    
    
    
    
    
    
    
    
    
    
    
    