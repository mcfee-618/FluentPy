# coding:utf-8
"""
@author: mcfee
@description:
@file: test_yield_from1.py
@time: 2020/7/24 上午10:19
"""


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        try:
            new_num = yield average
            if new_num is None:
                break
            count += 1
            total += new_num
            average = total / count
        except GeneratorExit as _e:
            print("清理")
            return

    print("end")
    # 每一次return，都意味着当前协程结束。
    return total, count, average


# 委托生成器
def proxy_gen():
    # 如果GeneratorExit异常被抛给委派生产器，或者委派生产器的close()方法被调用，那么迭代器有close()的话也将被调用。
    total, count, average = yield from average_gen()
    print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)  # 预激协程
    calc_average.close()


if __name__ == '__main__':
    main()
