# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0


        def recursive(root, maxVal):
            if not root:
                return
            nonlocal count
            if root.val >= maxVal:
                count += 1

            recursive(root.left, max(maxVal, root.val))
            recursive(root.right, max(maxVal, root.val))

        if not root:
            return 0
        
        recursive(root, root.val)

        return count
