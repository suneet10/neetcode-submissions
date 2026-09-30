# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def trav(node1,node2):

            if node1 and node2:
                if node1.val == node2.val:
                    a = trav(node1.left,node2.left)
                    b = trav(node1.right,node2.right)

                    if a and b:
                        return True
                    else:
                        return False
                
                else:
                    return False

            else:
                if node1 == None and node2 == None:
                    return True
                
                else:
                    return False

        return trav(p,q)
