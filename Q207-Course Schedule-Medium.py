'''
Question: 
  207. Course Schedule

Descrition: 
  There are a total of n courses you have to take, labeled from 0 to n-1.

  Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
  which is expressed as a pair: [0,1]

Examples:

	1.Input: 2, [[1,0]] 
	  Output: true
	  Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

	2.Input: 2, [[1,0],[0,1]]
	  Output: false
	  Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

#Python3 Code:

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #Solution 2
        #DFS-时间复杂度是O(N)，空间复杂度是O(N)
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
        
    # Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True

        
        #Solution
        #if not graph[n]找的是没有需要先修课的课,放入stack
        #[[1,0]]则是0,然后把先修课是0这门课的课的先修课删除，因为找到并修了
        #如果删除后该graph[i]为空，则说明这门课成了没有需要先修课的课，放入stack
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        stack = [n for n in range(numCourses) if not graph[n]]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            for n in neighbors[node]:
                graph[n].remove(node)
                if not graph[n]:
                    stack.append(n)
        return count == numCourses

        