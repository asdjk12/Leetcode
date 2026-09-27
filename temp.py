from collections import deque

def solve():
    node_num =  int(input())
    tree = [[] for _ in range(node_num+1)] # 保留root

    for _ in range(node_num-1):         # n个node， 会有n-1 条edge
        u,v = map(int,input().split())

        # 相互连接
        tree[u].append(v)
        tree[v].append(u)

    # tree done

    # dist 用于表示node 收到指令的时间，
    # -1 是为了检测是否收到过，
    # node_number +1 是为了匹配node 编号
    dist = [-1] * (node_num +1)     
    dist[1] = 0

    queue = deque([1])    # 初始化
    while queue:
        cur = queue.popleft()   # 弹出当前node

        # 获取当前node的子节点
        for childs in tree[cur]:
            if dist[childs] == -1:  # 未接收到指令
                dist[childs] = dist[cur] +1     # 下一秒接收
                queue.append(childs)

    # time
    max_time = max(dist[1:])

    # cnt
    cnt = 0
    for i in range(1, node_num+1):
        if dist[i] == max_time:
            cnt += 1
    print(max_time, cnt)

print(solve())