"""
LC 242 - Valid Anagram
Pattern: Frequency Hash Map
Time: O(n)
Space: O(1)  # since only lowercase letters

solved on: 2026-03-06
resolved on: 

"""

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))