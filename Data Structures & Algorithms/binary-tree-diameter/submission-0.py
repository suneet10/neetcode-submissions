# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dia = 0
        
        def diameter(node):
            nonlocal dia
            if node:
                left = diameter(node.left)
                right = diameter(node.right)
                dia = max(dia,left+right)
                return 1 + max(left,right)

            else:

                return 0
        
        diameter(root)
        return dia