class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)

        visit = [0] * numCourses

        def has_cycle(curr):
            if visit[curr] == 1:
                return True
            if visit[curr] == 2:
                return False

            visit[curr] = 1
            for next_course in adj[curr]:
                if has_cycle(next_course):
                    return True

            visit[curr] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)

        visited = [0]*numCourses

        def has_cycle(curr):
            # If it was visited in current test, it has a cycle
            if visited[curr] == 1:
                return True

            # If it was processed, no need to visit again
            if visited[curr] == 2:
                return False

            # visited in current session
            visited[curr] = 1

            for next_course in adj[curr]:
                if has_cycle(next_course):
                    return True

            # Finish current session
            visited[curr] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses  # number of prerequisites for each course

        adj = [[] for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        from collections import deque

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return finish == numCourses
