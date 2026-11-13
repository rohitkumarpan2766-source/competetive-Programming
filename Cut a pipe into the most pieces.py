def max_pieces(n, cuts):
    NEG = float('-inf')
    dp = [0] + [NEG] * n
    for i in range(1, n + 1):
        for c in cuts:
            if c <= i:
                dp[i] = max(dp[i], dp[i - c] + 1)
    return dp[n] if dp[n] != NEG else -1