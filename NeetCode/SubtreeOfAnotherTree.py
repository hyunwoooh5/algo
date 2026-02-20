# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root:
                return False

            if self.isSameTree(root, subRoot):
                return True

            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and root2:
                return False
            elif root1 and not root2:
                return False
            elif not root1 and not root2:
                return True

            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right) and root1.val == root2.val

        return dfs(p, q)
