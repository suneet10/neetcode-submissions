# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0
        
        def trav(node,mnode):

            nonlocal ans

            if node:
                if node.val >= mnode:
                    ans += 1
                mnode = max(mnode,node.val)
                trav(node.left,mnode)
                trav(node.right,mnode)

        trav(root,0)
        return ans

            