# 给定整数数组nums 判断nums中是否存在3个元素a,b,c 使a+b+c = 0，找出所有满足条件且不重复的三元组
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            # nums中很可能有重复的数值 因此需要去重
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = n - 1
            while(l < r):
                if (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    # 去重
                    while(l<r and nums[l]==nums[l+1]):
                        l += 1
                    while(l<r and nums[r]==nums[r-1]):
                        r -= 1
                    l += 1
        return res

solve = Solution()
nums = [-1,0,1,2,-1,-4]
answer = solve.threeSum(nums)
print(answer)

