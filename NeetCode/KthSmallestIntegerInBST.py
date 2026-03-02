# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0, None]

        def traverse(node):
            if not node:
                return

            traverse(node.left)

            count[0] += 1

            if count[0] == k:
                count[1] = node.val
                return

            traverse(node.right)

        traverse(root)

        return count[1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0, None]

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if count[0] < k:
                count[1] = node.val
                count[0] += 1
            inorder(node.right)

        inorder(root)

        return count[1]
