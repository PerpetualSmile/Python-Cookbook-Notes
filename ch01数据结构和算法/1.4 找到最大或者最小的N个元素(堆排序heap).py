# 在某个集合中找到最大或者最小的N个元素
# 使用heapq模块中的nlargest()和nsmallest()

import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]
print("-" * 100 + '1')


# 使用参数key可以处理更复杂的数据结构的排序
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)
print("-" * 100 + '2')


# 利用堆排序找出最大最小（堆顶的元素总是最大或者最小）
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)
# nums[0]总是最小的
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
# 时间复杂度为O(logN)


# 总结：N = 1 时(只是简单地找最大最小)用min(), max()更快
# 当N相对较小的时候， nlargest()和nsmallest()最实用
# 如果是N和集合本身差不多大小，用sorted(items)[:N]或者sorted(items)[-N:]最好
