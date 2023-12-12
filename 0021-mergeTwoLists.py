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

from typing import Optional, ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # None values

        return None

list1 = [1,2,4]
list2 = [1,3,4]
print(Solution().mergeTwoLists(list1, list2))

list1 = []
list2 = []
print(Solution().mergeTwoLists(list1, list2))

list1 = []
list2 = [0]
print(Solution().mergeTwoLists(list1, list2))