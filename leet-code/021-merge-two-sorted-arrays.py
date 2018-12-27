# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        node = None
        if l1.val > l2.val:
            node = l2
            node.next = self.mergeTwoLists(l1, l2.next)
        else:
            node = l1
            node.next = self.mergeTwoLists(l1.next, l2)
        
        return node
