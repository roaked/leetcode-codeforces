"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise."""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head #pointers to head
        while fast and fast.next: #this way we find the middle pointer
            slow = slow.next #one node (middle)
            fast = fast.next.next #two nodes
        
        prev = None
        while slow: #one node
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
sol = Solution().isPalindrome(head)
print(sol)
