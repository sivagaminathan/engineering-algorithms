"""
LC 994 - Rotting Oranges
Difficulty: Medium
Pattern: BFS (Multi-source)

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Solved on: 03-15-2026
Re-solved on:
Notes:
- Use BFS to rot adjacent fresh oranges 
    (multiple rotten oranges in same level 
    will rot multiple fresh oranges at same time)
- DFS will not work since it will rot oranges in one path first before moving to other paths
"""

from typing import List
from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()

        ROW = len(grid)
        COL = len(grid[0])

        minutes = 0
        fresh = 0 
        # Step 1: Add all rotten oranges to queue and count fresh oranges
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        # 4 possible directions to rot adjacent fresh oranges
        directions = [[0, 1],[0, -1], [1, 0], [-1, 0]]

        # Step 2: BFS to rot adjacent fresh oranges 
        while q and fresh > 0: 

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = dr + r 
                    col = dc + c 
                    # Check if adjacent cell is within bounds and is a fresh orange
                    if (row < 0 or row >= ROW or 
                        col < 0 or col >= COL or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2 
                    q.append([row, col]) 
                    fresh -= 1 
            minutes += 1
        # Step 3: If there are still fresh oranges left, return -1, else return minutes
        return minutes if fresh == 0 else -1


if __name__ == "__main__":

    s = Solution()

    grid = [[2,1,1],[1,1,0],[0,1,1]]

    print("Input grid:")
    for row in grid:
        print(row)

    result = s.orangesRotting(grid)

    print("\nMinutes until all oranges rot:", result)               

