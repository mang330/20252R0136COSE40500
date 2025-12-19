from collections import deque

def bfs(adj, start):
    visited = set([start])
    q = deque([start])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nv in adj.get(v, []):
            if nv not in visited:
                visited.add(nv)
                q.append(nv)
    return order

def dfs(adj, start):
    visited = set()
    order = []
    def go(v):
        visited.add(v)
        order.append(v)
        for nv in adj.get(v, []):
            if nv not in visited:
                go(nv)
    go(start)
    return order

if __name__ == "__main__":
    adj = {1:[2,3], 2:[4], 3:[4], 4:[]}
    print(bfs(adj, 1))
    print(dfs(adj, 1))
