
# 96. Unique Binary Search Trees

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        numTree = [1] * (n+1)
        
        # BST = max 2 children & left S.T is smaller than root, right is larger
#         # numTrees(2) = numTrees(0)*numTrees(1) +
#                         numTrees(1)*numTrees(0) = 2
                        
            
#         # numTrees(3) = numTrees(0)*numTrees(2) +
#                         numTrees(1)*numTrees(1) +
#                         numTrees(2)*numTrees(0) = 2+1+2=5
        
        # recursive
        for node in range(2, n+1):
            total = 0
            for root in range(1, node+1):
                left = root - 1
                right = node - root
                total += numTree[left] * numTree[right]
            numTree[node] = total
        
        return numTree[n]
        
# Solution: https://www.youtube.com/watch?v=Ox0TenN3Zpg