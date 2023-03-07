nums = []
error = 2
target = 1
ans = []
visited = set()
n = len(nums)
def dfs(idx,cur,path):
    #结束条件
    # 1.找到解
    if cur == target:
        ans.append(path.copy())
        return
    # 2. 搜索完毕
    if idx == n:
        return

    # 考虑可能的解 进入递归
    for num in nums:
        #忽略非法
        if num == error or num in visited:
            continue
        # 考虑这个数 进行状态更改
        visited.add(num)
        path.append(num)
        dfs(idx+1,cur+num,path)

        #恢复状态
        path.pop()
        visited.remove(num)
