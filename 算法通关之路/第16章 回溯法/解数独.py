from typing import List
class Solution:
    def solveSudoku(self,board:List[List[str]])->None:
        col = [[False]*9 for i in range(9)]
        row = [[False]*9 for i in range(9)]
        place = [[False]*9 for i in range(9)]
        # 初始化
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    col[j][num] = True
                    row[i][num] = True
                    place[i//3*3 + j//3][num] = True

        def dfs(i:int,j:int)->bool:
            # 终止条件（边界）
            if j == 9:
                return dfs(i+1,0)
            if i == 9:
                return True
            # 如果已有数字
            if board[i][j] != '.':
                return dfs(i,j+1)

            for k in range(9):
                # 已有不考虑
                if (col[j][k] == True or row[i][k] == True or place[i//3*3 +j//3][k] == True):
                    continue
                # 考虑这个数
                board[i][j] = str(k+1)
                col[j][k] = True
                row[i][k] = True
                place[i//3*3 +j//3][k] = True

                # 如果可以成功
                if dfs(i,j+1) == True:
                    return True

                # 消除影响
                board[i][j] = '.'
                col[j][k] = False
                row[i][k] = False
                place[i // 3 * 3 + j // 3][k] = False
                # 下一个数会由循环带来
            return False
        dfs(0,0)
