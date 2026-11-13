nums = list(map(int, input("Enter descending numbers: ").split()))
target = int(input("Enter target: "))

left = 0
right = len(nums) - 1
result = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        result = mid
        break
    elif nums[mid] < target:
        right = mid - 1
    else:
        left = mid + 1

print("Index:", result)