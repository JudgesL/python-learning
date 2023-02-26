# 数独游戏 每行每列和每个九宫格恰好由1-9这9个数字组成
# 对于九宫格 用行号//3 *3 + 列号//3
# 优化的时候 可以考虑不用顺序遍历 而是寻找最有把握的格子开始填
from typing import List
class Solution:
    row_state = [[False for i in range(10)] for _ in range(9)]
    column_state = [[False for i in range(10) for _ in range(9)]]
    box_state = [[False for i in range(10)] for _ in range(9)]
    board = []
    def solveSudoku(self, board:List[List[str]]) -> None:
        #LeetCode 判定时会反复调用函数，因此需要反复初始化状态表
        self.row_state = [[False for i in range(10)] for _ in range(9)]
        self.column_state = [[False for i in range(10) for _ in range(9)]]
        self.box_state = [[False for i in range(10)] for _ in range(9)]
        self.board = board
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != '.':
                    num = int(self.board[i][j])
                    self.row_state[i][num] = True
                    self.column_state[j][num] = True
                    self.box_state[(i//3)*3 +j//3][num] = True

    def place_number(self, row:int, column:int, i:int,)->bool:
        self.row_state[row][i] = True
        self.column_state[column][i] = True
        self.box_state[(row//3)*3 + column//3][i] = True
        self.board[row][column] = str(i)

    def undo_number_placement(self, row:int, column:int, i:int,)->bool:
        self.row_state[row][i] = False
        self.column_state[column][i] = False
        self.box_state[(row // 3) * 3 + column // 3][i] = False
        self.board[row][column] = '.'

        def recursive_place_number(self,row:int, column:int,)->bool:
            if row == -1 and column == -1:
                return True
            if self.board[row][column] != '.':
                return False

            for i in range(1,10):
                # 如果这个数在行、列、九宫格中用到 就不能复用
                if (self.row_state[row][i] or self.column_state[column][i] or
                        self.box_state[(row // 3) * 3 + column // 3][i]):
                    continue
                else:
                    self.place_number(row,column,i)
                    x,y = self.get_max_possible_coordinate()
                    if recursive_place_number(self,x,y):
                        return True
                    self.undo_number_placement(row,column,i)
                return False
        x, y = self.get_max_possible_coordinate()
        recursive_place_number(self,x,y)

    def get_max_possible_coordinate(self,row:int,column:int,i:int,)->bool:
        x, y, min_count = -1,-1,9
        for i in range(9):
            for j in range(9):
                # 寻找没有填写的格子
                if self.board[i][j] != '.':
                    continue
                tmp_count = 9
                for k in range(9):
                    # 如果存在已经填写了数字的位置 找到填写了多少 并且将tmp减去
                    if(self.row_state[i][k] or self.column_state[j][k] or self.box_state[(row // 3) * 3 + column // 3][k]):
                        tmp_count -= 1
                # 如果只有唯一的可能性 立刻填写
                if tmp_count == 1:
                    return i,j
                # 如果有多个可能性 取可能性最少的保存
                if min_count > tmp_count:
                    min_count = tmp_count
                    x = i
                    y = j
        return x,y


