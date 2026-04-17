class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses

        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[pre] += 1
            adj[course].append(pre)

        from collections import deque

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return ans[::-1] if len(ans) == numCourses else []


# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)

        visited = [0]*numCourses

        ans = []
        is_possible = True

        def has_cycle(curr):
            nonlocal is_possible
            if not is_possible:
                return

            visited[curr] = 1

            for next_course in adj[curr]:
                if visited[next_course] == 0:
                    has_cycle(next_course)
                elif visited[next_course] == 1:  # There is a cycle
                    is_possible = False
                    return

            visited[curr] = 2
            ans.append(curr)

        for i in range(numCourses):
            if visited[i] == 0 and is_possible:
                has_cycle(i)

        return ans[::-1] if is_possible else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses

        adj = [[] for _ in range(numCourses)]

        # Direction is different
        for course, pre in prerequisites:
            indegree[course] += 1
            adj[pre].append(course)

        ans = []

        def dfs(node):
            ans.append(node)
            indegree[node] -= 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    dfs(neighbor)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return ans if len(ans) == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj_list[pre].append(course)

        visit = [0]*numCourses

        ans = []

        def dfs(curr):
            if visit[curr] == 1:
                return True
            if visit[curr] == 2:
                return False

            visit[curr] = 1

            for course in adj_list[curr]:
                if dfs(course):
                    return True

            visit[curr] = 2

            ans.append(curr)

            return False

        for i in range(numCourses):
            if dfs(i):
                return []

        return ans[::-1]
