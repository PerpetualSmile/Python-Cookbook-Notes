# 保存最后N个元素： 在迭代或其他处理的过程中对最后几个记录做一个有限的历史记录统计
# 使用collection.deque（双向队列）
# deque(maxlen=N)创建一个固定长度的队列，当有新纪录加入而队列已经满时自动移除最老的记录

from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)                # deque([1, 2, 3,], maxlenn=3)
q.append(4)
print(q)                # deque([2, 3, 4,], maxlenn=3)
print("-" * 100 + "1")


# 完整的简单队列结构，使用appendleft入（最左边加入元素），pop出队
q = deque()             # 不指定maxlen默认为无限队列
q.append(1)
q.append(2)
q.append(3)
print(q)                # deque([1, 2, 3])

q.appendleft(4)
print(q)                # deque([4, 1, 2, 3,])

print(q.pop())          # 3
print(q.popleft())      # 4
print(q)                # deque([1, 2])


# 队列两端添加或者弹出的时间复杂度都是O（1）
# 当从列表的头部插入或者移除元素时， 列表复杂度为O（N）
# python各个数据结构时间复杂度比较 http://www.orangecube.net/python-time-complexity
# https://wiki.python.org/moin/TimeComplexity