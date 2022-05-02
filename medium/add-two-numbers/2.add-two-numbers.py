#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        return self.helper(l1, l2, carry)
    
    def helper(self, l1, l2, carry):
        
        val = l1.val + l2.val + carry
        carry = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.helper(l1.next, l2.next, carry)
        return ret
        
            
        
            
        
# @lc code=end
