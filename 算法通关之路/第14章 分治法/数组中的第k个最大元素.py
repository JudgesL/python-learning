# 找到数组中的第k个最大的元素 排序后的第k个
# 排序
from typing import List
import random
class Solution:
    def findKthLargest(self,nums:List[int],k:int)->int:
        nums.sort()#升序
        return nums[-k]
    # 快速选择
    def findKthLargest_quick(self,nums:List[int],k:int)->int:
        return self.select(nums,0,len(nums)-1,len(nums)-k)

    def select(self,nums:List[int],left:int,right:int,k_smallest:int):
        if left == right:
            return nums[left]
        pivot_index = random.randint(left,right)
        # 得到新的piviot 这个时候 左边都比pivot小 右边都比pivot大
        pivot_index = self.partition(nums,left,right,pivot_index)
        # 如果n-k = pivot 我们已经找到了对应位置
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return self.select(nums,left,pivot_index-1,k_smallest)
        else:
            return self.select(nums,pivot_index+1,right,k_smallest)
    # 上面的写法是尾递归 但是我们也可以写成迭代
    def select_iter(self, nums: List[int], left: int, right: int, k_smallest: int):
        while left<right:
            pivot_index = random.randint(left,right)
            pivot_index = self.partition(nums,left,right,pivot_index)
            if k_smallest == pivot_index:
                return nums[pivot_index]
            elif k_smallest < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
        if left == right:
            return nums[left]

    def partition(self,nums:List[int],left:int,right:int,pivot_index:int):
        i = left
        j = right + 1
        pivot =nums[pivot_index]
        # 临时替换位置 因为中间部分马上就要进入排序
        nums[pivot_index],nums[left] = nums[left],nums[pivot_index]

        while True:
            while True:
                i+= 1
                if i== right or nums[i] >= pivot:
                    break
            while True:
                j -= 1
                if i==left or nums[j] <= pivot:
                    break
            # 停止的时候 j停在了一个小于pivot的位置 偏左
            if i >= j:
                break
            nums[i],nums[j] = nums[j],nums[i]
        nums[left],nums[j] = nums[j],nums[left]
        # j变成了实质上的pivot
        return j




