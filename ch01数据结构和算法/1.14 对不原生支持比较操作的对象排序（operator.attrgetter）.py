# 对不原生支持比较操作的对象排序

# 使用lambda


class User:
    def __init__(self, use_id):
        self.use_id = use_id

    def __repr__(self):
        return 'User({})'.format(self.use_id)

users = [User(23), User(3), User(99)]
print(sorted(users, key=lambda x: x.use_id))  # [User(3), User(23), User(99)]

# 使用operator.attrgetter()
from operator import attrgetter
print(sorted(users, key=attrgetter("use_id")))

# 通常来说使用attrgetter()要更快一些，而且具有同时提取多个字段的能力，前面讲公共键排序时类似
# 同样也适用于min、max等函数的key
print(min(users, key=attrgetter('use_id')))
