"""
LC 210 - Course Schedule II
Difficulty: Medium
Pattern: Graph + DFS + Topological Sort

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Solved on: 03-14-2026
Re-solved on:

Notes:
- Similar to LC 207 (cycle detection)
- Build adjacency list
- Use DFS to detect cycle
- Append course AFTER processing prerequisites
- If cycle exists -> return []
"""

from typing import List


def dfs(course, courseMap, visiting, done, output):

    # cycle detected
    if course in visiting:
        return False

    # already processed
    if course in done:
        return True

    visiting.add(course)

    for prereq in courseMap[course]:
        result = dfs(prereq, courseMap, visiting, done, output)
        if result == False:
            return False

    visiting.remove(course)
    done.add(course)
    output.append(course)

    return True


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Step 1: Create adjacency list
        courseMap = {}
        for i in range(numCourses):
            courseMap[i] = []

        # Step 2: Build graph
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        output = []
        visiting = set()
        done = set()

        # Step 3: Run DFS for every course
        # Defing DFS outside 
        for course in range(numCourses):
            result = dfs(course, courseMap, visiting, done, output)
            if result == False:
                return []

        return output


if __name__ == "__main__":

    s = Solution()

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    print("Input:")
    print("Courses:", numCourses)
    print("Prerequisites:", prerequisites)

    result = s.findOrder(numCourses, prerequisites)

    print("Output:", result)

    
    numCourses = 2
    prerequisites = [[0,1],[1,0]]

    print("Input:")
    print("Courses:", numCourses)
    print("Prerequisites:", prerequisites)

    result = s.findOrder(numCourses, prerequisites)

    print("Output:", result)