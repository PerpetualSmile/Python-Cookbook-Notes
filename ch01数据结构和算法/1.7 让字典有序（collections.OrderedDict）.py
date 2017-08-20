# 让字典保持有序，在对字典做迭代或序列化操作时也能控制其中元素的顺序
# collections.OrderedDict类
from collections import OrderedDict


d = OrderedDict()  # 严格按照初始的添加顺序进行
d["foo"] = 1
d["bar"] = 2
d["grok"] = 4
d["spam"] = 3


for key in d:
    print(key, d[key])

# 注意：OrderedDict的大小是普通字典的2倍多，慎重使用


