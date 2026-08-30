import math
def solve():
    n, m = map(int, input().split())
    nums = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        nums.append(temp)

    # print(nums)

    res = 0     # result

    # body
    for i in range(1,m):      # i: 运行次数
        print(f"第{i}轮")
        # nums 中取元素
        for x in range(len(nums)):
            # 首尾元素
            print(f"nums: {nums}")
            print(f"x: {x}")
            # print(nums[x][0])
            h,t = nums[x][0], nums[x][-1]   # head, tail
            if h<= t:
                print(f"hhh: {h}")
                round_res = h * pow(2,i)
                print(f"round_res {round_res}")
                # nums update
                nums[x] = nums[x][1:]
            else:
                print(f"ttt: {t}")
                round_res = t * pow(2,i)
                print(f"round_res {round_res}")
                # nums update
                nums[x] = nums[x][:-1]
            # res update
            res += round_res
            print(f"res: {res}")

    # 最后一轮
    print(f"last: {nums}")
    for last in nums:
        res += last[0] * pow(2,m)

    print(res % (10^9 +7))
        



if __name__ == "__main__":
    solve()
