# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        stack = [root]

        if not root:
            return []

        while len(stack) > 0:
            toAppend = 0
            toRange = len(stack)
            for i in range(toRange):
                item = stack[0]
                stack.pop(0)
                if item.left:
                    stack.append(item.left)
                if item.right:
                    stack.append(item.right)

                toAppend = item.val

            output.append(toAppend)

        return output