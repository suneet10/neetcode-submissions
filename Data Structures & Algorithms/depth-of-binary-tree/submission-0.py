# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def countDepth(node,count):

            if node:

                count += 1
                count = max(countDepth(node.left,count),countDepth(node.right,count))

            return count

        count = 0
        return countDepth(root,count)