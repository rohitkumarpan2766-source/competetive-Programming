nums = list(map(int, input("Enter numbers: ").split()))

seen = set()
result = []

for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)

print("After removing duplicates:", result)