"""
add_two_numbers.py

This is a solution to the add two numbers problem on leetcode.com

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。


# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Utility function to print the linked list for debugging purposes
    def __str__(self):
        vals = []
        current = self
        while current:
            vals.append(str(current.val))
            current = current.next  # 跳出循环的条件是 current 为 None  了
        return "->".join(vals)


# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。


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
        # 开始执行加法，两条链表走完且没有进位时才能结束循环
        while p1 or p2 or carry:
            # 先加上上次的进位
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            # 处理进位情况
            carry, val = divmod(val, 10)
            # 构建新节点
            p.next = ListNode(val)
            p = p.next
        # 返回结果链表的头结点（去除虚拟头结点）
        return dummy.next


# Test function
def test():
    # Helper function to create a linked list from a list of values
    def create_linked_list(vals):
        dummy = ListNode()
        current = dummy
        for val in vals:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Test cases
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = Solution().addTwoNumbers(l1, l2)
    print(result)  # Expected output: 7->0->8

    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = Solution().addTwoNumbers(l1, l2)
    print(result)  # Expected output: 0

    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = Solution().addTwoNumbers(l1, l2)
    print(result)  # Expected output: 8->9->9->9->0->0->0->1


# Run the test function
test()
