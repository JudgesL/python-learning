# 外观数列是一个整数数列 从数字1开始 序列中每一项都是对前一项的描述
#1 11 21 1211 111221
#1 1个1 2个1  1个2，1个1  1个1，1个2，2个1
# 给定一个正整数 输出外观数列的第n项
class Solution:
    # 第一种方法 迭代法 时间复杂度O(mn) m是最后一个字符串的长度 空间复杂度O(m)
    def countAndSay(self,n:int)->str:
        ans = '1'
        for i in range(1,n):
            tmp =''
            current_char,char_count = ans[0],0
            for j in range(len(ans)):
                if ans[j] != current_char:
                    tmp += str(char_count) + current_char
                    current_char,char_count = ans[j],1
                else:
                    char_count += 1
            tmp += str(char_count) + current_char
            ans = tmp
        return ans
    # 第二种显而易见的解法 递归法 时间复杂度O(mn) 空间复杂度O(n+m)
    def countAndSay_digui(self,n:int)->str:
        if n == 1:
            return '1'
        previous_string = self.countAndSay_digui(n-1)
        char_index,char_count =0,1
        current_string=''
        for i in range(len(previous_string)-1):
            if previous_string[char_index] == previous_string[char_index+1]:
                char_count += 1
            else:
                current_string += str(char_count) + previous_string[char_index]
                char_index,char_count = i+1,1
        current_string += str(char_count) + previous_string[char_index]
        return current_string