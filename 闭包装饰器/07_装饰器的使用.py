import time


# 1 定义装饰器
def get_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('time:', end - start)
    return inner
# 2 装饰函数


# 要被装饰的函数
@get_time
def func():
    for i in range(10000):
        print(i)


func()
