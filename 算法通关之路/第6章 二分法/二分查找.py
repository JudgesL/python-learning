# 给定有n个元素的 有序的（升序）的整形数组nums和一个目标值target 搜索target 返回下标或-1
def binary_search(nums:[], target:int)->int:
    n = len(nums)
    l,h = 0, n - 1
    while l<=h:
        # mid = (l + h )//2
        # 为了避免再其他语言中溢出，可以采用这个写法
        mid = l + (h-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return -1