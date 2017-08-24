# 将多个映射合并为单个映射
# 使用collections.ChainMap
from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'], c['y'], c['z'])
print(len(c))
print(list(c.keys()))


# 如果有重复的键，那么会采用第一个映射中对应的值，因此c['z'] = 3
# 同样的，修改映射的操作总是会作用在第一个映射结构上
c['z'] = 10
c['w'] = 4
del c['x']
print('-' * 100)
print(a)
print(b)
# del c['y']  # ERROR


# ChainMap与带作用域的值，比如编程语言中的变量（全局变量、局部变量等）一起工作时特别有用
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)


# ChainMap 的一个替代方案是利用字典的update()方法将多个字典合并在一起
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'], merged['y'], merged['z'])
b['y'] = 19
print(merged['y'])

# 这么干可以，但是需要另外构建一个单独的字典，否则就会破坏原始数据
# 另外，如果其中任何一个原始字典做了修改，并不会反映到字典中，不具有同步更新能力
# 而ChainMap使用的就是原始字典

