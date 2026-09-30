# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def trav(node,arr):

            if node:
                arr.append(node.val)
                trav(node.left,arr)
                trav(node.right,arr)
            else:
                arr.append(None)

            return arr
        
        ans1 = []
        ans1 = trav(p,ans1)
        ans2 = []
        ans2 = trav(q,ans2)

        if ans1 == ans2:
            return True
        else:
            return False