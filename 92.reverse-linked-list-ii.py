#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head:
            return None
        
        if left == right:
            return head
        
        stack = []
        
        curr = head
        nodeCounter = 1
        
        while curr:
            if nodeCounter >= left and nodeCounter <= right:
                stack.append(curr.val)
            curr = curr.next
            nodeCounter += 1

        curr = head
        nodeCounter = 1
        while curr and stack:
            if nodeCounter >= left and nodeCounter <= right:
                curr.val = stack.pop()
            curr = curr.next
            nodeCounter += 1
        
        return head
# @lc code=end

