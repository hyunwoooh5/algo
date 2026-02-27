class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}

            node = node[char]

        node['*'] = word

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node:
                return False
            node = node[char]

        return '*' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])

        res = set()

        def backtrack(r, c, node, path):
            # BC
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in path or board[r][c] not in node:
                return

            char = board[r][c]
            next_node = node[char]

            if '*' in next_node:
                res.add(next_node['*'])

            path.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                backtrack(r+dr, c+dc, next_node, path)

            path.remove((r, c))

        for row in range(m):
            for col in range(n):
                backtrack(row, col, trie.root, set())

        return list(res)
