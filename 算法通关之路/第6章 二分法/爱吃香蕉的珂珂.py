# 珂珂喜欢吃香蕉 有n堆香蕉 第i堆有piles[i]根 每小时选择一堆香蕉 吃k根 如果少于k就全部吃完 警卫h小时后回来
# 由于每小时最多只能吃完一堆香蕉 因此速度是有最大值的 速度必定在[1,max(piles)]中
# 在[1,h]中判断中间速度mid是否可行的时候 如果不可行将左边界更新为mid+1
# 如果可行 最小速度就锁定在[1,mid]中 mid不能直接被排除
# 最后直到缩小到区间只有一个
from typing import List
class Solution:
    def minEatingSpeed(self,piles:List[int],H:int)->int:
        # 判断速度k是否满足条件
        def help(k:int)->bool:
            cnt = 0
            for pile in piles:
                # 这里pile - 1是为了让pile = k的时候 第一个项0 第二个+1
                cnt += (pile - 1)//k + 1
            return cnt <= H

        l, h = 1,max(piles)
        while l <= h:
            mid = l + (h-l)//2
            if l == h:
                return l
            if help(mid):
                h = mid
            else:
                l = mid + 1
        return -1


