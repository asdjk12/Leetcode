from typing import List

def maxArea(height:List[int]):
    # leetcode 11
    # 双指针无限逼近，穷举法完成

    # 初始化
    left = 0
    right = len(height) -1
    ans = min(height[left], height[right]) * (len(height)-1)

    while left < right:
        # 计算当前area
        cur_area = abs(left- right) * min(height[left], height[right])
        if cur_area > ans:
            ans = cur_area

        # 逼近过程中宽一定减少
        # 因此 高度要提高
        # 高度取决于 柱子的短高
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
        

    return ans

if __name__ == "__main__":
    print(maxArea([4,3,2,1,4]))

    

