import heapq
from bisect import bisect_right, bisect_left

# 幸运年份
def special_year():
    T = int(input())
    for _ in range(T):
        year = int(input())

        year += 1    # 最小的更大数
        while len(str(year)) != len(set(str(year))):    # set 自带去重
            year += 1

        print(year)

def string_skip():
    T = input()
    if len(T) < 2:
        print("")
    else:
        print(T[0] + T[1::2])

def pdd_20250914_q3():
    # 前缀和
    n = int(input())
    nums = list(map(int, input().split()))
    
    hashMap = {0:1}    # key, value

    prefix = 0  # 前缀和
    ans = 0     # 多少对
    for i in nums:
        i -= 1  

        prefix += i # 获取前缀和
        ans += hashMap.get(prefix, 0) # 上一次同前缀 - 这次前缀 无变化。满足需求

        hashMap[prefix] = hashMap.get(prefix, 0)+1  # 次数加1

    return ans   

def pdd_20240825_q3():
    n,x = map(int,input().split()) # n: number ; x= val
    a = list(map(int,input().split()))

    def increase(nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True

    for i in range(n-1, 0, -1):
        # 满足条件:
        # 1. 前者大于后者
        if a[i] < a[i-1]:
            # 2. x> 前者
            if x< a[i-1] and x> a[i]:
                #swap
                x, a[i-1] = a[i-1], x
            else:
                return -1

    return a if increase(a) else -1

def pdd_2025_0817_q2():
    n,x = map(int, input().split())
    nums = list(map(int, input().split()))

    # 计算每个物品的花费资源
    for i in range(n):      # 不包括N
        nums[i] = nums[i] *  (n-i)        

    # 排序
    nums = sorted(nums) # 从小到大

    ans = 0
    for i in nums:
        if x>= i:
            ans += 1
            x -= i
        else:
            break
    return ans

def pdd_20250914_q4():
    n = int(input())
    nums = list(map(int, input().split()))
    x,y = map(int, input().split())

    # k的具体倍数index
    def k_number(k):
        res = []
        for i in range(1, n+1):
            if i %k ==0:    #x 倍数
                res.append(i)
        return res

    # 各自index
    x_number = k_number(x)
    y_number = k_number(y)

    # remove dumplicate
    x_number = set(x_number) - set(y_number)
    y_number = set(y_number) - set(x_number)

    x_len,y_len= len(x_number), len(y_number)

    nums = sorted(nums)
    # max - min
    ans = sum(nums[len(nums)-x_len:] ) - sum(nums[:y_len])
    return ans

def pdd_20240324_q1():
    n = int(input())
    a = list(map(int, input().split()))

    # dp
    dp = [[0] * n for _ in range(n)]

    # 长度为i的区间
    for i in range(n):
        dp[i][i] = a[i]     # nums 本身

    for length in range(2, n+1):   # 控制长度
        for i in range(n-length+1): # left
            j = i+length -1    # right

            take_left = a[i] + dp[i+1][j]
            take_right = a[j] + dp[i][j-1]

            dp[i][j] = max(
                take_left,take_right
            )

    # 最终所求的答案是在dp[0][n-1]
    print(dp[0][n-1])

def q2_20240811():
    n = int(input())

    tasks = []  # 具体的任务
    for i in range(n):
        s,d,p = list(map(int, input().split()))
        tasks.append([s,d,p,i])

    tasks.sort(key=lambda x:x[0])

    heap = []
    cur_time = 0    # 当前时间
    index = 0       # 指向下个任务index
    res = [0]* n

    while index < n or heap:    # 所有任务并未完成
        # 有任务但当前时间未达到
        if not heap and cur_time< tasks[index][0]:
            # 时间快进
            cur_time = tasks[index][0]  

        # 塞入所有到达的
        while index < n and tasks[index][0] <= cur_time:
            s, d, p, task_id = tasks[index]

            heapq.heappush(
                heap,
                (-p, task_id, s,d)
            )

            index += 1

        # 最高优先task
        neg_p,task_id,s,d = heapq.heappop(heap) # 弹出

        if index < n:
            # 获取下个任务时间
            next_time = tasks[index][0]

            # 能否干完
            if cur_time + d <= next_time:
                cur_time += d
                res[task_id] = cur_time
            else:
                # 当前任务只能先执行到下一个任务到达
                d -= next_time - cur_time

                cur_time = next_time
                heapq.heappush(heap,(neg_p,task_id, s, d))

        else:
            # 最后一个任务
            cur_time += d
            res[task_id] = cur_time

    print(res)

def q3_20260816():
    n = int(input())

    tasks = []
    for _ in range(n):
        task = list(map(int,input().split()))
        tasks.append(task)
    tasks.sort(key=lambda x:x[1])

    ends = [task[1] for task in tasks]
    # 动态规划
    dp = [0 * x for x in range(n)]

    # dp 主题逻辑
    for i in range(n):   
        # 手写第 0 位
        if i == 0:
            dp[i] = tasks[i][2]
            continue

        # 当前任务
        start = tasks[i][0]
        value = tasks[i][2]

        # 前 i 个任务中，有多少个 end <= start
        j = bisect_right(ends, start, 0, i)

        # 不选当前任务
        not_take = dp[i - 1]

        # 选当前任务
        if j == 0:
            take = value
        else:
            take = dp[j - 1] + value

        dp[i] = max(not_take, take)

    print(dp[-1])

def q2_20250914():
    day, order_num, max_day = map(int,input().split())
    prices = list(map(int,input().split()))
    deadlines = list(map(int,input().split()))

    deadlines.sort()    # 排序，早的先卖
    heap = []       # 最小堆    （price，day，remain）

    # 全局变量
    cur_day  = 1      # 记录当前天
    total_cost = 0

    for d in deadlines:
        # 插入heap
        while cur_day <= day and cur_day<=d:
            heapq.heappush(
                heap,
                (prices[cur_day], cur_day, max_day)
            )
            cur_day += 1

        # body
        if not heap:    # heap 空了
            print(-1)
        else:
            # 弹出今日信息
            price, cur_day, remain = heapq.heappop(heap)

            # 更新
            total_cost += price
            remain -= 1

            if remain >0:
                # 仍有继续售出
                heapq.heappush(
                    heap,
                    (prices[cur_day], cur_day, remain)
                )
    print(total_cost)

def q4_20260816():
    node, edge = map(int,input().split())
    nums = []

    for _ in range(edge):
        s,e,w = map(int,input().split())    # start/end/weight
        nums.append([s,e,w])

    # 动态规划
    dp = [1] * node     # 以第i条边为重点的最大边数是多少
    # ans = 0     # 最长边数

    for i in range(edge):
        # cur info
        c_s, c_e, c_w = nums[i]
        for j in range(i):   # prev
            p_s,p_e,p_w = nums[j]
            if p_e == c_s and p_w < c_w:
                dp[i] = max(dp[i], dp[j] +1)
    print(max(dp) if edge > 0 else 0 )




if __name__ == "__main__":
    q3_20260816()

