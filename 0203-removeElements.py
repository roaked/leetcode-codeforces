"""Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
 and return the new head."""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(-1) #dummy placeholder at beginning (-1 1 2 6 3 4 5 6)
        dummy.next = head
    
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next


head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6
sol = Solution().removeElements(head, val)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")