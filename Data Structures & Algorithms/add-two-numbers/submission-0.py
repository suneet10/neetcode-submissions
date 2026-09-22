# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        count = 0
        head = ListNode(0,None)
        curr = head
        carry = 0

        while l1 or l2:
            prev = curr
            curr.next = ListNode(0,None)

            x = y = 0

            if l1:
                x = l1.val
                l1 = l1.next

            if l2:
                y = l2.val
                l2 = l2.next

            # x = x*(10**count)
            # y = y*(10**count)

            print(x,y,carry)

            curr.val = (x + y + carry) % 10
            carry = (x + y + carry) // 10

            count += 1

            print(curr.val)
            curr = curr.next
        if carry != 0:
            curr.val = carry
            curr.next = None
        else:
            prev.next = None

        return head
