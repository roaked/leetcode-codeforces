"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        dummy = cur = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next

        cur.next = list1 if list1 else list2
        
        return dummy.next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution().mergeTwoLists(list1, list2)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")

list1 = ListNode()
list2 = ListNode()
sol = Solution().mergeTwoLists(list1, list2)
while sol:
    print(sol.val, end=" ")
    sol = sol.next

print("\n")

list1 = ListNode()
list2 = ListNode(1)
sol = Solution().mergeTwoLists(list1, list2)
while sol:
    print(sol.val, end=" ")
    sol = sol.next
