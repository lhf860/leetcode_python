# coding:utf-8


"""
最长回文子串：二维动态规划的问题，提供了两种方案：1）动态规划  2）空心扩展法【优化方法】


问题定义：

    给定一个字符串s，找到s中最长的回文子串，回文子串即从头到尾正向读和从尾向头逆向读是完全相同的字符串。

思路：
1、找到子结构
   对于回文子串（前提）， 从头部和尾部去掉相同数量的字符，中间部分必定是一个回文字符串；
   对于回文子串来说，其子结构就是其中间部分仍未回文子串。
   所以可以用一个二维数组来表示本字符串的两位质检是否是回文子串，在初始化化时默认只有二维数组的对角线上是TRUE，其余默认为FALSE。

2、递推公式
   s=输入的字符串
   dp: 保存字符串两位之间是否是回文字符，数组内部每个数据是布尔类型
   当s[i]=s[j]时，就继续判断dp[i-1][j+1]是否是回文子串，如果是，那么s[i]到s[j]的子串就是回文串，再更新dp[i][j]为TRUE。
   dp[i][j]=s[i]==s[j]  and (dp[i+1][j-1] or j-i==1)

   遍历顺序：由于判断i到j之间是不是回文子串，要求第i+1到第j-1位是不是回文子串，因此在变量字符串的过程中，从后向前遍历，如此可以保证第i+1位到第j-1位是不是回文子串，避免重复计算。


"""


def longest_palindrome(s):

    right = left = 0
    dp = []

    # 初始化dp1
    for i in range(len(s)):
        dp.append([False] * len(s))
        dp[i][i] = True

    i = len(s) - 2
    while i >= 0:
        j = i + 1
        while j < len(s):
            dp[i][j] = s[i]==s[j] and (dp[i+1][j-1] or j - i == 1)
            if dp[i][j] and right - left < j - i:
                right = j
                left = i
            j += 1
        i -= 1
    return s[left: right+1]



"""
优化方法： 中心扩展法，相比动态规划，节约了存储空间，降低了一定的复杂度。

中心扩展法： 遍历原始字符串中的每个字符，依次判断以每个字符为中心的回文子串。在向两边扩展的过程中，，如果已经不是回文子串的情况，那么无须再扩展，因此一个回文子串其中心扩展而来的子串必定也是回文子串。

"""

"""
变量定义：
i: 表示当前中心字符位置，初始化为0
minstart: 表示当前为止最长回文子串的头部位置，初始化为0
maxl: 表示目前为止最长回文子串的长度，初始化长度为1
l: 表示以中心点向左扩展到的位置，在每趟遍历中，初始化为i
r: 表示以中心点向右扩展的位置，在每趟遍历中，初始化为i

遍历过程中：有两个需要注意的地方： 
1） 每轮遍历之初，先对当前最长回文子串的长度与以当前字符为中心可能得到的最长回文子串长度进行比较，如果以当前字符为中心不可能当前更长的回文子串，那么停止遍历。
    if len(s) -i < maxl/2:
    break
2) 需要注意的问题：在每个中心位置向右扩展判断字符是否与中心字符相同，如果相同，则右指针向后移动。
   while r < len(s) -1 and s[r] == s[r+1]:
   r += 1


"""



def longest_Palindrome_(s):

    if len(s) <= 1:
        return s

    i = minstart = 0
    maxl = 1
    while i < len(s):
        if len(s) - i < maxl/2:
            break

        l = r = i
        while r < len(s) -1 and s[r] == s[r+1]:
            r += 1

        while r < len(s) -1 and l > 0 and s[l-1] == s [r+1]:
            l, r = l-1, r+1
        if r -l + 1 >= maxl:
            minstart, maxl = l, r-l+1
        i += 1

    return s[minstart: minstart+maxl]





