class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        from collections import defaultdict, deque

        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                all_combo_dict[pattern].append(word)

        queue = deque([(beginWord, 1)])

        visited = set()

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                intermediate_pattern = current_word[:i] + \
                    "*" + current_word[i+1:]

                for neighbor in all_combo_dict[intermediate_pattern]:
                    if neighbor == endWord:
                        return level+1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

        return 0
