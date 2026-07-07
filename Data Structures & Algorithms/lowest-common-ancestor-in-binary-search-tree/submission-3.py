# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parentNode = {}

        def dfs(node, parent):
            if not node:
                return

            parentNode[node.val] = parent

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        marked = set()

        def reverseDfs(node):
            if not node:
                return False

            if node.val in marked:
                return node

            marked.add(node.val)
            return reverseDfs(parentNode[node.val])

        reverseDfs(p)
        return reverseDfs(q)
