# 有4张分别写有1-9的牌 判断能否通过 * / + - （）的运算获得24
from typing import List
class Solution:
    def judgePoint24(self,nums:List[int])->bool:
        return self.compute([float(i) for i in nums],4)
    # 这一次把排列和计算融入到了一起
    def compute(self,nums:List[int], n:int) -> bool:
        if n == 1:
            return abs(nums[0] - 24) < 0.00001

        new_nums = [0]*4
        for left in range(n-1):
            for right in range(left+1,n):
                index = 0
                # 未参与计算的数字放到了最前端
                for i in range(n):
                    new_nums[index] = nums[i]
                    index += 1
                # 开始运算 这里会产生4种分叉
                new_nums[index] = nums[left] + nums[right]
                # 第一次未参与运算的数字是2个 减少了一个数 这里传入了3
                if self.compute(new_nums, index+1):
                    return True
                # 减法存在两种可能性
                new_nums[index] = nums[left] - nums[right]
                if self.compute(new_nums, index + 1):
                    return True
                new_nums[index] = nums[right] - nums[left]
                if self.compute(new_nums, index + 1):
                    return True
                # 乘法只有一种可能性
                new_nums[index] = nums[right] * nums[left]
                if self.compute(new_nums, index + 1):
                    return True
                #除法有两种可能性
                if nums[left] != 0:
                    new_nums[index] = nums[right] / nums[left]
                    if self.compute(new_nums, index + 1):
                        return True
                if nums[right] != 0:
                    new_nums[index] = nums[left] / nums[right]
                    if self.compute(new_nums, index + 1):
                        return True
        return False
