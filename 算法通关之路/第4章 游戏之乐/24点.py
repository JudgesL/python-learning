# 有4张分别写有1-9的牌 判断能否通过 * / + - （）的运算获得24
from typing import List
class Solution:
    def judgePoint24(self,nums:List[int])->bool:
        # 全排列
        permutations = self.permuteUniques(nums)
        for permutation in permutations:
            if self.compute(permutation):
                return True
        return False

    def compute(self,nums:List[float])->bool:
        if len(nums) == 1:
            # 避免精度问题
            return abs(nums[0] - 24) <= 0.00001
        for i in range(len(nums) - 1):
            # 计算 + - * / 对应的结果
            tmp = []
            tmp.append(nums[i] + nums[i+1])
            tmp.append(nums[i] - nums[i+1])
            tmp.append(nums[i] * nums[i+1])
            if nums[i+1] != 0:
                tmp.append(nums[i]/nums[i+1])

            for num in tmp:
                new_list = nums[:]
                # 将两个数形成的结果替换掉原来的位置 并pop掉一个 这样nums就由4到3
                new_list[i] = num
                new_list.pop(i+1)
                if self.compute(new_list):
                    return True
        return False
    # 全排列
    def permuteUniques(self,nums:List[int]) -> List[List[int]]:
        permutations = []
        nums.sort()
        tmp = []
        visited = [False]*len(nums)
        self.backtracking(nums,tmp,visited,permutations)
        return permutations

    def backtracking(self,nums:List[int], tmp:List[float],visited:List[bool],perm:List[int]) -> None:
        if len(nums) == len(tmp):
            perm.append(tmp[:])
            return
        for i in range(len(nums)):
            print('i=', i)
            print(visited)
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            tmp.append(nums[i])
            print(tmp)

            # 1. 走完了1234这个排列后 再运行这个backtrack只是在perm里面留下了记录 随后就return了
            self.backtracking(nums,tmp,visited,perm)
            print('backtrack执行完毕')
            # 2. 第一次来到这个位置 i=3 然后把已经访问的最后设为False了
            # 5. 第二次来到这个位置 i=2 然后把访问的倒数第二位（数3）也设了False
            print('i回溯：',i)
            visited[i] = False
            # 3. 第一次弹出了‘4’这个数 然后本段程序运行结束了 也就是i=3的程序到此结束了
            # 4. 然后回溯到了调用的时候 也就是已经有了123序列 i=2的时候的记录
            # 6. 这次弹出了‘3’这个数 但是并没有修改i 于是马上i就会+1变成3 会把最后一个4加进来 于是就完成了顺序的修改
            tmp.pop()

solve = Solution()
nums = [1,2,3,4]
answer = solve.judgePoint24(nums)
print(answer)