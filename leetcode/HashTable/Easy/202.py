# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.



# 12 
# 1 + 4 = 5
# false 

class Solution:
    def isHappy(self, n: int) -> bool:  
        nStr = str(n)
        while len(nStr) > 1:
            sum = 0
            for i in range(len(nStr)):
                sum += (int(nStr[i]))^2
            nStr = str(sum)
        return (int(nStr) == 1)