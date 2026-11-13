s = input("Enter brackets: ")

stack = []
pairs = {')': '(', '}': '{', ']': '['}

for ch in s:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack or stack[-1] != pairs[ch]:
            print("Invalid")
            break
        stack.pop()
else:
    if not stack:
        print("Valid")
    else:
        print("Invalid")