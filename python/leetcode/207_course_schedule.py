"""
LC 207 - Course Schedule
Difficulty: Medium
Pattern: Graph + DFS + Cycle Detection

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Solved on:
Re-solved on:
Notes:
- Convert prerequisites into adjacency list
- Use DFS to detect cycle
- If cycle exists -> cannot finish courses
"""

from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Step 1: create adjacency list
        preMap = {}

        for i in range(numCourses):
            preMap[i] = []

        # Step 2: build graph
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # visited set for detecting cycles
        visited = set()
        done = set()

        # Step 3: DFS function
        def dfs(course):

            # cycle detected
            if course in visited:
                return False

            # cycle detected 
            if course in done:
                return True 
            
            visited.add(course)

            for prereq in preMap[course]:
                result = dfs(prereq)
                if result == False:
                    return False

            visited.remove(course)
            done.add(course)

            # mark course as completed
            preMap[course] = []

            return True

        # Step 4: run DFS for every course
        for course in range(numCourses):

            result = dfs(course)

            if result == False:
                return False

        return True


if __name__ == "__main__":

    s = Solution()

    numCourses = 2
    prerequisites = [[1,0]]

    print("Input:")
    print("Courses:", numCourses)
    print("Prerequisites:", prerequisites)

    result = s.canFinish(numCourses, prerequisites)

    print("Output:", result)

    
    numCourses = 2
    prerequisites = [[1,0], [0,1]]

    print("Input:")
    print("Courses:", numCourses)
    print("Prerequisites:", prerequisites)

    result = s.canFinish(numCourses, prerequisites)
    
    print("Output:", result)