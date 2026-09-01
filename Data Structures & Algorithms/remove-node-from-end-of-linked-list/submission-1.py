# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length, nth node from the end = (l-n) th
        length = 0
        cur = head 
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode(0, next = head)
        prev = dummy

        for _ in range(length-n):
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next