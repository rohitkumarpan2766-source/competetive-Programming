def count_routes(n, k, d):
    MOD = 10**9 + 7
    all_routes = [0] * (n + 1)
    small_routes = [0] * (n + 1)
    all_routes[0] = small_routes[0] = 1
    
    for s in range(1, n + 1):
        for j in range(1, k + 1):
            if j <= s:
                all_routes[s] = (all_routes[s] + all_routes[s - j]) % MOD
            if j < d and j <= s:
                small_routes[s] = (small_routes[s] + small_routes[s - j]) % MOD
                
    return (all_routes[n] - small_routes[n]) % MOD