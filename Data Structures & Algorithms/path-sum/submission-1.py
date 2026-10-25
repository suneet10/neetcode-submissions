# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        res = [0]
        
        def trav(curr,val):
            # print(curr.val,val)

            if val == targetSum and not curr.left and not curr.right:
                res.append(1)
                return

            if curr.left:
                trav(curr.left,val + curr.left.val)
            if curr.right:
                trav(curr.right,val + curr.right.val)

        if root:
            trav(root,root.val)
        if res[-1] == 1:
            return True

        return False
