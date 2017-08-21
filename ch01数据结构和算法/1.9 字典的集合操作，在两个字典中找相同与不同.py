# 找出两个字典相同的键、相同的值，对字典使用表达式进行过滤
# 字典中items和keys对象支持集合操作，比如并集、交集、差集


a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "w": 10,
    "x": 11,
    "y": 2
}

print(a.keys()&b.keys())    # {'x', 'y'}
print(a.items()&b.items())  # {('y', 2)}
# print(a.values()&b.values()) # ERROR
print(a.keys() - b.keys())  # {'z'}


# 根据已有字典创建一个新字典，且过滤掉某些键
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)  # {'x': 1, 'y': 2}

# 在需要对字典作常见的集合操作时，不必转化为集合，可以直接操作，但是对values的集合操作是不可以的，因为有些键的值可能一样

