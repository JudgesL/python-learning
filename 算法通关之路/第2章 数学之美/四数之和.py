# 给定整数数组nums 判断nums中是否存在4个元素a,b,c,d 使a+b+c = target，找出所有满足条件且不重复的四元组
from typing import List
class Solution:
    # 解法1 ： 暴力法
    def backtrack(self, res:List[List[int]], nums:List[int], n:int, tempList:List[int], remain:int, start:int, hashmap:dict):
        if (len(tempList)>4):
            return
        if (remain == 0 and len(tempList) == 4):
            if (str(tempList) in hashmap):
                return
            else:
                hashmap[str(tempList)] = True
                # 注意此处append的内容是list的copy 避免list的内容改变对res造成的影响
                return res.append(tempList.copy())
        for i in range(start, n):
            tempList.append(nums[i])
            self.backtrack(res,nums,n,tempList,remain - nums[i], i+1, hashmap)
            # 如果命中了 res中会自然存入结果，可以将目前的这个pop出去换下一个
            # 如果数量没到4个，无法执行判断语句，会不断的append到tempList中
            tempList.pop()
    def fourSum(self, nums:List[int], target:int) -> List[List[int]]:
        res = []
        hashmap = {}
        nums.sort()
        self.backtrack(res,nums,len(nums),[],target,0,hashmap)
        return res

    # 解法2 分治法
    def fourSum_fenzhi(self,nums:List[int], target:int):
        nums.sort()
        results = []
        self.findNSum(nums, target, 4, [], results)
        return results

    def findNSum(self,nums:List[int], target: int, N:int, tempList:List[int], results:List[List[int]]):
        if len(nums) < N or N < 2:
            return
        if N == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(tempList + [nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1                    
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        # 多和问题转化为多个二和问题
        else:
            for i in range(0, len(nums)):
                if i==0 or (i>0 and nums[i-1] != nums[i]):
                    self.findNSum(nums[i+1:], target-nums[i], N-1, tempList+[nums[i]],results)




solve = Solution()
nums = [1,0,-1,0,-2,2]
answer = solve.fourSum_fenzhi(nums,0)
print(answer)


