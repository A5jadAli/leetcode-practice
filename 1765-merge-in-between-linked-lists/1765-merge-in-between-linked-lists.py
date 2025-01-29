# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pos = 0
        cur = list1
        end2 = list2
        while (end2.next):
            end2 = end2.next
        while (cur):
            if pos == a - 1:
                start = cur
                cur = cur.next
                pos += 1
            if pos == b:
                end2.next = cur.next
                start.next = list2
                return list1
            else:
                cur = cur.next
                pos += 1