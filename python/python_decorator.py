# def deco(func):
#     print(f"收到的func.__name__ = {func.__name})")
#     return "啊哈，我把你替换咯，而且还返回一个string，气不气"
#
#
# @deco
def hello():
    return "world"


print(f"1: {hello}")
print(f"2: {hello()}")



print("============")


def deco(func):
    print(f"收到的func.__name__ = {func.__name__})")
    return "啊哈，我把你替换咯，而且还返回一个string，气不气"


@deco
def hello():
    return "world"


print(f"3: {hello}")
print(f"4: {hello()}")# 注意看，这一行运行会报什么错误


