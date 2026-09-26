#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        ans = []
        if head is None or head.next is None:
            return head
        first = head
        sec = head.next
        prev = None

        while first is not None and sec is not None:
            third = sec.next
            sec.next = first 
            first.next = third

            if prev is not None:
                prev.next = sec

            else:
                head = sec
            prev = first
            first = third
            if third is not None:
                sec = third.next
            else:
                sec = None
            
        return head


        # 1---> 2 ---> 3 ---> 4
# @lc code=end

