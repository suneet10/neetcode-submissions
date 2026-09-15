# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = ListNode(0,head)
        
        curr = head
        last = head
        prev = dummy
        arr = []

        while last:

            arr.append(last)
            last = last.next

        if len(arr) > 2:
            curr = head.next
            prev = head

            for i in range((len(arr)//2)+1):
                # print(prev.val,curr.val)
                prev.next = arr.pop()
                prev = prev.next
                prev.next = curr
                curr = curr.next
                prev = prev.next
                # print(prev.val,curr.val)

                if prev == curr:
                    break

            # print(curr.val,len(arr))
            curr.next = None
            



         