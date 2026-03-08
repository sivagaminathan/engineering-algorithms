"""
LC 238 - Product of Array Except Self
Pattern: Prefix + Suffix Products
Time: O(n)
Space: O(n)

solved on: 2026-03-08
re-solved on:
"""

class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)

        # Multiply by 1 . will not change outcome since we are multiplying
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        # solution : product of i = product of ele left of i * product of ele right of i
        # Prefix stores product of all elements to the left of i
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        # Suffix stores product of all elements to the right of i
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        # final result is product of prefix and suffix
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result


if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3,4]
    print(s.productExceptSelf(nums))