arr = [1, 2, 3, 2, 4, 1, 5]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print("Original list:", arr)
print("After removing duplicates:", result)