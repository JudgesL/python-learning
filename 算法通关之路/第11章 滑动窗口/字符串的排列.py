# 给定两个字符串S1 S2，写一个函数判断S2是否包含S1的排列
# 换句话说 第1个字符串的排列之一是第2个字符串的子串。

class Solution:
    def checkInclusion(self,s1:str,s2:str):
        if (len(s1)<len(s2)):
            return False
        list1 = [0 for i in range(26)]
        list2 = [0 for i in range(26)]
        # s1记录 s2初始化
        for i in range(len(s1)):
            list1[ord(s1[i])-ord('a')] += 1
            list2[ord(s2[i])-ord('a')] += 1
        count = 0
        # count初始化
        for i in range(26):
            if list1[i] == list2[i]:
                count+=1
        # 窗口大小已固定 开始移动
        for i in range(len(s2)-len(s1)):
            if count == 26:
                return True
            # 新的right 和 left。这里的right保存的是新加入的 而left保存的其实是要移出的
            right_in = ord(s2[i+len(s1)]) - ord('a')
            left_out = ord(s2[i]) - ord('a')
            # 处理新增right带来的影响
            list2[right_in] += 1
            if list2[right_in] == list1[right_in]:
                count += 1
            elif list2[right_in] == list1[right_in] + 1:
                count -= 1

            list2[left_out] -= 1
            if list2[left_out] == list1[left_out]:
                count += 1
            elif list2[left_out] == list2[left_out] - 1:
                count -= 1
        return count == 26

