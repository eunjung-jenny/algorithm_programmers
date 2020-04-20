def solution(arr, divisor):
    answer = [num for num in arr if not (num % divisor)]    
    return sorted(answer) if answer else [-1]