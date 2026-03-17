"""
LC 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding Window + HashSet

Time Complexity: O(n)
Space Complexity: O(n)

Solved on: 03-17-2026
Re-solved on:

Notes:
- Use sliding window with two pointers
- Expand right pointer
- Shrink left pointer when duplicate found
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()

        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":

    s = Solution()

    string = "abcabcbb"

    print("Input:", string)

    result = s.lengthOfLongestSubstring(string)

    print("Output:", result)