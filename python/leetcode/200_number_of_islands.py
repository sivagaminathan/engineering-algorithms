"""
LC 200 - Number of Islands
Difficulty: Medium
Pattern: Graph DFS on grid

Time: 
Space: 

Solved on: 03-12-2026
Re-solved on: 
Notes:
"""
def dfs(grid, r, c, rows, cols):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return 
            
            grid[r][c] = "#" # mark as visited - can also mark 0 
            dfs(grid, r+1, c, rows, cols) 
            dfs(grid, r-1, c, rows, cols)
            dfs(grid, r, c+1, rows, cols)
            dfs(grid, r, c-1, rows, cols)


class Solution:

    def numIslands(self, grid):

        if not grid: 
             return 0
        
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1
                    dfs(grid, r, c, rows, cols)
                
        return islands

if __name__ == "__main__":

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    s = Solution()
    print(s.numIslands(grid))