from itertools import product

def solution(info, query):
    items = [['cpp',"java","python"], ["backend","frontend"], ["junior","senior"],["chicken","pizza"]]
    val = list(product(*items))
    answer = []
    val_dic = {''.join(v[:4]):[] for v in val}
    for inf in info:
        value = inf.split(" ")
        key = ''.join(value[:4])
        score = int(value[4])
        val_dic[key] += [score]
    for con in query:
        corect = 0
        con = con.replace(" and "," ")
        li =con.split()
        conli = []
        for ind, condition in enumerate(li):
            if ind == 4:
                if condition == '-':
                    conli.append([0])
                else:
                    conli.append([int(condition)])
            elif condition == '-':
                conli.append(items[ind])
            else :
                conli.append([condition])
        for condi in list(product(*conli)):
            print(condi)
            score = condi[4]
            condi = ''.join(condi[:4])
            for sco in val_dic[condi]:
                if sco >= score:
                    corect +=1
        answer += [corect]
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))