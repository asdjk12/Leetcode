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

if __name__ == "__main__":
    print(isAnagram("rat","car"))