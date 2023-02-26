# 峰值元素是值其值大于左右相邻值的元素 给定一个数组nums 其中nums[i]!= nums[i+1] 只需要返回一个
# 因为只需要返回一个峰值元素 所以可以用二分法来处理
# 如果右边元素大于mid 那右边必定存在峰值 因为其已经满足大于左边 只要找到一个右边的更小值或者nums[n]=-∞的位置
# 如果左边元素大于mid 那左边必定存在峰值 同理
from typing import List
class Solution:
    def findPeakElement(self,nums:List[int]) -> int:
        n = len(nums)
        l,h = 0,n-1
        while l <= h:
            mid = l + (h-l)//2
            if mid + 1 < n and nums[mid] < nums[mid+1]:
                # 右侧存在峰值
                l = mid + 1
            elif mid -1 >=0 and nums[mid] < nums[mid-1]:
                # 左侧存在峰值
                h = mid - 1
            else:
                # 如果大于左边 大于右边 自己就是峰值
                return mid
        return -1
