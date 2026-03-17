"""
LC 560 - Subarray Sum Equals K
Pattern: Prefix Sum + HashMap

Time Complexity: O(n)
Space Complexity: O(n)

solved on: 03-17-2026
re-solved on: 
"""

from typing import List
from collections import defaultdict


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # base case

        current_sum = 0
        count = 0

        for num in nums:

            current_sum += num

            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]

            prefix_map[current_sum] += 1

        return count


if __name__ == "__main__":

    s = Solution()

    nums = [1, 1, 1]
    k = 2

    print("Input:", nums, "k =", k)

    result = s.subarraySum(nums, k)

    print("Output:", result)