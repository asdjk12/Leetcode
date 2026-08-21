import heapq
from collections import Counter

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class solutions:
	def findKthLargest(self, nums, k):
		# 建堆
		heapq.heapify(nums)
		for _ in range(len(nums)-k+1):
			res = heapq.heappop(nums)
		return res

	def topKFrequency(self, nums, k):
		# 转化频率
		freq = Counter(nums)

		# 构造
		res = []
		for (value, count) in freq.items():
			if len(res) < k:
				heapq.heappush(res,(count,value))
			else:
				if count > res[0][0]:
					heapq.heappop(res)	# 弹出
					heapq.heappush(res,(count,value))
		return [value for (count, value) in res]

	def mergeKLists(self, lists):
		heap = []
		for (idx, node) in enumerate(lists):
			if node:
				heapq.heappush(heap, (node.val, idx, node))		# 头节点放第一个

		# listNode
		dummy = listNode(0)
		cur = dummy

		# 直到None
		while heap:
			val, idx, node = heapq.heappop(heap)		# 出来最小的
			cur.next = node		# update
			# listNode move
			cur = cur.next
			node = node.next

			if node:
				heapq.heappush(heap, (node.val, idx, node))

		return dummy.next