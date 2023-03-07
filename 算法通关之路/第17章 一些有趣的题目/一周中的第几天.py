#一周中的第几天
class Solution:
    def dayOfTheWeek(self,day:int,month:int,year:int)->str:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        leap_months = [31,29,31,30,31,30,31,31,30,31,30,31]
        # 1971-01-01是基准日期 1971-01-01是星期五
        days = ['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
        years = year - 1971
        leaps = 0
        # 处理计算中间有多少闰年
        i = 1972
        while i < year:
            if i%400 ==0 or (i%4 == 0 and i % 100 != 0):
                leaps += 1
            i += 1
        diff = (years*365) + leaps
        # 处理月
        for m in range(month - 1):
            if i % 400==0 or (i%4==0 and i% 100 !=0):
                diff += leap_months[i]
            else:
                diff += months
        # 处理日
        diff += day - 1
        return days[diff % 7]
    