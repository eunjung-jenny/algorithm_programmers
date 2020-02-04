# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

import datetime

def solution(a, b):
    base = '20160101'
    if a < 10:
        a = '0'+str(a)
    else:
        a = str(a)
    
    if b < 10:
        b = '0'+str(b)
    else:
        b = str(b)

    target = '2016' + a + b

    datetime.datetime(target[:4])
    return answer

