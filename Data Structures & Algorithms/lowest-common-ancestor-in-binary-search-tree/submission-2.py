# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dictionary = {}

        queue = deque()

        queue.append(root)

        while len(queue) != 0:
            current = queue.popleft()
            if current == None:
                continue
            if current.left != None:
                dictionary[current.left.val] = current
                queue.append(current.left)
            if current.right != None:
                dictionary[current.right.val] = current
                queue.append(current.right)

        pLow = p
        encountered = {root.val: True}
        qLow = q
        while pLow.val != root.val:
            encountered[pLow.val] = True
            pLow = dictionary[pLow.val]

        while qLow.val != root.val and qLow.val not in encountered:
            qLow = dictionary[qLow.val]

        return qLow

