
def first_mismatch(s):
    match = {')': '(', ']': '[', '}': '{'}
    st = []

    for i, ch in enumerate(s):
        if ch in '([{':
            st.append(ch)

        elif not st or st.pop() != match[ch]:
            return i

    return -1 if not st else len(s)


print(first_mismatch("{[()] }"))
print(first_mismatch("{[()] }".replace(" ", "")))
print(first_mismatch("{[(])}"))
