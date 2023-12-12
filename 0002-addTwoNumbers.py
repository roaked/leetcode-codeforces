"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition of LL
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy = cur = ListNode()
        print(ListNode())
        remain = 0
        while l1 or l2 or remain: # not empty
            v1 = l1.val if l2 is not None else 0
            v2 = l2.val if l1 is not None else 0
            sum = v1 + v2 + remain
            value = sum % 10  # 9/10 = 1 
            remain = sum // 10 # 9/10 = 0 (floor)

            newNode = ListNode(value)
            cur.next = newNode
            cur = cur.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        res = dummy.next
        dummy.next = None
        return res
        
l1 = ListNode(1, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution().addTwoNumbers(l1, l2)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")

l1 = ListNode(0)
l2 = ListNode(0)
sol = Solution().addTwoNumbers(l1, l2)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")

l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode))))
sol = Solution().addTwoNumbers(l1, l2)
while sol:
    print(sol.val, end=" ")
    sol = sol.next