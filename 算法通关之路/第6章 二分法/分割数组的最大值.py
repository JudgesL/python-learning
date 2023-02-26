# 给定一个非负整数数组和一个整数m 将这个数组分成m个非空的连续子数组 设计一个算法让这m个数字各自和的最大值最小
# 这个需要对思路进行一个转化 二分法分的不是数组 而是划分最大值的区间 和吃香蕉的问题有一点类似
# 和最大值所在的空间就是[max(nums),sum(nums)] 如果取mid无法达成，那意味着结果值在右侧 否则在左侧
from typing import List
class Solution:
    def splitArray(self,nums:List[int], m:int) -> int:
        def help(ans:int)->bool:
            cnt,cur=1,0
            for num in nums:
                if (cur + num) > ans:
                    cur = num
                    cnt += 1
                else:
                    cur += num
            return cnt <= m
        l, h = max(nums),sum(nums)
        while l<=h:
            mid = l + (h-l)//2
            if l==h:
                return l
            # 如果中间值可以分割 意味着答案在左侧
            elif help(mid):
                h = mid
            else:
                l = mid+1
        return -1