from typing import List
# 查找第一个大于或等于x的元素
def bs(nums:List[int], x:int)->int:
    l, h = 0, len(nums) - 1
    while l <= h:
        mid = l + (h-l)//2
        if l == h:
            break
        # 如果=x 也不能马上退出 需要保留这种情况
        elif nums[mid] >= x:
            h = mid
        # 因为mid小于x了 所以l可以放心的+1
        else:
            l = mid + 1
# 查找最后一个小于或等于x的元素
def bs_less(nums:List[int],x:int)->int:
    l, h =0, len(nums) - 1
    while l <= h:
        mid = l + (h-l)//2
        if l == h or l + 1 == h:
            break
        elif nums[mid] <= x:
            l = mid
        else:
            h = mid - 1
    # 找最后一个
    if nums[h] <= x:
        return nums[h]
    else:
        return nums[l]
