# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = deque()
        while True:
            r = deque()
            prev = None
            while True:
                if not head:
                    return head
                node = ListNode(head.val, prev)
                r.appendleft(node)
                prev = node
                if head.next is None:
                    break
                head = head.next
            print([n.val for n in r])
            return r.popleft()