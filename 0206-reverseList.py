"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
#Reverse pointers
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = None #null
        current = head #12345
        while current: #loop until empty LL
            next = current.next 
            current.next = dummy
            dummy = current
            current = next
        return dummy


head = ListNode(1, ListNode(2))
sol = Solution().reverseList(head)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution().reverseList(head)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")

head = []
sol = Solution().reverseList(head)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")