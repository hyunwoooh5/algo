# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            curr = root.right
            while curr.left:
                curr = curr.left

            curr.left = root.left
            result = root.right
            del root
            return result

        return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        parent = None
        curr = root

        # Find node to delete
        while curr and curr.val != key:
            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        # If key does not exist
        if not curr:
            return root

        # one child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right

            # if node to delete is the root, child becomes the root
            if not parent:
                return child

            # link parent and node
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Two children
        else:
            par = None
            delNode = curr  # node to be replaced
            curr = curr.right

            # left traversal to find successor
            while curr.left:
                par = curr
                curr = curr.left

            # leftmost node
            if par:
                par.left = curr.right
                curr.right = delNode.right

            # successor takes leftover
            curr.left = delNode.left

            # delete root
            if not parent:
                return curr

            if parent.left == delNode:
                parent.left = curr
            else:
                parent.right = curr

        return root
