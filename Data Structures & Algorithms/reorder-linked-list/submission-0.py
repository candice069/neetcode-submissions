# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        #notice that the first half doesnt change their order but the second half changes
        #find the middle node first
        mid_node = self.findMid(head)

        #then, we need to reverse the last half
        def reverse(head):
            prev = None
            cur = head

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        reverse_head = reverse(mid_node.next)
        mid_node.next = None #need to cut this, otherwise, it will form the cycle
        cur1= head
        cur2 = reverse_head
        while cur1 and cur2:
            nxt1 = cur1.next
            nxt2 = cur2.next
            cur1.next = cur2
            cur2.next= nxt1
            cur1 = nxt1
            cur2 = nxt2
        # return head