from typing import List
import sys

"""
递归当中:
    一定要把我们递归过程中一直在更新变量放入新一轮的递归中

"""


def letterCombinations(digits: str) -> list[str]:
    # leetcode 17
    data = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    ans = []   
    sub = ""    # 单条元素

    # empty digits
    if not digits:
        return ans

    def backtracking_17(sub_digits, sub):
        """
        sub_digits: 传入的字符串  ---递归中逐渐减少
        sub: 单条元素
        """
        
        # 递归结束逻辑
        if len(sub_digits) == 0:
            ans.append(sub)
            return ans
        else:
            # 取头部元素，因为sub_digits 一定非空
            cur_str = sub_digits[0]
            # 遍历该元素在data中的value值
            data_value:str = data[cur_str]

            for i in data_value:
                backtracking_17(sub_digits[1:], sub+i)

    backtracking_17(digits, sub)
    return ans







if __name__ == "__main__":
    print(letterCombinations("2378"))
        