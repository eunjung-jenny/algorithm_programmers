def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for ss in s:
        if not ss.isdigit():
            return False
    return True


strings = ['a234', '1234']
answer = [False, True]

for i in range(len(strings)):
    if solution(strings[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')

# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)