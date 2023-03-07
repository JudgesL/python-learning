# 给孩子小饼干 每个孩子一块 每个孩子i都有一个胃口值gi 对于每个饼干都有一个大小sj sj》gi 孩子满足 尽可能满足更多
from typing import List
class Solution:
    def findContentChildren(self,g:List[int],s:List[int])->int:
        g.sort()
        s.sort()
        ans = 0
        idx = 0
        for i in range(len(g)):
            while idx < len(s):
                if s[idx] > g[i]:
                    ans += 1
                    idx += 1
                    break
                else:
                    # 如果这个饼干的大小连这个孩子都不能满足 后续的更加不能满足 直接舍弃即可
                    idx += 1
        return ans