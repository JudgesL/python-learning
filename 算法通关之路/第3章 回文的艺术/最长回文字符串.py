# 给定一个字符串s 找到s中最长的回文子串 假设s的最大长度为1000
# 如果列举出所有的子串 复杂度为O(n^2) 判断是否是回文的复杂度为O(n) 整体复杂度O(n^3)
# 另有一种方法 就是抓住回文的核心 也就是回文其中心到两边呈现对称的姿态
from typing import List
class Solution:
    def longestPalindrome(self,s:str) -> str:
        n = len(s)
        if n == 0:
            return ''
        res = s[0]
        def extend(i:int,j:int,s:str)->str:
            while i>=0 and j<len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        for i in range(n-1):
            #如果是奇数个 自身就是中心点
            e1 = extend(i,i,s)
            #如果是偶数个 自己与下一个是中心点
            e2 = extend(i,i+1,s)
            if max(len(e1),len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res
