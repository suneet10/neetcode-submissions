"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return None
        
        curr = head
        new_head = Node(0)
        new_curr = new_head

        index = 0
        dic = {}

        while curr:
            
            new_curr.val = curr.val
            
            if curr.next:
                new_curr.next = Node(0)

            dic[curr] = new_curr

            curr = curr.next
            new_curr = new_curr.next

        curr = head
        new_curr = new_head
        
        while curr:

            if curr.random:
                new_curr.random = dic[curr.random]
            else:
                new_curr.random = None

            curr = curr.next
            new_curr = new_curr.next

        return new_head