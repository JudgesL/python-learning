# 给定一个字符串 请找出其中不含有重复字符的最长子串的长度
from typing import List
class Solution:
    # 暴力法
    def allUnique(self,s:str)->bool:
        dic = {}
        for i in range(0, len(s), 1):
            if s[i] in dic:
                return False
            else:
                dic[s[i]] = 1
                return True

    def lengthOfLongestSubstring(self,s:str)->int:
        res = 0

        for i in range(0,len(s),1):
            for j in range(i,len(s),1)
            if self.allUnique(s[i:j+1]):
                res = max(res,j-i+1)
            else:
                break
        return res

    # 双指针法
    # 当右指针遇到重复字符即可跳出循环
    def lengthOfLongestSubstring_double(self,s:str)->int:
        res,left,right = 0,0,0
        # 存储字母
        settings = set()
        for left in range(0,len(s),1):
            right = left
            while(right<len(s)):
                if (s[right] in settings):
                    break
                else:
                    settings.add(s[right])
                    res = max(res,right-left+1)
                    right = right+1
            settings.clear()

        return res

    # 双指针法II
    # 当我们发现abcdc中包含了重复字符c 因此不必再检测bcdc了，因为必定长度无法超过abcd
    # 因此 如果出现重复 只需要从重复位之后一个开始查找就行 比如dc
    def lengthOfLongestSubstring_doubleII(self,s:str)->int:
        res, left, right = 0, 0, 0
        settings = set()

        while right<len(s):
            if s[right] in settings:
            # 出现重复 移动left进行清算
                while left < right:
                    if s[left] == s[right]:
                        settings.discard(s[left])
                        left += 1
                        break
                    else:
                        settings.discard(s[left])
                        left += 1
            # 如果不出现重复 或者清算结束后继续
            settings.add(s[right])
            res = max(res, right - left + 1)
            right = right + 1

        return res

    # 滑动窗口法
    def lengthOfLongestSubstring_slide(self,s:str)->int:
        res, left, right = 0,0,0
        dic = {}
        while right < len(s) and left + res < len(s):
            if s[right] in dic:
                left = max(left, dic[s[right]]+1)

            dic[s[right]] = right
            res = max(res,right-left+1)
            right += 1
        return res


