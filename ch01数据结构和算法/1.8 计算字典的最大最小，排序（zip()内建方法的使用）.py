# 与字典有关的计算问题， 求最大值、最小值、排序等
# 使用zip()


prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75
}

# 字典找最大最小值
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)  # (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)  # (612.78, 'AAPL')

# 字典排序
prices_sorted = sorted(zip(prices.values(), prices), reverse=True)
print(prices_sorted)

# 注意：zip创建的是一个迭代器，他的内容只能被使用一次
prices_and_names = zip(prices.values(), prices)
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError

# 找最大最小键
print(min(prices))
print(max(prices))

# 找最大最小值
print(min(prices.values()))
print(max(prices.values()))

# 找到最大最小值对应的键
    # 使用key

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

# 如果既要知道最大最小值对应的键又要知道对应的值， 必须多一步查找
min_value = prices[min(prices, key=lambda k: prices[k])]

# 所以使用zip更为快捷方便
# 注意的是zip比较时当值相同时则根据键的大小来排序，这个也是根据元组比较大小的特点决定的，前面有涉及的

print("-" * 100)
# 补充zip的用法
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip(a, c)))  # [(1, 4), (2, 5), (3, 6)] 匹配的长度和最短的相同
zipped = zip(a, c)
print(list(zip(*zipped)))  # [(1, 2, 3), (4, 5, 6)] 解除压缩unzip
