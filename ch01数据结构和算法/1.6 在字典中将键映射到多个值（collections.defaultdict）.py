# 在字典中将键映射到多个值上
# 使用collections 模块中的 defaultdict
from collections import defaultdict


d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d['b'].append(1)
d['c']
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [1], 'c': []})
# defaultdict会自动创建字典表项，即使还没有赋值
print('-' * 100 + '1')


# 普通字典也可以这么干, 但不够简洁
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)  # d['a'].append(2)
d.setdefault('b', []).append(1)
print(d)
print('-' * 100 + '2')





