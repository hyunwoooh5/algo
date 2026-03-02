# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        from collections import deque

        queue = deque([root])

        while queue:
            level_size = len(queue)
            temp = 0

            for _ in range(level_size):
                node = queue.popleft()

                temp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)

        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth+1)  # right first
            dfs(node.left, depth+1)

        dfs(root, 0)

        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        from collections import deque

        queue = deque([root])

        while queue:
            l = len(queue)

            for _ in range(l):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(node.val)

        return ans


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def dfs(node, depth):
            if not node:
                return

            # if it is not added yet, we add it
            if len(ans) == depth:
                ans.append(node.val)

            # right first
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return ans
