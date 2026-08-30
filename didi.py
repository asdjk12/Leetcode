import sys

def solve(N,K,a):
    ans = 0
    for i in range(N+1):    # 左card 个数
        for j in range(N-i+1):    # 右card 个数
            take = i + j     # 当前次数
            
            if take > K:    # 超过total
                continue
            
            # rebuild 手牌
            cards = a[:i]    # 左手牌
            if j >0:    # 右手牌有效？
                cards += a[N-j:]    # 左+右 手牌

            print("LEFT=",i, "RIGHT=",j, "cards=",cards)
            
            sum_ = sum(cards)    # 当前分数
            
            # 剩余action no.
            remain = K-take 
            
            negatives = sorted(x for x in cards if x<0)
            
            # 舍弃 negative value
            for k in range(min(remain, len(negatives))):     # 可舍弃次数
                sum_ -= negatives[k]    # -(-1)
                
            ans = max(sum_, ans)
    print(ans)


if __name__ == "__main__":
    ans = solve(
        N = 6, 
        K= 4, 
        a=[-10,8,2,1,2,6],
    )

    

    
    