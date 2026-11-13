n = int(input("Enter n: "))

if n < 0:
    print("Enter a non-negative integer")
else:
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print("Fibonacci number:", dp[n])