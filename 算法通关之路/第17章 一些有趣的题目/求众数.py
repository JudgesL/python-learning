# 一个大小为n的数组 找出其中出现次数超过n/3的元素 时间复杂度O(n) 空间O(1)
# 摩尔投票法 出现一个数就计1 如果重复出现就增加 我们这里需要超过n/3 所以最多有2个（0 1 2）三种可能性
# 用2个计数器 当出现了第二个数的时候让第二个计数器也开始计 如果两个计数器都满了 再出现新的数就让两个计数器一起-1，直到空出一个
from typing import List
class Solution:
    def majorityElement(self,nums:List[int])->List[int]:
        n = len(nums)
        res = []
        cnt1 = 0
        cnt2 = 0
        n1 = None
        n2 = None

        for num in nums:
            if num == n1:
                cnt1 += 1
            elif num == n2:
                cnt2 += 1
            elif cnt1 == 0:
                n1 = num
                cnt1 += 1
            elif cnt2 == 0:
                n2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        # 确定n1 n2是否真的超过1/3
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == n1:
                cnt1 += 1
            elif num == n2:
                cnt2 += 1

        if cnt1 > n//3:
            res.append(n1)
        if cnt2 > n//3:
            res.append(n2)
        return res