"""
LC 1091 - Shortest Path in Binary Matrix
Difficulty: Medium
Pattern: Graph + BFS (Shortest Path)

Time Complexity: O(n^2)
Space Complexity: O(n^2)

Solved on: 03-16-2026
Re-solved on:

Notes:
- BFS guarantees shortest path
- Move in 8 directions
"""

from typing import List
from collections import deque


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Step 1: Check start and end
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        queue = deque()

        queue.append((0, 0, 1))  # row, col, distance

        grid[0][0] = 1  # mark visited

        directions = [
            (1,0),(-1,0),(0,1),(0,-1),
            (1,1),(1,-1),(-1,1),(-1,-1)
        ]

        # Step 2: BFS
        while queue:

            r, c, dist = queue.popleft()

            if r == n-1 and c == n-1:
                return dist

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= n or 
                    nc < 0 or nc >= n or 
                    grid[nr][nc] != 0
                ):
                    continue

                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = 1

        return -1


if __name__ == "__main__":

    s = Solution()

    grid = [
        [0,1],
        [1,0]
    ]

    print("Input grid:")
    for row in grid:
        print(row)

    result = s.shortestPathBinaryMatrix(grid)

    print("\nShortest path length:", result)