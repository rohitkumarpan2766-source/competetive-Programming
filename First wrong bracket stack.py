def first_mismatch(s):
    match = {')': '(', '}': '{', ']': '['}
    st = []
    for i, ch in enumerate(s):
        if ch in '({[':
            st.append(ch)
        elif not st or st.pop() != match[ch]:
            return i
    return -1 if not st else len(s)