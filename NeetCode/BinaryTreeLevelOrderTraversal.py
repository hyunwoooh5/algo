# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []

        from collections import deque

        queue = deque([root])

        while queue:
            level_size = len(queue)
            temp = []
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(temp)
        return ans


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)

        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        from collections import deque
        queue = deque([root])

        while queue:
            l = len(queue)
            temp = []

            for _ in range(l):

                node = queue.popleft()

                temp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(temp)

        return ans


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        def dfs(node, depth):
            if not node:
                return None

            # add a new layer
            if len(ans) == depth:
                ans.append([])

            ans[depth].append(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return ans
