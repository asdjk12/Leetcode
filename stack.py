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
    
if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))

    