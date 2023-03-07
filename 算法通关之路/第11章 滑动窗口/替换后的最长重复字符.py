# 一个仅由大写英文字母构成的字符串 可以将任意位置字符替换成任意其他字符 最多k次 找到包含重复字母的最长子串的长度
# 把问题转化为 在一个滑动窗口内 出现次数最多的字符+可替换次数 是否=长度
# 如果满足替换 那么是一个潜在解 如果不满足，那更长的窗口一样是不满足的 可以直接右移
import collections
class Solution:
    def characterReplacement(self,s:str,k:int)->int:
        if len(s) == 0:
            return 0
        res = left = right = 0
        max_char_n =0
        # 统计窗口内出现的字符数
        counts = collections.Counter()
        for right in range(0,len(s)):
            # 进入字符
            counts[s[right]] += 1
            max_char_n = max(max_char_n,counts[s[right]])

            if right - left + 1 > k + max_char_n:
                counts[s[left]] -= 1
                left += 1
        # 由于窗口不严格递增 因此可以直接返回大小作为答案
        return right - left + 1

    # 更抽象的方法 只关注于长度本身
    def characterReplacement_slideII(self,s:str,k:int)->int:
        max_char_n = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]]+=1
            max_char_n = max(max_char_n,count[s[i]])
            # 判断长度是否满足要求
            if res - max_char_n < k:
                res += 1
            else:
                count[s[i-res]] -= 1
        return res