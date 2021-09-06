# coding:utf-8

"""
斐波那契数列的实现

fib(i)={1, i< 3; fib(i-1) + fib(i-2) i>=3;

实现方式两种：
1） 递归算法，按照上述方式定义的公式进行实现， 会有重叠子问题，重复计算；递归问题：自顶向下
2） 动态规划，自底向上，避免重复计算，需要额外的空间来保存中间结果



"""

# 递归算法求解

def fib(n):
    if n < 1:
        return 0

    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)


# 动态规划求解

def fib(n):
    l= [0, 1, 1]
    for i in range(3, n+1):
        l.append(l[i-1] + l[i-2])
    return l[n]












