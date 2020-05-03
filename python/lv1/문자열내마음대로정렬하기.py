def solution(strings, n):
    chars = sorted(list(set(word[n] for word in strings)))

    my_dict = {}
    for word in strings:
        if word[n] in my_dict:
            my_dict[word[n]].append(word)
        else:
            my_dict[word[n]] = [word]
    
    for char in my_dict.keys():
        my_dict[char] = sorted(my_dict[char])

    answer = []
    for char in chars:
        answer.extend(my_dict[char])

    return answer

strings = [['sun', 'bed', 'car'], ['abce', 'abcd', 'cdx']]
n = [1, 2]
answer = [['car', 'bed', 'sun'], ['abcd', 'abce', 'cdx']]

for i in range(len(strings)):
    if solution(strings[i], n[i]) == answer[i]:
        print(f'{i+1}: pass')
    else:
        print(f'{i+1}: fail')