# 找出序列中出现次数最多的元素
# 使用collections.Counter

# 找出列表中出现最频繁的单词
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look',
         'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under'
         ]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)


# 可以给Counter对象提供任何可哈希对象作为输入，在底层实现中，Counter是一个字典，在元素和出现次数间作了映射
print(word_counts['look'])   # 4


# 如果要增加计数的单词，两种方法
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1


# 或者直接使用update方法
word_counts.update(morewords)

print("-" * 100)
# Counter的另外特性: 可以轻松使用各种运算操作符
a = Counter(words)
for i, j in a.items():  # Counter是字典
    print(i, j)
print("-" * 100)
b = Counter(morewords)
print("a:", a)
print("b:", b)
c = a + b
print("a + b:", c)
print("a - b", a - b)


# 所以当面对任何对数据制表或者计数的问题时，使用Counter比自己手写算法更方便



