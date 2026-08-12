from typing import Optional

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

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
     
# 2 题
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

# 21 题
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode(0)

    ln1 = list1
    ln2 = list2

    # 一方结束则停止
    while ln1 and ln2:
        if ln1.val <= ln2.val:
            # dummy update
            dummy.next = ln1
            dummy = dummy.next  

            # listNode update
            ln1 = ln1.next 
        else:
            dummy.next = ln2
            dummy = dummy.next
            ln2 = ln2.next

    # 剪枝,不存在两个listNode同时被取完
    if ln1:
        dummy.next = ln1
    else:
        dummy.next = ln2

    return cur.next

# 160 题  
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    解法1
    
    tempA = headA
    tempB = headB

    while tempA != tempB:
        tempA = tempA.next if tempA else headB
        tempB = tempB.next if tempB else headA

    return tempA
    """

    """
    解法2
    """
    # 获取两个listNode的长度
    def getLen(head:ListNode) -> int:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        return size

    lenA = getLen(head=headA)
    lenB = getLen(head=headB)

    # 差值
    diff = lenA - lenB

    # 基于差值重新构造listNode 
    if diff >=0:
        # lenA 先走
        while diff >0:
            headA = headA.next
            diff -=1

    elif diff < 0:
        # len B 先走
        while diff <0:
            headB = headB.next
            diff +=1

    # 双指针同时遍历
    tempA = headA
    tempB = headB
    while tempA != tempB:
        tempA = tempA.next
        tempB = tempB.next

    return tempA

# leetcode 203
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]: 
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

# 206 题
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            # 1. 保存下一个节点
            cur_next = cur.next

            # 2. 修改当前节点 next
            cur.next = prev

            # 3. prev 前进
            prev = cur

            # 4. cur 前进
            cur = cur_next

        return prev

def removeNthFromEnd(head: Optional[ListNode], n: int):
    # 快慢指针
    dummy = ListNode(0,next=head)
    fast = dummy
    slow = dummy

    # 快n个步伐
    for _ in range(n+1):
        fast = fast.next

    # 同时出发
    while fast:
        fast = fast.next
        slow = slow.next
    
    # 移除slow.next
    slow.next = slow.next.next

    return dummy.next

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head    # 移动一格
    fast = head    # 移动两格

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        # 有环
        if fast == slow:
            # 详情数学推理，结果为从slow走到剩余环的距离 == 从头开始走到环入口的距离
            p1 = head
            p2 = slow
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
    return None

def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    bit = 0  # 进位

    while l1 or l2:
        # 判断是否有节点
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # 三者求和
        sum_ = x + y + bit

        # bit 更新
        bit = sum_ // 10
        # 节点gengxin
        cur.next = ListNode(sum_ % 10)
        cur= cur.next

        # 更新listNodes
        l1 = l1.next
        l2 = l2.next

    return dummy.next


    

        

# 232 题
class MyQueue:
    def __init__(self):
        self.stack_in = []   # push 
        self.stack_out = []     # pop/peek

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        return 
        
    def pop(self) -> int:
        # 先判断stack_out 内部是否有element
        if self.stack_out:
            return self.stack_out.pop()

        # stack_in 倒进 stack_out
        while len(self.stack_in) >0:
            obj = self.stack_in.pop()
            self.stack_out.append(obj)
                
        return self.stack_out.pop()

    def peek(self) -> int:
        # 先判断stack_out 内部是否有element
        if self.stack_out:
            return self.stack_out[-1]
        
        while len(self.stack_in)>0:
            obj = self.stack_in.pop()
            self.stack_out.append(obj)
        
        return self.stack_out[-1]

    def empty(self) -> bool:
        if self.stack_in or self.stack_out:
            return False
        return True

        
if __name__ == "__main__":
    head = build_list([1,2,6,3,4,5,6])
    print(removeNthFromEnd(head, 2))

