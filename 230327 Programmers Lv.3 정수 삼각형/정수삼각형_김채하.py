def solution(triangle):
    sumtriangle = []
    sumtriangle.append(triangle[0])
    for arr in triangle[1:]:
        li = []
        for numind, num in enumerate(arr):
            if numind == 0:
                li.append(num+sumtriangle[-1][0])
            elif numind == len(arr)-1:
                li.append(num+sumtriangle[-1][-1])
            else:
                li.append(num+max(sumtriangle[-1][numind-1:numind+1]))
        sumtriangle.append(li)

    return max(sumtriangle[-1])