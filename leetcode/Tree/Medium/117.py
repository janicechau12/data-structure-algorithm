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
        if root is None:
            return root
        
        queue = []
        queue.append(root)
        
        while(len(queue) > 0):
            size = len(queue)
            
            for i in range(size):
                # BFS
                node = queue.pop(0)
                if (i < size -1) : 
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return root

# explanation - https://www.youtube.com/watch?v=gc0pFTn90zg
# solution - https://zhenyu0519.github.io/2020/03/13/lc117/