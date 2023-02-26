# 给定整数数组nums和一个目标值target 寻找和为目标值的那两个整数 返回索引

# 1 两层循环找到两两组合 时间复杂度O(n^2)

# 2 排序后从头尾分别相加 根据结果移动指针
from typing import List
class Solution:
    # 复杂度在排序 排序复杂度为O(nlogn) 比较操作复杂度为O(n) 整体复杂度O(nlogn)
    def twoSum_sort(self, nums:List[int], target:int) -> List[int]:
        n = len(nums)
        nums.sort()
        l = 0
        r = n - 1
        while(l < r):
            if (nums[l] + nums[r] < target):
                l += 1
            elif (nums[l] + nums[r] > target):
                r -= 1
            else:
                return [l, r]
        return []
    # 空间复杂度为 O(n) 时间复杂度上 循环有O(n)的复杂度，循环内部查找为O(1),其他为常数操作，因此整体复杂度为O(n)
    def twoSum_haxi(self, nums:List[int], target:int) -> List[int]:
        n = len(nums)
        mapper = {}
        for i in range(n):
            # 如果之前遇到过满足的结果，直接从哈希表中调取
            if (target - nums[i] in mapper):
                return [i,mapper[target - nums[i]]]
            else:
                # 哈希表索引的是值 而索引的结果是位置 这样保存下来了对应存在的位置
                mapper[nums[i]] = i
        return []


solve = Solution()
nums = [1,2,3,4,5,6,7,8,9]
answer = solve.twoSum(nums,11)
print(answer)