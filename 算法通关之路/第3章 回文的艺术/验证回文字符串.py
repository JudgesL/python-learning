# 给定一个非空字符串s 要求最多删除一个字符 判断其能否成为回文字符串
# 如果是回文 那首位指针读取到的必定是相同的内容
# 从两端分别往中间开始读 如果出现了不一样 那就必须要进行删除 删除左边或者删除右边 如果能成为回文就true 否则 false
from typing import List
class Solution:
    def validPalindrome(self, s:str) -> bool:
        n = len(s)

        def isPalidrome(s:str, i:int, n:int)-> bool:
            l = 0
            r = n-1
            while l<r:
                # 这里考虑的是删除 做成了跳过的形式 这个比直接在str中删除一个字母再比较更好
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1

                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
        l = 0
        r = n -1
        while l<r:
            if s[l] != s[r]:
                return isPalidrome(s, l, n) or isPalidrome(s,r,n)
            l += 1
            r -= 1
        return True