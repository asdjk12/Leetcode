import sys

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


def HJ44():
    # 华为笔试 43题，数独
    board = []
    for line in sys.stdin:
        row = list(map(int, line.split()))
        board.append(row)

    def isVaild(r,c,num):
        # 在board 中的r,c位置加入num是否合理
        # 行
        if num in board[r]:
            return False

        # 列
        for i in range(9):
            if board[i][c] == num:
                return False

        # 3*3
        b_r, b_c = (r // 3) * 3, (c // 3) * 3
        for m in range(b_r, b_r+3):
            for n in range(b_c, b_c+3):
                if board[m][n] == num:
                    return False

        return True

    def sudo():
        value = [x for x in range(1,10)]
        # 对0的位置填充
        for i in range(9):
            for j in range(9):
                # 9*9 数独
                if board[i][j] == 0:    # 待填充
                    for v in value:
                        if isVaild(i,j,v):
                            board[i][j] = v
                            if sudo():
                                return True
                            board[i][j] = 0

                    # 1~9 全部尝试完都不行
                    return False
        return True

    sudo()

    for row in board:
        print(*row)

def HJ48():
    nums = []
    for line in sys.stdin:
        nums = list(map(int,line.split()))

    node_remove = nums[-1]
    index = 2
    node_hashMap = {}

    # 把头节点放入map
    head = ListNode(nums[1])
    node_hashMap[2] = head

    while index < len(nums)-1:
        node_pair = [nums[index], nums[index+1]]

        prev = node_hashMap[node_pair[1]]    # num[index] 放在谁后面
        cur = ListNode(nums[index])       

        # 链表插入
        cur.next = prev.next
        prev.next = cur

        # 更新hashMap
        node_hashMap[nums[index]] = cur

        index += 2

    # 移除元素
    if head.val == node_remove: 
        head = head.next
    else:
        cur = head

        while cur.next:
            if cur.next.val == node_remove:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next

    # 输出真正的链表顺序
    cur = head
    res = []

    while cur:
        res.append(str(cur.val))
        cur = cur.next

    print(" ".join(res))

