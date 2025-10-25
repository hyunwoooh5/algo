class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []

        n = len(tiles)
        used = [False] * n

        def backtrack(start, path):
            result.append(list(path))

            for i in range(n):
                if used[i] == False:
                    path.append(tiles[i])
                    used[i] = True
                    backtrack(i+1, path)
                    path.pop()
                    used[i] = False

        backtrack(0, [])

        return len(set(["".join(r) for r in result]))-1
