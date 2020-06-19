def getval(A, i, j, L, H):
    if i < 0 or i >= L or j < 0 or j >= H:
        return 0
    else:
        return A[i][j]

def findMaxBlock(A, r, c, L, H, size):
    global maxsize
    global cntarr
    if r >= L or c >= H:
        return
    cntarr[r][c] = 1
    size += 1
    if size > maxsize:
        maxsize = size
    direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    for i in range(0, 7):
        newi = r + direction[i][0]
        newj = c + direction[i][1]
        val = getval(A, newi, newj, L, H)
        if val > 0 and cntarr[newi][newj] == 0:
            findMaxBlock(A, newi, newj, L, H, size)
    cntarr[r][c] = 0

def getMaxOnes(A, rmax, colmax):
    global maxsize
    global size
    global cntarr
    for i in range(0, rmax):
        for j in range(0, colmax):
            if A[i][j] == 1:
                findMaxBlock(A, i, j, rmax, colmax, 0)
    return maxsize

zarr = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[1,0,0,1,1],[0,1,0,1,1]]
rmax = 5
colmax = 5
maxsize = 0
size = 0
cntarr = rmax*[colmax*[0]]
print("Number of maximum ones are: ", end = "")
print(getMaxOnes(zarr, rmax, colmax))
"""
arr = [[1,0,0,1],[1,1,0,1],[0,0,1,1]]
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
print(max(cntarr))
"""