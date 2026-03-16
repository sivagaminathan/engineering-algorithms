"""
LC 542 - 01 Matrix
Difficulty: Medium
Pattern: Graph + BFS (Multi-source)

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Solved on: 03-16-2026
Re-solved on:

Notes:
- Start BFS from all 0 cells
- Expand outward updating distance
"""

from typing import List
from collections import deque


class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        queue = deque()

        # Step 1: Initialize queue with all zeros
        for r in range(rows):
            for c in range(cols):

                if mat[r][c] == 0:
                    queue.append((r, c))

                else:
                    mat[r][c] = -1

        directions = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]

        # Step 2: BFS
        while queue:

            r, c = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    mat[nr][nc] != -1
                ):
                    continue

                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))

        return mat


if __name__ == "__main__":

    s = Solution()

    mat = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]

    print("Input:")
    for row in mat:
        print(row)

    result = s.updateMatrix(mat)

    print("\nOutput:")
    for row in result:
        print(row)