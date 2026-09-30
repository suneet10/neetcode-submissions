# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        diff = 0
        
        def calculate(node):

            nonlocal diff

            if node:

                left = calculate(node.left)
                right = calculate(node.right)
                if left == -1 or right == -1:
                    return -1
                if abs(left-right) > 1:
                    return -1
                diff = max(diff,abs(left-right))
                return 1 + max(left,right)

            else:
                return 0

        ans = calculate(root)
        if ans == -1:
            return False
            
        if diff <= 1:

            return True
        else:

            return False


            