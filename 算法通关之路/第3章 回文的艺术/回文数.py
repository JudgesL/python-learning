# 判断一个数是否是回文数 一个最简单的方法是转化为字符串str然后用双指针
# 如果限制了不允许转化成字符串 那只需要把一个数不停的%10 这就取得他从后到前的排列 然后与从前到后的比较即可
from typing import List
class Solution:
    def isPalindrome(self,x:int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        res = 0
        copy = x
        while x > 0:
            res = res*10 + (x % 10)
            x = x//10
        return copy == res