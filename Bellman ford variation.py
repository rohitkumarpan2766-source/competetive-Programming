def cheapest(n, fares, src, dst, k):
    INF = float('inf')
    cost = [INF] * n
    cost[src] = 0
    
    for _ in range(k + 1):
        new_cost = cost[:] 
        for u, v, w in fares:
            if cost[u] != INF:
                new_cost[v] = min(new_cost[v], cost[u] + w)
        cost = new_cost
        
    return cost[dst] if cost[dst] != INF else -1