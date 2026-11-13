def kth_special(n, k):
    MOD = 10**9 + 7
    ans, power = 0, 1
    while k > 0:
        if k & 1: 
            ans = (ans + power) % MOD
        power = (power * n) % MOD
        k >>= 1 
    return ans