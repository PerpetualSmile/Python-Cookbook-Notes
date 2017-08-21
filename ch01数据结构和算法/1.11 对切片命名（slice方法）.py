# 对切片命名
# 避免重复使用硬编码的切片，比如有一些代码是从字符串的固定位置中取出具体数据

record = "askdljkajwrmhvjbxmvksioiqfjgnsk"
A = slice(5, 10)
B = slice(15, 20)
c = record[A] + record[B]
print(c)


items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A = slice(1, 9, 2)
print(items[A])

items[A] = [0, 0, 0, 0]
print(items)

a = items[A]
a.sort()
print(items)

a = items
a.sort()
print(items)


# slice对象的一个方法是indices(size),作用为将切片映射到特定大小的序列上，返回一个元组（start, stop, step），所有的值都被恰好限制在边界以内

print("-" * 100)
s = "HelloWorld"
print(A.indices(len(s)))
for i in range(*A.indices(len(s))):  # 注意此处*的用法，*其实相当于解除序列化，比如前面的zip(*item)是解除压缩，再比如传入多个参数时使用*
    print(s[i])


