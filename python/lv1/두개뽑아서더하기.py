def solution(numbers):
    answerSet = set()
    for i in range(len(numbers)):
        first_num = numbers[i]
        for j in range(len(numbers)):
            second_num = numbers[j]
            if i != j:
                sum_num = first_num + second_num
                answerSet.add(sum_num)

    return list(sorted(answerSet))


numbers = [[2, 1, 3, 4, 1], [5, 0, 2, 7]]
result = [[2, 3, 4, 5, 6, 7], [2, 5, 7, 9, 12]]

for i in range(len(numbers)):
    if result[i] == solution(numbers[i]):
        print("pass")
    else:
        print("fail")
