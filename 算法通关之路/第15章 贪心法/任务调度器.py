# 用26个字母表示26种不同种类的任务 同样种类的任务有长度n的冷却时间 计算最短时间
# 首先找出最多的任务 然后设计成 A__A__A__ (n=2) 然后往中间插入 如果有溢出 就插在板块之间 ABC D ABC ABC
from typing import List
class Solution:
    def leastInterval(self,tasks:List[str],n:int)->int:
        t_map = [0]*26
        for t in tasks:
            t_map[ord(t)-ord('A')] += 1
        #sort以后打乱了排序 任务的种类是ABCD也就消失了 不过这个不重要
        t_map.sort()
        # max_num是最高次数 cnt是最高次数的任务种类
        max_num,cnt =t_map[25],0
        for i in range(26):
            if t_map[i] == max_num:
                cnt += 1
        # 如果插入的空格不够 有溢出 那就可以在最短时间内完成任务 也就是len(task)
        # 如果存在空格 那应该是 首先处理最后一组任务之前的(max_num - 1)*(n+1) 然后加上尾巴 cnt
        return max((max_num-1)*(n+1)+cnt,len(tasks))