import heapq
from collections import defaultdict


def topKFrequent(nums, k):
	frequency_map = defaultdict(int)
	for num in nums:
		frequency_map[num] += 1

	heap = []
	for num, frequency in frequency_map.items():
		heapq.heappush(heap, (frequency, num))
		if len(heap) > k:
			heapq.heappop(heap)

	result = []
	while heap:
		result.append(heapq.heappop(heap)[1])

	return result[::-1]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))