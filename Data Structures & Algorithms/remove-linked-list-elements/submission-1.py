# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        curr = head

        if head == None:
            return None
        
        while curr.next:

            if curr.val == val and curr == head:

                head = curr.next
                curr = curr.next

            elif curr.next.val == val:

                curr.next = curr.next.next

            else:
                curr = curr.next

        if head.val == val:
            return head.next

        return head