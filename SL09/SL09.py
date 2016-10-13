# -*- coding: utf-8 -*-
import random

random1 = []
result = []
judge = []


def redpacket(people, money):
    remain = people
    remain_money = money
    b = True
    while b:
        for i in range(people):
            # 在一个list中添加0-1的随机数
            random1.append(random.random())
            # 算出和
        s = sum(random1)

        for i in range(people):
            remain -= 1
            if remain >= 1:
                # 求加权后的前people-1个红包值
                a1 = round(random1[i] / s * remain_money, 2)
                result.append(a1)
                remain_money -= a1
            else:
                # 最后一个人的红包是总数减去其他的
                result.append(round(money - sum(result),2))
        # 判断最小红包金额是否大于一分钱
        if min(result) >= 0.01:
            b = False
    return result


people = input('How many people:')
money = input('How much:')
redpacket(people, money)
print result
print sum(result)