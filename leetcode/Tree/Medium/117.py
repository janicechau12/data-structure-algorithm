# 117. Populating Next Right Pointers in Each Node II
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
        
        current, next = root, root.left if root else None
        
        while current and next:
            # connect then ancenstor children
            if current.left and current.right:
                current.left.next = current.right
            
            # if current.next is not null, connect both children and move pointer to right
            if current.next:
                if current.right:
                    current.right.next = current.next.left if current.next.left else current.next.right
                elif current.left:
                    current.left.next = current.next.left  if current.next.left else current.next.right
                
                current = current.next
            else:
                # move both pointer
                current = next
                # tricky part - it is possible that current doesn't have child
                if current.left and current.right is None:
                    if current.next is not None:
                        next = current.next.left if current.next.left else current.next.right
                    else:
                        next = None
                else:
                    next = current.left if current.left else current.right
                
        return root