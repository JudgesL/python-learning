# 给定一个字符串S 一个字符串T 请在字符串S中找出包含T所有字母(重复的话就要有多次）的最小子串
# 滑动窗口法 将两个指针都指向第一个元素
# 右指针右移直到满足要求
# 左指针左移直到不满足 循环
# 右指针右到末尾 结束
from collections import Counter
class Solution:
    def minWindow(self,s:str,t:str):
        if not t or not s:
            return ''
        # 初始化滑动窗口
        left, right =0,0
        # dict_t存放字符串T中的字符和对应的个数
        # required 为T中不相同字符的个数
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        window_counts = {}
        # ans[0]存放字符长度 ans[1]和ans[2]分别存放左右索引
        ans = float('inf'),None,None
        while right < len(s):
            character = s[right]
            #如果字典中尚未包含 character，则(返回0）添加其计数为1。如果 character 已经在字典中，其计数将增加1。
            window_counts[character] = window_counts.get(character,0) + 1
            # 这个字符的加入刚好满足要求 注意这边的==
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # 不断移动右边界 直到满足全部要求 然后开始移动左边界
            while left <= right and formed == required:
                character = s[left]
                # 保存记录
                if right - left + 1 <ans[0]:
                    ans = (right-left+1,left,right)
                #处理左减少带来的问题
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                left += 1
        if ans[0] == float('inf'):
            return ''
        else:
            return s[ans[1]:ans[2]+1]

