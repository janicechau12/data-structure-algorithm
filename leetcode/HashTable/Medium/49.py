# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Example 2:

# Input: strs = [""]
# Output: [[""]]

from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        key = set()
        dict = defaultdict(list)
        
        for i in range(len(strs)):
        
            for s in range(len(strs[i])):
              key.add(strs[i][s])
            dict[tuple(key)].append(strs[i])
            key.clear()
        
        return dict.values()

# Result:
# {'t', 'a', 'e'}


# {'t', 'a', 'e'}


# {'t', 'a', 'n'}


# {'t', 'a', 'e'}


# {'n', 'a', 't'}


# {'t', 'a', 'b'}


# dict_values([['eat', 'tea', 'ate'], ['tan'], ['nat'], ['bat']])