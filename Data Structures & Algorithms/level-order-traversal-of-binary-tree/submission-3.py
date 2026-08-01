# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        dfs = deque()

        dfs.append(root)

        if not root:
            return []

        while len(dfs) > 0:
            n = len(dfs)
            output.append([])

            for i in range(n):
                curr = dfs.popleft()
                output[-1].append(curr.val)

                if curr.left:
                    dfs.append(curr.left)
                
                if curr.right:
                    dfs.append(curr.right)

        return output



