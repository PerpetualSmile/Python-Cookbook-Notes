# 将名称映射到序列的元素中, 通过名称访问序列中的元素而不是位置
# 使用collections.namedtuple 命名元组
# collections.nametuple 是一个工厂方法，返回的是python中标准元组类型的子类，返回的是一个可实例化的类
from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub, sub.joined, sub.addr)


# namedtuple虽然看起来是类，但它的实例与普通元组是可以互换的，支持所有普通元组的操作，例如索引和分解
addr, joined = sub
print(addr, joined)


# 通过位置来引用元素常常使得代码的表达力不够强，而且依赖于记录的具体结构，在处理大型的元组列表时，一旦某个元组中位置与其他不一样，那么程序很容易崩溃
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
        # total += rec[1] * rec[2]
    return total


# namedtuple的另外一种可能用法是作为字典的替代，后者需要更多的空间，如果要构建涉及字典的大型数据结构，使用namedtuple更加高效，但是namedtuple是不可变的
# 如果需要修改任何属性，可以通过实例的_replace()方法来实现, 该方法创建一个全新的命名元组
s = Stock('ACME', 100, 123.45)
# s.shares = 75  # ERROR
s = s._replace(shares=75)
print(s)


# _replace()方法还可以作为一种简便的方法填充具有可选或者缺失字段的命名元组
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_default = Stock('', 0, 0, None, None)


def dict_to_stock(s):
    return stock_default._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

# 最后，如果我们的目标是定义一个高效的数据结构，而且将来会修改各种属性，那么使用namedtuple不是最佳选择，可以考虑定义一个使用__slots__属性的类（8.4节）

