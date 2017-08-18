# 从任意长度的可迭代对象中分解元素
# 问题：需要从某个对象中分解出N个元素，但对象的长度可能超过N
# 解决：使用“*元素”表达式
# *式的语法


# 去掉最高分和最低分取平均值，但不知道中间多少个值
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

grades = [1, 2, 3, 4, 5, 6, 7, 8, 1000]
print(drop_first_last(grades))
print("----------1")

# 对最近一个季度的销售额度和前7个季度的平均值做比较
sales_record = [1, 2, 3, 4, 5, 6, 7, 8]
*a, b = sales_record
a_avg = sum(a)/len(a)
print(a)
print(b)
print(sum(a)/len(a), b)
print("----------2")

# 迭代一个变长的元组序列
records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3, 4),
]

def do_foo(x, y):
    print("foo", x, y)

def do_bar(a):
    print("bar", a)

for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":                  # *式不加*则是一个list看待，可以进行列表的操作
        do_bar(*args)                   # 不加*就代表一串值，不能进行列表的操作， **同理
print("----------3")


# 和字符串处理操作相结合，比如splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname)
print(sh)
print("----------4")


# 总结：*式可以轻松将一个序列分解为头部，中部，尾部
# 可以用于丢弃序列中某些不需要的值，提取有用的值

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
