# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        count = 0
        curr = head

        while curr:

            count += 1
            curr = curr.next

        if count == 1:
            return True
        print(count)

        if count % 2 == 0:
            odd = False
        else: 
            odd = True
        
        arr = []
        curr = head
        count2 = 0
        while curr:
            count2 += 1
            # print(curr.val,arr,count2,odd,(count/2)+1)
            if (count//2)+1 == count2 and odd == True:
                a = 1
            else:
                if count/2 >= count2:
                    arr.append(curr.val)
                elif arr[-1] == curr.val:
                    arr.pop()
            # print(curr.val,arr,count2,odd,(count/2)+1)
            curr = curr.next

        if arr == []:
            return True
        else:
            return False
        