def brackets(s: str) -> bool:
    br = {')' : '(', ']' : '[', '}' : '{'}
    cap = []

    for i in s:
        if i in "([{":
            cap.append(i)
        elif i in ")]}":
            if not cap or cap.pop() != br[i]:
                return False
        else: return False


    return len(cap) == 0

s = '([]{}({})))'

print(brackets(s))

