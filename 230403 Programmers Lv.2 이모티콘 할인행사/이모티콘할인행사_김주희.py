from itertools import product
def solution(users, emoticons):
    a = [10, 20, 30, 40]
    answer = []
    for i in product(a, repeat=len(emoticons)):
      price2 = 0
      count = 0
      for j in users:
        price = 0
        for k in range(len(emoticons)):
          if i[k] >= j[0]:
            price += emoticons[k] * (100-i[k]) / 100
        if price >= j[1]:
          count += 1
        else:
          price2 += price
      answer.append([count, int(price2)])
    answer.sort(key = lambda x : (-x[0], -x[1]))
    return answer[0]