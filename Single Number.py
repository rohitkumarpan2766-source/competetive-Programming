nums = list(map(int, input("Enter numbers: ").split()))

result = 0

for num in nums:
    result = result ^ num

print("Single number:", result)