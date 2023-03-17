
from collections import defaultdict
from itertools import combinations
def solution(info,query):
    answer = []
    dic = defaultdict(list)
    
    for i in info:
        inf = i.split(' ')
        tmp = inf[:-1]
        score = int(inf[-1])
        for j in range(5):
            idxList = list(combinations(range(4),j))
            for idx in idxList:    
                tmpCopy = tmp.copy()
                for id in idx:
                    tmpCopy[id] = '-'
                key = ''.join(tmpCopy)
                dic[key].append(score)
    
    for value in dic.values():
        value.sort()
    for q_value in query:
        tmp = q_value.replace('and ', '')
        query_list = tmp.split()
        
        queryKey = ''.join(query_list[:-1])
        queryScore = int(query_list[-1])
    
        cnt = 0
        
        if queryKey in dic:
            target_list = dic[queryKey]
            idx = binarySearch(target_list ,queryScore)
            cnt = len(target_list) - idx
        
        answer.append(cnt)
        
    return answer
        

def binarySearch(data,value):
    low = 0
    high = len(data)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if data[mid] < value:
            low = mid+1
        else:
            high = mid-1
                
    return low

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))