class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for char in "abcdefghijklmnopqrstuvwxyz"}
        indegree = {char: 0 for word in words for char in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            # Edge case
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for k in range(min_len):
                if w1[k] != w2[k]:
                    if w2[k] not in adj[w1[k]]:
                        adj[w1[k]].add(w2[k])
                        indegree[w2[k]] += 1
                    break

        queue = deque([char for char in indegree if indegree[char] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)

            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # check cycle
        if len(res) < len(indegree):
            return ""

        return "".join(res)
