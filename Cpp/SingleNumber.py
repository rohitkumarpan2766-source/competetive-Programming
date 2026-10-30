arr = [2, 3, 5, 3, 2]

result = 0

for num in arr:
    result = result ^ num

print("Number appearing only once:", result)