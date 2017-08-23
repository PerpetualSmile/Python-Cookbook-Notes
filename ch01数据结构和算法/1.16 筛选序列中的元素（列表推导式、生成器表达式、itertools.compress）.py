# 筛选序列中的元素, 序列中含有一些数据，我们需要提取出其中的值或者根据某种标准对序列做删减
# 列表推导式、生成器表达式、内建函数filter, 条件表达式， itertools.compress()

# 使用序列推导式（list comprehension）
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

# 适用房列表生成式的问题是如果原始输入非常大，那么结果就会很庞大，所以可以使用生成器表达式通过迭代的方法产生筛选的结果
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# 使用内建的filter函数, 可以处理比较复杂的和有异常的筛选
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

vals = list(filter(is_int, values))  # filter()返回的是一个迭代器
print(vals)


# 使用条件表达式，可以用新值替换掉不满足条件的值
clip_neg = [n if n > 0 else 0 for n in mylist]  # 注意这样的表达式，非常简洁漂亮
print(clip_neg)

# 使用筛选工具itertools.compress(), 接受一个可迭代对象以及一个布尔选择器序列作为输入
address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(address, more5)))

# 相当于一个位置的数据选择器，选出特定位置的数据
