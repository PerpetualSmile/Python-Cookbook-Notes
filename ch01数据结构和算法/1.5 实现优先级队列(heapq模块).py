# 实现优先级队列, 它能够以给定的优先级来对元素排序， 且每次pop操作时都会返回优先级最高的那个元素
# 使用heapq模块
import heapq


# 简单的优先级队列
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))   # ()元组是个表示优先级的表达式，先比较前面的，若前面相同则再比较下一个，以此类推
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # push的是一个元组，这边返回的也是元组，前面都是表示优先级的，最后一个才是我们真正需要的


# 使用优先级队列
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())  # bar
print(q.pop())  # spam
print(q.pop())  # foo
print(q.pop())  # grok
print('-'*100 + '1')

# 说明:index实现了稳定排序，即优先级相同的根据插入的先后出队，如上面的foo和grok


# 补充：如果以元组（priority, item）形式表示那么只要优先级不同即可直接进行比较，比较（）是先比较前面的元素
# 同样列表list和tuple一样可以用 < > 比较
a = (1, Item("foo"))
b = (2, Item("bar"))
print(a < b)  # True

c = (1, Item("bar"))
# print(a < c) # 报错，因为第二个元素Item不可以比较

a = [1, 1, 1, 1]
b = [1, 1, 1, 2]
print(a < b)
