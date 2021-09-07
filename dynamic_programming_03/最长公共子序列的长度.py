# coding:utf-8


"""
问题描述：
  给定两个字符串s1和s2， 返回两个字符串的最长公共子序列。
  一个字符串的子序列是指由原始字符串在不改变字符的相对顺序的情况下，删除某些字符（不删除任何字符也可以）之后形成的字符串。
  比如：ADE是ABCDEF的子序列，但是AED不是它的子序列。
  两个字符串的公共子序列是这两个字符串所共同拥有的子序列。若没有公共子序列，返回0.


"""



"""
思路解析：
 假设s1的字符串的前m位为x={x1,x2,...xm}， 取s2的前n位y={y1,y2...yn}， 如果要判断x与y的最长公共子序列长度， L(i, j)代表x的前i个字符与y的前j个字符的最长公共子序列长度。
 当xm=yn时，x与y的最长公共子序列长度为1+L(m-1,n-1);
 当xm!=yn时，x与y的最长公共子序列长度为L(m, n-1)和L(m-1, n）中的较大值。状态转移方程也清晰了，因此L(m,n)分3中情况：
 1） 当m=0或n=0， L(m,n)=0
 2)  当m、n均大于0， 其xm=yn时， L(m,n)=L(m-1,n-1) + 1
 3)  当m、n均大于0,其xm!=yn时， L(m,n)=max(L(m-1, n)， L(m, n-1))


"""


"""
变量定义：
s1、s2表示给定的两个字符串
array: 动态规划过程中保存状态的二维数组
len1: 表示s1的长度
len2: 表示s2的长度

初始化：定义len1*len2的二维数组，初始值均为0


"""


def lonest_subsequence(s1, s2):

    len1 = len(s1)
    len2 = len(s2)

    # len1 + 1 与len2+1，表示字符串可能为空，相当于在每个字符串添加一个特定的空字符
    array = [[0] * (len2+1) for _ in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1,len2+1):
            if s1[i-1] == s2[j-1]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i-1][j], array[i][j-1])
    return array[len1][len2]

s1 = "ABCB"
s2 = "BDCA"

print(lonest_subsequence(s1, s2))


s1 = "ABC"
s2 = "ABC"

print(lonest_subsequence(s1, s2))

s1 = "ABC"
s2 = "RTY "

print(lonest_subsequence(s1, s2))



















