"""
LC 1 - Two Sum
Difficulty: Easy
Pattern: Hash Map
Time: O(n)
Space: O(n)

Solved on: 2026-03-04
Re-solved on:
"""

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hashmap:
                print(f"Found pair: {num} and {remaining} at indices {i} and {hashmap[remaining]}")
                return hashmap[remaining], i
            hashmap[num] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))