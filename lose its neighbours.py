def max_score(nums):
    if not nums:
        return 0
    M = max(nums)
    w = [0] * (M + 1)
    for x in nums:
        w[x] += x  
        
    dp = [0] * (M + 1)
    dp[1] = w[1]
    for i in range(2, M + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + w[i])
    return dp[M]