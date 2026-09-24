# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        hashset = {}
        
        while head:

            if head.val not in hashset:
                hashset[head.val] = 1

            else:
                if hashset[head.val] == 0:
                    hashset[head.val] += 1

                else:
                    hashset[head.val] -= 1

            head = head.next
            
        count = 0
        for i in hashset.values():

            if i != 0:
                count += 1
                if count == 1:
                    continue
                else:
                    return False

        return True
