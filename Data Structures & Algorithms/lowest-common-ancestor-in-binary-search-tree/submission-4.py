# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parentNode = {}

        marked = set()

        def dfs(node, parent):
            if not node:
                return False

            parentNode[node.val] = parent

            print(node.val)

            toAdd = dfs(node.left, node)
            otherAdd = dfs(node.right, node)

            if toAdd or otherAdd or node.val == p.val:
                marked.add(node.val)
                return True

            return False

        dfs(root, None)
        print(marked)

        def reverseDfs(node):
            if not node:
                return None

            if node.val in marked:
                return node

            marked.add(node.val)
            return reverseDfs(parentNode[node.val])

        return reverseDfs(q)
