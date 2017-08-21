# 通过公共键对字典列表排序
# 使用operator模块中的itemgetter
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print('-' * 100)
print(rows_by_uid)

# itemgetter()函数还可以接受多个参数
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print('-' * 100)
print(rows_by_lfname)

# operator.itemgetter()可以是字典键的名称。用数字表示的列表的索引或是任何可以传给对象__getitem__（）的值，如果传多个标记给itemgetter()，那么它产生的可调用对象将返回一个包含所有元素在内的元组。


# 前面用到在min、max、sort的时候用到的key是用lambda匿名函数写的
rows_by_fname = sorted(rows, key=lambda x: x['fname'])
rows_by_lfname = sorted(rows, key=lambda x: (x['lname'], x['fname']))

# 在效率性能上，itemgetter快一些，因此在考虑性能问题时最好使用itemgetter
# 本节的技术同样适用于min、max
print(min(rows, key=itemgetter('uid')))



