# 116. Populating Next Right Pointers in Each Node

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.


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
        # Thought: breadth first traverse + queue (fifo) to traverse from left to right
        
        # base case
        if root is None:
            return
        
        # create queue and enqueue the root 
        queue = []
        queue.append(root)
        
        while(len(queue) > 0):
            # pop first node in queue
            current = queue.pop(0)
            
            # if mod of 2 is not 0, means the next value in queue is in same level
            if len(queue) % 2 != 0:
                current.next = queue[0]
                
            # add two children into queue
            if current.left is not None:
                queue.append(current.left)
            
            if current.right is not None:
                queue.append(current.right)
    
    
    
    
    
    
    
    
    
    