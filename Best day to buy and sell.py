def max_profit(prices):
    if not prices:
        return 0

    low = prices[0]
    best = 0

    for price in prices:
        low = min(low, price)
        best = max(best, price - low)

    return best


print(max_profit([9, 4, 7, 2, 8, 5, 6]))