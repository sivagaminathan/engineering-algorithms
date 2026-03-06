"""
LC 49 - Group Anagrams
Difficulty: Medium
Pattern: HashMap + Sorting

Time: O(n * k log k) n-no.of words, k-length of longest word 
Space: O(n) # O(n*k) but O(N)

Solved on: 2026-03-06
Re-solved on:
Notes: 
"""

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = {} # HashMap to group anagrams by their sorted wordset

        for word in strs:
            key = "".join(sorted(word)) # sort the word with their char

            if key not in anagram_map:
                anagram_map[key] = [] # create a new list for this anagram group

            anagram_map[key].append(word) # add the original word to the corresponding anagram group

        return list(anagram_map.values()) # return the grouped anagrams as a list of lists


if __name__ == "__main__":
    s = Solution()

    input_data = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(input_data))