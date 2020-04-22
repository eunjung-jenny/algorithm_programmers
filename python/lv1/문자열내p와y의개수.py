def solution(s):
    s_lower = s.lower()
    p = s_lower.count('p')
    y = s_lower.count('y')

    print(p == y)
    return p == y

s1 = 'pPoooyY'
answer1 = True

s2 = 'Pyy'
answer2 = False

solution(s1)
solution(s2)