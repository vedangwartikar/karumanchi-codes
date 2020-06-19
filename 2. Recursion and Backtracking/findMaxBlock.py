"""arr = [[1,0,0,1],[1,1,0,1],[0,0,1,1]]
cntarr = []
for i in arr:
    for j in i:
        print(j, end = " ")
    print()
m, n = len(arr), len(arr[0])
def bfs(arr, i, j, m, n, cnt):
    if i < 0 or i > m-1 or j < 0 or j > n-1 or arr[i][j] == 0:
        return
    arr[i][j] = 0
    cnt += 1
    cntarr.append(cnt)
    bfs(arr, i-1, j, m, n, cnt)
    bfs(arr, i+1, j, m, n, cnt)
    bfs(arr, i, j-1, m, n, cnt)
    bfs(arr, i, j+1, m, n, cnt)
    bfs(arr, i-1, j-1, m, n, cnt)
    bfs(arr, i+1, j+1, m, n, cnt)
    bfs(arr, i-1, j+1, m, n, cnt)
    bfs(arr, i+1, j-1, m, n, cnt)
for i in range(m):
    for j in range(n):
        cnt = 0
        if arr[i][j] == 1:
            bfs(arr, i, j, m, n, cnt)
        else:
            cnt = 0
#print(cntarr)
print(max(cntarr))"""