"""
LC 347 - Top K Frequent Elements
Difficulty: Medium
Pattern: Hashmap + Bucket Sort

Time: O(n)
Space: O(n)

Solved on: 2026-03-09
Re-solved on:
Notes:
"""

class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: frequency map init freq count for each num in nums 
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: buckets init buckets with freq as index and list of nums as value
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 3: collect top k 
        result = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

if __name__ == "__main__":
    s = Solution()

    nums = [1,1,1,2,2,3]
    k = 2

    print(s.topKFrequent(nums, k))