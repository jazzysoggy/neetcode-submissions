# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = -1

        def subTree(root, n):
            if not root:
                return 0

            nonlocal answer
            
            left = subTree(root.left, 0)

            if left + n == k - 1:
                answer = root.val

            right = subTree(root.right, left + n + 1)

            return left + right + 1

        subTree(root, 0)
        return answer



        