# 按照升序排列的数组再一个预见未知的某个点上进行了旋转 例如【0，1，2，4，5，6，7】 可能变成【4，5，6，7，0，1，2】 找出最小元素 可以假设不重复
# 对本题进行分析可知 因为在数组中的某个位置发生了旋转 因此会导致 旋转后左侧区域的数值都大于右侧区域
# 那么 对于中间元素nums[mid] 如果它大于末元素 意味着它位于左侧区域 那最小值在[mid+1,h]
# 对于中间元素nums[mid] 如果它小于末元素 意味着它位于右侧区域 最小值在[l,mid] 此时mid有可能就是最终答案 是不能被排除的
from typing import List
class Solution:
    def findMin(self,nums:List[int])->int:
        l,h = 0, len(nums)-1
        while (l <=h):
            mid = l + (h-l)//2
            if l == h:
                return nums[l]
            elif nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] < nums[h]:
                h = mid
        return -1