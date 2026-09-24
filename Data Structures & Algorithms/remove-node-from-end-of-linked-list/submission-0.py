# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            return None

        i = n
        curr = head
        fast = head

        while fast.next:

            if i > 0:
                fast = fast.next
                i -= 1

            else:
                fast = fast.next
                curr = curr.next

        if curr == head:
            curr = curr.next
            return curr
        else:
            curr.next = curr.next.next
            return head
