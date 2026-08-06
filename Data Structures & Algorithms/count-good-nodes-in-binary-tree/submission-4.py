# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodCount = 0

        def helper(root, max_prev):
            if not root:
                return

            nonlocal goodCount

            if root.val >= max_prev:
                goodCount += 1

            helper(root.left, max(max_prev, root.val))
            helper(root.right, max(max_prev, root.val))


        helper(root, -math.inf)

        return goodCount