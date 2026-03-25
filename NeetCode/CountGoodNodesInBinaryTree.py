# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, m=-100):
            if not node:
                return None

            if node.val >= m:
                self.count += 1
                m = node.val

            dfs(node.left, m)
            dfs(node.right, m)

        dfs(root)

        return self.count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        from collections import deque
        q = deque()

        q.append((root, -float("inf")))

        while q:
            node, maxval = q.popleft()

            if node.val >= maxval:
                res += 1
                maxval = node.val

            if node.left:
                q.append((node.left, maxval))

            if node.right:
                q.append((node.right, maxval))

        return res


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, maximum):
            if not node:
                return

            # if this is not a good node
            if node.val < maximum:
                dfs(node.left, maximum)
                dfs(node.right, maximum)
                return
            # if this is a good node
            else:
                self.ans += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)

        dfs(root, -101)

        return self.ans


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        from collections import deque

        queue = deque([(root, -float("inf"))])

        while queue:
            node, maxval = queue.popleft()

            if node.val >= maxval:
                ans += 1
                maxval = node.val
            if node.left:
                queue.append((node.left, maxval))

            if node.right:
                queue.append((node.right, maxval))

        return ans
