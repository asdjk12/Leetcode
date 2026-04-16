from collections import deque
import heapq
from typing import List

class Search(object):
    def bfs(self, graph, start):
        # queue and set
        visited = set()
        queue = deque()

        #start node
        visited.add(start)
        queue.append(start)

        # queue非空
        while queue:
            # FIFO
            current = queue.popleft()  # 取出node并展开其child，故：expansion

            # child
            for neighbour in graph[current]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour) # 发现一个新节点并将它放入node,故：generation
        return visited
    
    def dfs(self, graph, start):
        # stack and set
        visited = set()
        stack = [start]

        # stack 非空
        while stack:
            # LIFO
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                for neighbour in reversed(graph[current]):
                    stack.append(neighbour)
        return visited

    def uniformCostSearch(self, graph, start,goal):
        # Initialization 
        priority_queue = [(0,start)] # pq根据第一行的value来弹出
        #    结构: {node: (g, parent)}
        visited = {start, (0,None)}

        total_cost = 0

        while priority_queue:
            # 弹出当前的最小cost value
            current_cost, current_node = heapq.heappop(priority_queue)

            if current_node == goal:
                return current_cost, Search.reconstruct_path(visited, start, goal)
            
            for nei_cost, nei_node in graph[current_node]:
                # element: (total_cost, nei_node)
                total_cost = current_cost + nei_cost
                # 2 rules: 1: not visited and 2: less cost
                if nei_node not in visited or total_cost< visited[nei_node]:
                    visited[nei_node] = (nei_node,(total_cost,current_node))
                    heapq.heappush(priority_queue,(total_cost, nei_node))

        return None, None
    
    def reconstruct_path(self, visited, start, goal):
        # 倒序path，最后inverse
        path = []
        node = goal

        while node is not None:
            path.append(node)
            node = visited[node][1]
        return list(reversed(path))

def binarySearch(nums: List[int], target: int) -> int:
    # leetcode 704
    """
    nums是顺序的，因此二分查找。
    双指针 + mid, 无限逼近 注意index
    """
    
    left = 0
    right = len(nums)-1

    while left <= right:
        # mid 判断
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid -1

    return -1

def removeElement(nums: List[int], val: int) -> int:
    # leetcode 27
    """
    交换指针/快慢指针(两种都可)
    """

    """
    # 交换版本
    left = 0
    right = len(nums)

    while left <right:
        # 找到要被替换的val
        if nums[left] == val:
            nums[left] = nums[right-1]
            right -=1
        else:
            left += 1

    return left"""

    # 快慢指针
    """
    快指针遍历list, 慢指针构建答案区。 
    快指针在nums[fast] == val的时候直接skip该元素,相当于丢弃该元素.最后未被丢弃的就是扔进slow，被构建成答案区
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow +=1
    return slow

def sortedSquares(nums: List[int]) -> List[int]:
    #leetcode 977
    """
    双指针：从后向前推进。最大平方只会在最左or最右出现。
    """
    ans = [0] * len(nums)

    left = 0
    right = index = len(nums) -1  # index 参数用于从后向前推
    
    while left <= right:
        if nums[left] ** 2 >= nums[right] ** 2:
            ans[index] = nums[left] ** 2
            left += 1
        else:
            ans[index] = nums[right] ** 2
            right -= 1

        index -= 1
    return ans
            
        


if __name__ == "__main__":
    print(sortedSquares([-7,-3,2,3,11]))


