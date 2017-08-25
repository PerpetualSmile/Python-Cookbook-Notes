# 针对任意多的分隔符拆分字符串
# 我们需要将字符串拆分为不同的字段，但是分隔符（以及分隔符之间的空格）在整个字符串中并不一致
# 使用re.split()
# 字符串对象的split()只能处理非常简单的情况，而且不支持多个分隔符，对分隔符周围可能存在的空格也无能为力
import re


line = 'asdf fjdk; afed, fjek,asdf,    foo'
print(line.split())  # ['abc aa', "bb,cc | dd(xx).xxx 12.12'\txxxxx"]
print(re.split(r'[;,\s]\s*', line))  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 使用re.split()时要小心正则表达式中的捕获组（capture group）是否包含在了括号中。如果使用了捕获组，那么匹配的文本也会包含在最终结果中
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
values = fields[::2]
delimiters = fields[1::2] + ['']
print(delimiters)  # [' ', ';', ',', ',', ',', '']
print(''.join(v + d for v, d in zip(values, delimiters)))  # asdf fjdk;afed,fjek,asdf,foo

# 如果不想再结果中看到分隔字符，但仍想用括号对正则表达式模式进行分组，那么要确保用的是非捕获组，以?:...的形式指定
print(re.split(r'(?:;|,|\s)\s*', line))  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

print('-' * 100)


# str.split（）和re.split（）对比


# str.split不支持正则及多个切割符号，不感知空格的数量，比如用空格切割，会出现下面情况。
s = "aa bb   cc"
print(s.split(" "))  # ['aa', 'bb', '', '', 'cc']

# str.split()不带参数时默认以空格分配，而且取出多余的空格符
print(s.split())  # ['aa', 'bb', 'cc']

# str.split()只支持单个字符切割，输入多个字符之后是以字符串分隔
print(s.split("bb"))  # ['aa ', '   cc']

# str.split()的切割，分隔符前后都必须有结果，即使是连续的分隔符，中间必须有空字符“”
print(s.split("b"))  # ['aa ', '', '   cc']


# re.split()支持正则表达式以及多个字符切割
s = "abc aa;bb,cc | dd(xx).xxx 12.12'\txxxxx"

# 空格切割
print(re.split(r' ', s))  # ['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'\txxxxx"]

# 将空格放可选框内[]内
print(re.split(r'[ ]', s))  # ['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'\txxxxx"]

# 按所有空白字符来切割：\s（[\t\n\r\f\v]）\S（任意非空白字符[^\t\n\r\f\v]
print(re.split(r'[\s]', s))  # ['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'", 'xxxxx']

# 多字符匹配
print(re.split(r'[;,]', s))  # ['abc aa', 'bb', "cc | dd(xx).xxx 12.12'\txxxxx"]
print(re.split(r'[;,\s]', s))  # ['abc', 'aa', 'bb', 'cc', '|', 'dd(xx).xxx', "12.12'", 'xxxxx']

# 使用括号捕获分组的适合，默认保留分割符
print(re.split('([;])', s))  # ['abc aa', ';', "bb,cc | dd(xx).xxx 12.12'\txxxxx"]

# 去掉分隔符，加?:
print(re.split(r'(?:;)', s))  # ['abc aa', "bb,cc | dd(xx).xxx 12.12'\txxxxx"]




