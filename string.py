from typing import List

def lengthOfLongestSubstring(s: str) -> int:
    """
    拼接字符串
    
    记录max_length
    重复则从头部消除元素后再配对 直到 无重复
    """
    
    ans = ""
    max_legth = 0

    for i in range(len(s)):
        if s[i] not in ans:
            # 下个元素为新元素， 加入即可
            ans += s[i]
            if len(ans) >max_legth:
                max_legth = len(ans)        # update max_len
        else:
            while ans.find(s[i]) != -1:     # 一直有，一直切
                ans = ans[1:]
            ans += s[i]
    
    return max_legth

def search(nums: List[int], target: int) -> int:
    # leetcode 33
    # 双指针 + 二分搜索

    # 特殊情况
    if len(nums) == 1:
        return 0 if  nums[0] == target else -1
    
    # 双指针
    left = 0
    right = len(nums)-1

    """ 通过双指针的无限夹逼"""
    while left<=right:
        # center
        mid = (right+left) // 2

        if nums[mid] == target:
            return mid        

        # 判断左右哪里有序, 优先有序
        if nums[left] <= nums[mid]:
            # 左半边有序， 查询左半边
            if nums[left] <= target <= nums[mid]:
                right = mid-1
            # 未在半区，查询另外半区
            else:
                left = mid +1
        else:
            # 左边无序, 查询右边
            if nums[mid]<= target <= nums[right]:
                left = mid+1
            else:
                right = mid -1
    
    return -1

def generateMatrix(n: int) -> List[List[int]]:
    # leetcode 59

    # 四维边界
    top,left = 0,0
    down, right = n-1, n-1

    # 初始化 n x n 矩阵
    matrix = [[0] * n for _ in range(n)]

    num = 1
    target = n*n

    while num <= target:
        # left to right
        for i in range(left,right+1):
            matrix[top][i] = num
            num += 1
        top += 1

        # top to down
        for i in range(top, down+1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # right to left:
        if left < right:
            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
        
        if top < down:
            for i in range(down, top-1, -1):
                matrix[i][left] = num
                num+=1
            left += 1
    return matrix 

if __name__ == "__main__":
    print(generateMatrix(4))

