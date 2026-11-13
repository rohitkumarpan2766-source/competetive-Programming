nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        print("Indices:", seen[complement], i)
        break

    seen[num] = i
else:
    print("No solution found")