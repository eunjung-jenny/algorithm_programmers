def solution(phone_number): 
    return '*'*(len(phone_number) - 4) + phone_number[-4:]

phone_number = ['01033334444', '027778888']
result = ['*******4444', '*****8888']

for i in range(len(phone_number)):
    if solution(phone_number[i]) == result[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')