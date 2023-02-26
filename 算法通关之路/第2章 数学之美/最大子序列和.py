# 求数组中的最大连续子序列和 子数组必须是连续的 只需要求和 不需要返回具体位置 数组中的元素是整数
from typing import List
class Solution:
    # 暴力法
    def maxSubArray(self,nums:List[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        total = 0
        for i in range(n):
            total = 0
            for j in range(i,n):
                total += nums[j]
                maxSum = max(maxSum, total)
        return maxSum
    #分治法 全在左、全在右、横跨左右
    def maxSubArray_fenzhi(self,nums:List[int])->int:
        return self.helper(nums,0,len(nums-1))
    def helper(self,nums:List[int],l:int,r:int):
        if l>r:
            return float('-inf')
        mid = (l+r)//2
        # 递归计算左右序列最大值
        left = self.helper(nums,l,mid-1)
        right = self.helper(nums,mid+1,r)
        #处理中间序列的最大值
        left_suffix_max_sum = right_suffix_max_sum = 0
        total = 0
        # 这里是mid而不是mid-1 因为range里面最后一个取不到 实际取到mid-1就可以了
        for i in reversed(range(l,mid)):
            total += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum,total)
        total = 0
        # 注意这里是r+1 也就是需要最后取到r位置
        for i in range(mid+1,r+1):
            total += nums[i]
            right_suffix_max_sum = max(right_suffix_max_sum,total)
        cross_max_sum = left_suffix_max_sum + nums[mid] + right_suffix_max_sum
        return max(left,right,cross_max_sum)
    # 动态规划
    def maxSubArray_dongtai(self,nums:List[int])->int:
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1,n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index+nums[i],nums[i])
            max_sum = max(max_sum_ending_curr_index,max_sum)
        return max_sum
    # 前缀和
    def maxSubArray_qianzhui(self,nums:List[int])->int:
        n = len(nums)
        maxSum = nums[0]
        minSum = Sum = 0
        for i in range(n):
            Sum += nums[i]
            maxSum = max(maxSum,Sum-minSum)
            minSum = min(minSum,Sum)
        return maxSum
