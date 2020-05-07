def solution(n, arr1, arr2): 
    # n: size
    # 0 => 빈칸 => ' ' => 모두 공백이면 공백
    # 1 => 벽 => '#' => 둘 중 하나라도 벽이면 벽
    result = []

    for i in range(n):
        temp_1 = ('0'*n + bin(arr1[i])[2:])[-n:]
        temp_2 = ('0'*n + bin(arr2[i])[2:])[-n:]

        decoded = ''
        for j in range(n):
            if temp_1[j] == '1' or temp_2[j] == '1':
                decoded += '#'
            else:
                decoded += ' '
        
        result.append(decoded)

    # print(result)
    return result

n = [5, 6]
arr1 = [[9, 20, 28, 18, 11], [46, 33, 33, 22, 31, 50]]
arr2 = [[30, 1, 21, 17, 28], [27, 56, 19, 14, 14, 10]]
result = [["#####","# # #", "### #", "# ##", "#####"], ["######", "### #", "## ##", " #### ", " #####", "### # "]]

for i in range(len(n)):
    # solution(n[i], arr1[i], arr2[i])
    if solution(n[i], arr1[i], arr2[i]) == result[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')

## 비트연산!
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer

# zip
# 비트연산 & | ^ ~
# rjust : 정렬