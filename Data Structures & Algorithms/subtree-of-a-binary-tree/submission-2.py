# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(node1,node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            else:
                if node1.val == node2.val:
                    
                    a = check(node1.left,node2.left)
                    b = check(node1.right,node2.right)

                    if a and b:
                        return True
                    else:
                        return False
                else:

                    return False
        if not root:
            return False

        if root.val == subRoot.val:

            if check(root,subRoot):
                return True

        if self.isSubtree(root.left,subRoot):
            return True
        if self.isSubtree(root.right,subRoot):
            return True

        return False          