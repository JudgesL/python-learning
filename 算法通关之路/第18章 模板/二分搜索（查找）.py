from typing import List
def binary_search(nums:List[int],target:int):
    l,r = 0, len(nums) - 1
    while l <= r:
        mid = l+ (r-l)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] == target:
            return mid
    return -1

# 左区间搜索 第一个大于等于target的位置
def binary_search_leftbound(nums:List[int],target:int):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] == target:
            # 左区间必不缩左
            r = mid - 1

        # 检查越界 左区间搜索如果越界了 那就是全部的数都小于 这个时候把left顶出界了
        if l >= len(nums) or nums[l] != target:
            return -1
    return l

# 右区间搜索 最后一个小于等于target的位置
def binary_search_rightbound(nums:List[int],target:int):
    l, r =0, len(nums) - 1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] == target:
            # 右搜索不缩右
            l = mid + 1

        # 有可能都小于这个数 把right出界了
        if r < 0 or nums[r] != target:
            return -1
    return r