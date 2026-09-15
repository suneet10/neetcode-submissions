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

        if n == 1:
            print(curr.val,fast.val)
            curr.next = None
            return head
        if curr == head:
            return curr.next
        
        else:
            print(3)
            curr.next = curr.next.next
            return head
