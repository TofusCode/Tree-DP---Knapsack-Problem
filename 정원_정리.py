import sys
input = sys.stdin.readline
INF = float('inf')

def dfs(node):
    visited[node] = True
    for v in graph[node]:
        if not visited[v]:
            sub[node] += dfs(v)
    return sub[node]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

if n < m:
    print(-1)
elif n == m:
    print(0)
else:
    req = n-m
    dp = [[INF]*(req+1) for _ in range(n+1)]
    sub = [1]*(n+1)
    visited = [False]*(n+1)

    dfs(1)
    for i in range(1, n+1):
        if (sub[i] == m) or (n-sub[i] == m):
            dp[-1][-1] = 1
            break
        for j in range(req+1):
            if j == 0:
                dp[i][j] = 0
            else:
                if j >= sub[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-sub[i]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
    print(dp[-1][-1])