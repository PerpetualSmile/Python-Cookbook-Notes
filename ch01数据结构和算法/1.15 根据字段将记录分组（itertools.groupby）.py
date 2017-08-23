# 根据字段将记录分组, 根据某个特定的字段（比如说日期）来分组迭代数据
# 使用itertools.groupby()函数对数据进行分组
from operator import itemgetter
from itertools import groupby


rows = [
    {'address': '5142 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 N CLARK', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N CLARK', 'date': '07/02/2012'},
    {'address': '1060 N CLARK', 'date': '07/02/2012'},
    {'address': '4801 N CLARK', 'date': '07/01/2012'},
    {'address': '1039 N CLARK', 'date': '07/04/2012'},
]

# 公共键排序，前面有讲
rows.sort(key=itemgetter('date'))

# 分组
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# groupby()通过扫描序列找出相同的值（或是由Key参数指定）的序列项
# groupby()创建了一个子迭代器，而在每次迭代时都会返回一个值和子迭代器
# 注意groupby()只能检查连续的项，因此在使用前需要先排序
# 如果只是为了随机访问，那么使用defaultdict()构建一个一键多值的字典可能会更好, 前面1.6讲到了这个字典
from collections import defaultdict


print('-' * 100)
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
# 如果不考虑内存方面的因素，后面第二种方法要比第一种方便快，因为不需要排序
