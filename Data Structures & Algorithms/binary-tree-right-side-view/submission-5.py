# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        stack = deque()
        stack.append(root)

        while len(stack) > 0:
            output.append(0)
            for i in range(len(stack)):
                curr = stack.popleft()
                output[-1] = curr.val
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)

        return output

        