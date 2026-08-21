from typing import List

"""
    总结:
    单调栈用stack
"""


# leetcode 739
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # 利用单调栈
    result = [0] * len(temperatures)
    stack = []          # 储存的是index

    for i in range(len(temperatures)):
        # 触发 stack 更新
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # 记录index 更新result
            result[stack[-1]] = abs(i - stack[-1])

            # 丢弃当前栈末 并替换成 更大value
            stack.pop()
        
        # stack中没有比 i 更大的 
        stack.append(i)
    return result

from copy import deepcopy
from collections import deque

class solution:
    def isValid(self, s):
        # 20
        stack = []
        left = ["[","(","{"]
        right = ["]", ")", "}"]

        for i in s:
            if i in left:   # 开口
                stack.append(i)
            else:
                # 闭口
                if stack: # 非空
                    last = stack.pop()  # 最近的元素
                    if left.index(last) == right.index(i):  # 互为一对
                        # 则这一对相互抵消且到一个循环
                        continue    
                else:
                    return False
        
        # 循环结束， stack 应为空
        if stack:
            return False
        return True
    
    def validStackSequence(self,push, pop):
        # 946
        stack = []
        pop_id = 0
        # 模拟堆栈

        for i in push:
            stack.append(push)  # 入栈
            while stack and stack[-1] == pop[pop_id]:
                stack.pop()
                pop_id += 1
        
        # 合规则该为None
        return not stack

    def simplifyPath(self,path):
        # 71
        parts = [x for x in path.split('/') if x]
        stack = []

        for i in parts:
            # skip
            if i == '.' or i == '':
                continue
            # 上级目录
            elif i == '..':
                # 仅在 stack不为空时弹出
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return '/' + '/'.join(stack)

    def buildArray(self, target, n):
        # 1441
        res = []
        target_index = 0
    
        # 流式出结果，因此每个结果都要进stack后进行操作
        for i in range(1, n+1):
            # 是否已满足
            if i-1 == target[-1]:    #单调递增 且ordered
                break
            else:
                res.append("push")  # compulsory
                if i != target[target_index]:
                    res.append("pop")
                else:
                    target_index += 1
        return res

    def calculate(self, s):
        stack = []  # 储存 符号 和 sum外
        res = 0
        sign = 1 # 1 / -1
        index = 0

        while index < len(s):
            char = s[i]
            # 多重判断
            if char.isdigit():     # number
                num = 0
                while index < len(s) and s[i].isdigit():  # 不仅个位数
                    num = num *10 + int(s[index])       # 并非计算，只是单纯拼接数字
                    index += 1
                res += num * sign      # 全局累加
                # 非数字
                continue        # 在while 循环中 已经更新过index
            
            # 符号
            elif char == "+":
                sign = 1
            elif char == "-":
                sign = -1

            # 括号
            elif char == "(":
                # 保存
                stack.append(res)
                stack.append(sign)
                # reset
                res = 0
                sign = 1

            elif char == ")":
                # 取出
                pre_sign = stack.pop()
                pre_res = stack.pop()

                # 求和
                res = pre_res + pre_sign *res        # 乘数sum为 新一轮‘()’ 中的结果
            index += 1
        return res


 

class myQueue:
    def __init__(self):
        self.in_stack = []      # 入栈
        self.out_stack = []     # 出栈

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        # 注意out_stack 为空
        if not self.out_stack:
            # 全部替换
            while self.in_stack:
                self.out_stack.append(self.out_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        # 注意out_stack 为空
        if not self.out_stack:
            # 全部替换
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        res = self.out_stack.pop()
        self.out_stack.append(res)
        return res

    def empty(self):
        if self.in_stack:
            return False
        if self.out_stack:
            return False
        return True        

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x:int):
        # 把x插入列尾， 并对先前的元素依次进行队尾插入
        time = len(self.queue)
        if time == 0:
            self.queue = deque([x])
        else:
            self.queue.append(x)    # 在队尾
            for _ in range(time):
                self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self): 
        if self.queue:
            return False
        return True

if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))

    