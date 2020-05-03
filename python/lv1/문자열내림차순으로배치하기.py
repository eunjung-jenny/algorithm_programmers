def solution(s):
    return ''.join(sorted(s, reverse=True))


strings = ['Zbcdefg']
answer = ['gfedcbZ']

for i in range(len(strings)):
    if solution(strings[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')