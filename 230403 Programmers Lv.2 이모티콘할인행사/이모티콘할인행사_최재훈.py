from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    allCase = []

    for i in product([10,20,30,40], repeat=len(emoticons)):
        allCase.append(list(i))
    print(f'allCase : {allCase}')

    for each_case in allCase:
        serviceUser, totalPrice = 0, 0

        for user in users:
            sale_value, max_price = user
            sale_emoticon = 0

            for i, sale in enumerate(each_case):
                if sale_value <= sale:
                    sale_emoticon += (emoticons[i] * (100 - sale) / 100)

            if sale_emoticon >= max_price:
                serviceUser += 1
            else:
                totalPrice += sale_emoticon
            print(f'sale_value : {sale_value} / max_price : {max_price}')
            print(f'totalPrice : {totalPrice}')
        if serviceUser > answer[0]:
            answer[0], answer[1] = serviceUser, int(totalPrice)
        elif serviceUser == answer[0] and totalPrice > answer[1]:
            answer[1] = int(totalPrice)

    return answer


print(solution([[40, 10000], [25, 10000]], [7000,9000])) # [1, 5400]
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])) # [4, 13860]