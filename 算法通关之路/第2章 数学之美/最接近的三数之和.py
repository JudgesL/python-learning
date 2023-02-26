# 给定一个包括n个整数的数组nums和一个目标值target 找出nums中和最为接近的三个数并返回和
from typing import List
class Solution:
    # 没有使用排序 导致复杂度较高 即使是求closet也可以用排序降低复杂度 并且在while l<r的时候发现了问题
    def threeSumClosest_self(self, nums:List[int], target:int) -> int:
        n = len(nums)
        if (n<3):
            return
        res = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(len(nums)-2):
            l = i+1
            r = n-1
            while l<r:
                distance = abs(nums[i] + nums[l] + nums[r] - target)
                if distance == 0 :
                    return distance
                else:
                    if distance < res:
                        res = distance
        return distance
    def threeSumClosest(self, nums:List[int], target:int) -> int:
        n = len(nums)
        if (n < 3):
            return
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            # 去重
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s-target) < abs(res-target):
                    res = s
                # 这里体现了排序的意义
                if s < target:
                    l = l + 1
                elif s > target:
                    r = r - 1
        return res
