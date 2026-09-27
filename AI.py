def gradiant_descent(train_x, train_y,lr,epoch):
    # 梯度下降
    n = len(train_x)  # 训练集的大小

    # 优化的参数
    w = 0.0
    b = 0.0

    for i in range(epoch):
        print(f"The {i} epoch: ")
        dw = 0.0
        db = 0.0
        loss = 0.0

        # 全量训练
        for x in range(n):
            y = w * x + b
            error = train_y - y

            loss  += error ** 2

            # dw & db
            dw += 2*train_x[x] * error
            db += 2* error

        # 平均化
        dw = dw/n
        db = db/n
        loss = loss/n

        # lr
        w -= lr*dw
        b -= lr * db

    return w,b
    

def solve():
    num = int(input())  # apple number

    apple_list = []
    for _ in range(num):
        row=  list(map(int, input().split()))   # x, y, t
        apple_list.append(row)  
 
    dp=[0] * num     # dp[i]=以第i颗苹果结尾时，最多被砸多少次

    # 转化成二维，把y和时间相加
    apple_list_2d = []
    for i in apple_list:
        x,y,t = i
        apple_list_2d.append([x, y+t])

    # rank
    apple_list_2d.sort(key=lambda x: x[1])

    # 2d done
    """
    展示2D
    """
    for temp in apple_list_2d:
        print((temp[0],temp[1]))

    # body
    for apple in range(num):
        print(f"apple_id: {apple}")

        # m:x && n:y+t
        apple_loc, apple_time = apple_list_2d[apple]
        
        # 以当前apple 作为第一路线
        if abs(apple_loc) <= apple_time:
            dp[apple] = 1

        # 检查之前的apple是否接得上
        for prev in range(apple):
            prev_loc, prev_time = apple_list_2d[prev]

            if dp[prev] == 0:
                continue    # 该苹果没被接到过

            if abs(apple_loc-prev_loc) <= apple_time-prev_time:     # 后者大于0 as sort
                dp[apple] = max(
                    dp[apple],
                    dp[prev] + 1
                )
    print(max(dp))

print(solve())
        
        

    
        
     


