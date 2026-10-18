# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def reverse(node):

            head = node
            # print(1,head)

            if head:
                temp = head.left
                head.left = head.right
                head.right = temp

                reverse(head.left)
                reverse(head.right)

        reverse(root)

        return root