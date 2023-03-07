# 给定一个已按照升序排列的有序数组 找到两个数使他们相加之和等于目标数
# 注意 下标值不是从0开始的
from typing import List
class Solution:
    # 暴力法
    def twoSum(self,numbers:List[int],target:int)->List[int]:
        for i in range(0,len(numbers),1):
            for j in range(i+1,len(numbers),1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        return []

    # 双指针法
    def twoSum_shuangzhizhen(self, numbers:List[int], target:int)->List[int]:
        left,right=0,len(numbers)-1
        while left < right:
            if (numbers[left] + numbers[right] == target):
                return [left+1,right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []
