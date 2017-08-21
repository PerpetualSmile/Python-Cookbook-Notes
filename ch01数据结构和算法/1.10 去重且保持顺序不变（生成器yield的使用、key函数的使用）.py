#  从序列中移除重复元素，且保持原顺序不变


# 如果序列中的值是可哈希的（hashable），那么这个问题可以通过使用集合和生成器轻松解决:

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 如果元素时不可哈希的对象，需要加入关键字参数key
def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 注意这种风格代码，非常简洁漂亮
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe1(a, key=lambda x: (x['x'], x['y']))))
print(list(dedupe1(a, key=lambda x: x['x'])))

# 如果只是去重，那么通常最简单的方法就是构建成集合
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))

# 但是会打乱原本的顺序，不够通用
# 本节函数对生成器的使用告诉我们函数要尽可能地通用（不必绑在列表上使用）
