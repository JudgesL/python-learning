# 给定一个区间的集合 找到需要移除区间的最小数量 使剩余区间互不重叠
# 问题转化： 找到不重叠的最多区间数量 转换成问题的反面
from typing import List
class Solution:
    def earseOverlapIntervals(self,intervals:List[List[int]])->int:
        if len(intervals) == 0:
            return 0
        # 关键！制定了按照终点前后排序 选择终点越小 就越有空间存放新的区间
        intervals.sort(key=lambda i:i[1])
        cnt = 1
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                continue
            end = intervals[i][1]
            cnt += 1
        return len(intervals) - cnt
