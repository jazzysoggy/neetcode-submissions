# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        order_idx = defaultdict(int)

        for i in range(len(inorder)):
            order_idx[inorder[i]] = i

        def reconstruct(l, r, idx):
            if idx >= len(preorder):
                return None

            if l > r:
                return None

            if order_idx[preorder[idx]] > r or order_idx[preorder[idx]] < l:
                return reconstruct(l, r, idx + 1)

            root = TreeNode(preorder[idx])

            left = reconstruct(l, order_idx[preorder[idx]] - 1, idx + 1)
            right = reconstruct(order_idx[preorder[idx]] + 1, r, idx + 1)

            root.left = left
            root.right = right

            return root



        return reconstruct(0, len(preorder) - 1, 0)
            
        