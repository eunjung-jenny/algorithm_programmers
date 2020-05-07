zones = {'S': 1, 'D': 2, 'T': 3}
options = {'*': 2, '#': -1}

def solution(dartResult):
    scores = []
    temp = ''
    for i in range(len(dartResult)):
        char = dartResult[i]           
        if char.isdigit():
            temp += char
            if dartResult[i+1].isdigit():
                continue
            scores.append(int(temp))
            temp = ''
        elif char in zones:
            scores[-1] **= zones[char]
        elif char in options:
            if char == '*':
                scores[-1] *= options[char]
                if len(scores) >= 2:
                    scores[-2] *= options[char]
            else:
                scores[-1] *= options[char]
        
    return sum(scores)

dartResult = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']


for i in range(len(dartResult)):
    print(solution(dartResult[i]))