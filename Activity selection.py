n = int(input("Enter number of activities: "))

activities = []

for i in range(n):
    start, finish = map(
        int, input("Enter start and finish time: ").split()
    )
    activities.append((start, finish))

activities.sort(key=lambda x: x[1])

selected = []
last_finish = float('-inf')

for start, finish in activities:
    if start >= last_finish:
        selected.append((start, finish))
        last_finish = finish

print("Selected activities:", selected)
print("Maximum activities:", len(selected))