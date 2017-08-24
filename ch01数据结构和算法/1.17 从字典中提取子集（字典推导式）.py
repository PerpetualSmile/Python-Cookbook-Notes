# 从字典中提取子集
# 字典推导式（dictionary comprehension）
prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75
}

# 价格大于200的
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# 其他写法
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
# 运行效率不如第一种