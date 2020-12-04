def solution(data,n):
    repeats={}
    for i in data:
        if i not in repeats:
            repeats[i] = 1
        else:
            repeats[i] += 1

    target =[]
    for i in repeats.keys():
        if repeats[i] > n:
            target.append(i)
    result =[]
    for x in data:
        if x not in target:
            result.append(x)
    return result
