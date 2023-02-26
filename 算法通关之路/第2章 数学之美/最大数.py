# 给定一组非负数，重新排列他们的顺序以生成最大的整数
import functools
from typing import List

class Solution:
    def largestNumber(self,nums:List[int])->str:
        # 先全部转化为str
        s = [str(i) for i in nums]

        def comp(a,b):
            if (a+b) > (b+a):
                return 1
            if (a+b) < (b+a):
                return -1
            return 0

        s.sort(reverse=True,key=functools.cmp_to_key(comp))
        # 这里''.join(s)指的是用''作为连接符把s中的函数连接起来，转换成int是为了避免首位有0，然后再转成str
        # 但是既然说这个数值特别大 转int有可能会导致越界 这里可以用首去除把第一个出现的0去除 s.lstrip('0')
        return str(int(''.join(s)))