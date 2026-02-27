class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True

    def search(self, word: str) -> bool:
        def dfs(index, current_node):
            for i in range(index, len(word)):
                char = word[i]

                if char == '.':
                    for child in current_node:
                        if child != '*' and dfs(i+1, current_node[child]):
                            return True
                    return False

                else:
                    if char not in current_node:
                        return False
                    current_node = current_node[char]

            return '*' in current_node

        return dfs(0, self.root)
