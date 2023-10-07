"""
add_two_numbers.py

This is a solution to the add two numbers problem on leetcode.com

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 在两条链表上的指针
        p1, p2 = l1, l2
        # 虚拟头结点（构建新链表时的常用技巧）
        dummy = ListNode(-1)
        # 指针 p 负责构建新链表
        p = dummy
        # 记录进位
        carry = 0
        # loop through the two linked lists
        while l1 or l2:
            # get the values of the two nodes
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            # calculate the sum of the two values
            sum = l1_val + l2_val + carry
            # calculate the carry
            carry = sum // 10
            # calculate the value of the current node
            l3.val = sum % 10
            # move to the next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # check if there is a next node
            if l1 or l2:
                # create a new node
                l3.next = ListNode()
                # move to the next node
                l3 = l3.next

        # check if there is a carry
        if carry:
            # create a new node
            l3.next = ListNode()
            # move to the next node
            l3 = l3.next
            # set the value of the node to the carry
            l3.val = carry

        # return the head of the new linked list

        return l3_head
    
if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print(result.val)