def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu']
    diff_days = sum(days[0:a-1]) + b - 1
    answer = date[diff_days % 7].upper()
    
    return answer

a = [5]
b = [24]
answer = ["TUE"]

for i in range(len(a)):
    if solution(a[i], b[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')