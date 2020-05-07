def make_set(str):
    str_lower = str.lower()
    sub_str = []
    
    for idx in range(len(str_lower)-1):
        if ord('a') <= ord(str_lower[idx]) <= ord('z') and ord('a') <= ord(str_lower[idx+1]) <= ord('z'):
            sub_str.append(str_lower[idx:idx+2])
    
    dict_sub_str = dict()
    for key in sub_str:
        if key not in dict_sub_str:
            dict_sub_str[key] = 1
        else:
            dict_sub_str[key] += 1
    return dict_sub_str

def solution(str1, str2):
    dict_str1 = make_set(str1)
    dict_str2 = make_set(str2)
    
    duplicated_sum = sum(dict_str1.values()) + sum(dict_str2.values())
    if not duplicated_sum:
        return 1 * 65536
    

    intersection_num = 0
    for key in dict_str1.keys():
        if key in dict_str2:
            intersection_num += min(dict_str1[key], dict_str2[key])
        
    union_num = duplicated_sum - intersection_num
        
    j_idx = intersection_num / union_num
    
    return int((j_idx  * 65536) // 1)

str1 = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2 = ["french", "shake hands", "AAAA12", "e=m*c^2"]

for i in range(len(str1)):
    print(solution(str1[i], str2[i]))

## 다른 사람의 풀이

def solution(str1, str2):
    str1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    str2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)