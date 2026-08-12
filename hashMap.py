from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]):
    # Leetcode 49
    # 哈希表 + sorted(strs)获得唯一key
    # 第二种: 字母表计数。 相同计数字母表的为同一组
    hash_map = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        hash_map[key].append(word)

    return list(hash_map.values())

def isAnagram(s: str, t: str) -> bool:
    hashmap = defaultdict(int)

    for i in s:
        hashmap[i] += 1

    for i in t:
        hashmap[i] -= 1

    if all(v == 0 for v in hashmap.values()):
        return True
    return False

# shopee
def SortSubStringToBuildPhoneNum(phoneNum, cardListArray) :
    # write code here
    dict_ = {
        "0":0,
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
    }   

    # 构造 dict
    dictPhone = dict_.copy()
    for i in range(len(phoneNum)):
        dictPhone[(phoneNum[i])] += 1

    res = []
    for obj in cardListArray:
        # 判断是否有字母
        if any(element not in dict_ for element in obj):
            res.append(-1)
            continue

        # 无字母
        dictTemp = dict_.copy()
        for i in range(len(obj)):
            dictTemp[(obj[i])] += 1
        if dictTemp == dictPhone:
            res.append(1)
        else: 
            res.append(0)

    return res

if __name__ == "__main__":
    print(isAnagram("rat","car"))