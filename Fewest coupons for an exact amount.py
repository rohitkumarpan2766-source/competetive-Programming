def min_coupons(coins, amt):
    INF = float('inf')
    dp = [0] + [INF] * amt
    
    for i in range(1, amt + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                
    return dp[amt] if dp[amt] != INF else -1