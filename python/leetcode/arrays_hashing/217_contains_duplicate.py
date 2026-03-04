"""
LC 217 - Contains Duplicate
Difficulty: Easy
Pattern: Hash Set
Time: O(1)
Space: O(n)

Solved on: 2026-03-04
Re-solved on:
Notes:
"""

class Solution:
    def containsDuplicate(self, nums):
        seen = set() # Hash Set to store unique values 

        for num in nums: 
            if num in seen:
                return True
            seen.add(num)
        
        return False


if __name__ == "__main__":
    s = Solution()
    print("Nums: ", [1,2,3,1], "Contains Duplicate: ", s.containsDuplicate([1,2,3,1]))  # Expected: True
    print("Nums: ", [1,2,3,4], "Contains Duplicate: ", s.containsDuplicate([1,2,3,4]))  # Expected: False