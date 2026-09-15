# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        curr = head

        fast = head
        count = 1

        while fast.next:
            count += 1
            fast = fast.next

        for i in range(0,count-n):

            curr = curr.next
            dummy = dummy.next

        dummy.next = curr.next
        
        if curr == head:
            return dummy.next

        return head


        