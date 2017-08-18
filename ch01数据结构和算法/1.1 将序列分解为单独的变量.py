# 任何可迭代对象都可以通过赋值操作分解为普通变量
p = (4, 5)
x, y = p
print(x, y)
print("----------")

data = ['ACME', 50, 91.1, (2012, 12, 21)]
a, b, c, d = data
print(a)
print(b)
print(c)
print(d)
print("----------")


# 只要对象可以迭代就可以进行分解
# 字符串、文件、迭代器、生成器均可
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)
print("----------")


# 选一个用不到的变量名丢弃某些值
data = ['ACME', 50, 91.1, (2012, 12, 21)]
a, shares, price, b = data
print(shares, price)

