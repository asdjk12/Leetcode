from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    # leetcode 707
    def __init__(self) -> None:
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        # 获取listNode中第index个元素的value
        # special
        if index <0 or index >= self.size:
            return -1

        temp = 0
        cur = self.dummy.next
        while temp < index:
            cur = cur.next
            temp += 1
        return cur.val
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index > self.size:
            return 

        cur = self.dummy

        for _ in range(index):
            cur = cur.next
        temp = ListNode(val)
        temp.next = cur.next
        cur.next = temp
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index >= self.size:
            return 
        
        cur = self.dummy

        for _ in range(index):
            cur = cur.next

        cur.next = cur.next.next
        
        self.size -= 1
       
def build_list(nums):
    # 用于构建nodeList
    dummy = ListNode(0)   # 虚拟头节点
    cur = dummy

    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next    

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # leetcode 206
    if head.next is None:
        return head

    # dummy = ListNode(0)
    prex = None
    while head.next is not None:
        cur = ListNode(head.val)
        cur.next = prex

        prex = cur
        head = head.next
    return prex
     

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Leetcode 2
    dummy = ListNode(0)
    ans = dummy
    bit_carry  = 0

    while l1 or l2 or bit_carry:
        # 当前节点
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        sum = x+y + bit_carry       # 三者求和
        ans.next = ListNode(sum%10)    # 连接下一Node
        bit_carry = sum // 10       # 求余数
        
        # 推进下一位
        ans = ans.next          
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]: 
    # leetcode 203
    dummy = ListNode(0)
    ans = dummy

    while head:
        if head.val == val:
            head = head.next
        else:
            # 链接
            ans.next = head
            head = head.next
            ans = ans.next
            ans.next = None
    return dummy.next


        
if __name__ == "__main__":
    head = build_list([1,2,6,3,4,5,6])
    print(removeElements(head, 6))

