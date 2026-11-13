def max_run(arr):
    if not arr:
        return 0

    cur = best = arr[0]

    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)

    return best


print(max_run([3, -4, 5, -1, 2, -6, 4]))

