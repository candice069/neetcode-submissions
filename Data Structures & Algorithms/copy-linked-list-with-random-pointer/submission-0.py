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
        mapp = {None : None}
        cur = head

        while cur:
            new_node = Node(x=cur.val)
            mapp[cur] = new_node
            cur = cur.next
        
        cur = head
        while cur:
            new = mapp[cur]
            new.next = mapp[cur.next]
            new.random = mapp[cur.random]
            cur = cur.next
        return mapp[head]
        