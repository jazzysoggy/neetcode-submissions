# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.track = {}

    def longest(self, root):
        if root == None:
            return 0 

        return max(self.longest(root.left), self.longest(root.right)) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        nodePath = self.longest(root.left) + self.longest(root.right)
        dL = self.diameterOfBinaryTree(root.left)
        dR = self.diameterOfBinaryTree(root.right)
        return max(dL, dR, nodePath)