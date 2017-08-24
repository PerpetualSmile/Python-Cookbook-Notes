# 同时对数据做转换和换算
# 在函数中使用生成器表达式


# 计算平方和
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# 某个文件夹下是否存在.py文件
import os
files = os.listdir('D:\Desktop\github\Python-Cookbook-Notes\ch01数据结构和算法')
if any(name.endswith(".py") for name in files):
    print("There be python!")
else:
    print("Sorry, no python.")


# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(",".join(str(x) for x in s))


# Data reduction 换算
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]
min_shares = min(portfolio, key=lambda x: x['shares'])
print(min_shares)
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)


# 当把生成器表达式作为函数的单独参数时在语法上有微妙之处：不必重复使用括号
# 下面代码效果一样
s = sum((x * x for x in nums))
s = sum(x * x for x in nums)
# 比起创建一个临时序列，使用生成器做参数更为高效优雅

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
# 这种方法效果较差，创建了只用一次的临时列表，内存占用太多
# 基于生成器的解决方案可以以迭代的方式转换数据，因此在内存使用上更加高效

