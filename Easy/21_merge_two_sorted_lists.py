"""
https://leetcode.com/problems/merge-two-sorted-lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    The biggest issue with linked lists is ensuring that you aren't performing operations on None objects.
    Thankfully this is relatively straightforward.
    """
    head: Optional[ListNode] = None # We want to know which node we're starting with so we can return it.
    current: Optional[ListNode] = ListNode() # This is the current considered node, initialized with a placeholder.

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        while list1 and list2: # As long as we have two lists, we need to compare both of them. Then, add the lowest.
            if list1.val <= list2.val:
                list1 = self.addNode(list1)
            else:
                list2 = self.addNode(list2)

        if list1 or list2: # Once we run out, if there is a list left, we just need to attach the remaining node.
            if list1:
                self.addNode(list1)
            elif list2:
                self.addNode(list2)

        return self.head
    
    def addNode(self, node: ListNode) -> ListNode:
        """
        I've abstracted the addition of a node to the list here for readability.
        This would be faster without the abstraction, but it makes the main function much cleaner.
        """
        if not self.head:
            self.head = node
        self.current.next = node
        self.current = node
        return node.next
    
"""
Analysis:
We need to touch every node of the shortest list, so we're O(n)
"""