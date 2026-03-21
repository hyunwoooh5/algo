# Floyd-Warshall
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_pre = [[False]*numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            is_pre[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_pre[i][k] and is_pre[k][j]:
                        is_pre[i][j] = True

        return [is_pre[u][v] for u, v in queries]


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        is_pre = [set() for _ in range(numCourses)]

        for pre, course in prerequisites:
            adj[pre].add(course)
            indegree[course] += 1

        from collections import deque

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()

            for neighbor in adj[node]:
                is_pre[neighbor].add(node)
                is_pre[neighbor].update(is_pre[node])
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return [u in is_pre[v] for u, v in queries]
