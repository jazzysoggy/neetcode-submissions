# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        output = []

        while len(stack) > 0:
            toRange = len(stack)
            output.append([])
            for i in range(toRange):
                item = stack[0]
                stack.popleft()
                output[-1].append(item.val)
                if item.left:
                    stack.append(item.left)
                if item.right:
                    stack.append(item.right)

        return output

