"""
[([5, 5, 5], '1'), ([8, 7, 6], '3'), ([4, 5, 6], '1'), 
([2, 1, 0], '2'), ([7, 8, 9], '1'), ([0, 1, 2], '2'), 
([9, 8, 7], '3'), ([3, 3, 3], '2'), ([6, 4, 2], '3'), ([1, 2, 3], '2')] 
根据第二列排序，要求古法编程
"""

def qucik_sort(data):
    # 特殊情况
    if len(data) <= 1:
        return data
    
    # 基准
    pivot = int(data[0][1])
    
    # 存储数据
    left = []
    right = []

    for i in range(len(data)):
        if int(data[i][1]) < pivot:
            left.append(data[i])
        else:
            right.append(data[i])

    return qucik_sort(left) + [data[0]] + qucik_sort(right)

if __name__ == "__main__":
    data = [([5, 5, 5], '1'), ([8, 7, 6], '3'), ([4, 5, 6], '1'), 
            ([2, 1, 0], '2'), ([7, 8, 9], '1'), ([0, 1, 2], '2'), 
            ([9, 8, 7], '3'), ([3, 3, 3], '2'), ([6, 4, 2], '3'), ([1, 2, 3], '2')] 
    print(qucik_sort(data=data))

    

        