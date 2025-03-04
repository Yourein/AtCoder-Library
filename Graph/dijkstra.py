from heapq import heappush, heappop

def dijkstra(s: int) -> list:
    INF = 10 ** 18
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        pre = heappop(q)[1]
        for nxt, cost in g[pre]:
            if dist[nxt] < dist[pre] + cost: continue
            dist[nxt] = dist[pre] + cost
            heappush(q, (dist[nxt], nxt))

    return dist

n, m = map(int,input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    x, y, cost = map(int,input().split())
    x -= 1
    y -= 1
    g[x].append((y, cost))
    g[y].append((x, cost))

d = dijkstra(0)