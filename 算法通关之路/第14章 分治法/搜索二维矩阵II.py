# 编写一个高效的算法来搜索m*n矩阵matrix中一个目标值target
# 每行左到右升序 每列上到下升序
from typing import List
class Solution:
    def searchMatrix(self,matrix:List[List[int]], target:int)->bool:
        def binarySearch(arr:List[int],target:int)->bool:
            lo = 0
            # 最后一个元素的索引
            hi = len(arr) - 1
            # 所以这边搜索区间是需要包括到最后一个元素的
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    lo = mid + 1
                elif arr[mid] > target:
                    hi = mid - 1
            return False

        if not matrix or not matrix[0]:
            return False

        m = len(matrix)

        for i in range(m):
            if binarySearch(matrix[i],target):
                return True
        return False
    # 二分法优化 如何用上行列有序的特性
    # 方法1 沿着对角线
    def binary_search_duijiao(self,matrix:List[List[int]], target:int,start:int,vertical:bool)->bool:
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while lo <= hi:
            mid = lo + (hi - lo)//2
            if vertical:
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                elif matrix[mid][start] == target
                    return True
            else:
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                elif matrix[start][mid] == target:
                    return True
    def searchMatrix_optim(self, matrix:List[List[int]], target:int)->bool:
        if not matrix:
            return False
        minLen = min(len(matrix),len(matrix[0]))
        for i in range(minLen):
            # 寻找是从第i行第i列开始的 也就是沿着对角线
            vertical_found = self.binary_search_duijiao(matrix,target,i,True)
            horizon_found = self.binary_search_duijiao(matrix,target,i,False)
            if vertical_found or horizon_found:
                return True
        return False

    # 在二维空间中缩减搜索空间 任何一个子矩阵 左上角是最小值 右上角是最大值
    def searchMatrix_twod(self,matrix:List[List[int]],target:int)->bool:
        if not matrix:
            return False
        def search_rec(left,up,right,down):
            # 空矩阵
            if left>right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[right][down]:
                return False
            # 定位切分中心 这里搜索的是 中间行
            mid = left+(right-left)//2
            row = up
            # 最后 row停留在了 第一个 > target的位置
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search_rec(left,row,mid-1,down) or search_rec(mid+1,up,right,row-1)
        return search_rec(0,0,len(matrix[0])-1,len(matrix)-1)

    # 继续优化 在搜索row的时候也采用二分
    def searchMatrix_final(self,matrix:List[List[int]],target:int)->bool:
        if not matrix:
            return False
        def binarySearch(matrix:List[List[int]],up:int,down:int,col:int,target:int)->List:
            lo = up
            # 注意 这边的hi是取不到的
            hi = down + 1
            while lo < hi:
                mid = lo + (hi-lo)//2
                # 这里我们固定行 搜索中间列
                if matrix[mid][col] == target:
                    return [True,mid]
                elif matrix[mid][col] < target:
                    lo = mid + 1
                elif matrix[mid][col] > target:
                    hi = mid - 1
                # 返回较大的那个了
            return [False,lo]

        def search_rec(left:int,up:int,right:int,down:int)->bool:
            # 空矩阵
            if left > right or up > down:
                return False
            elif target < matrix[left][up] or target > matrix[right][down]:
                return False

            mid = left + (right - left)//2
            # 定位列
            find, col = binarySearch(matrix,up,down,mid,target)

            return (search_rec(left,mid+1,col-1,down) or search_rec(col,up,right,mid-1))
        return search_rec(0,0,len(matrix[0])-1,len(matrix)-1)

    # 从左下角 或者 右上角开始搜索
    # 如果从左下角开始搜索 当前值等于目标值 返回即可
    # 如果当前值小于目标值 那本列全都小于
    # 如果当前值大于目标值，那本行全都大于
    def searchMatrix_linear(self,matrix:List[List[int]],target:int):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])

        row = m - 1
        col = 0
        while col < n and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
        return False








