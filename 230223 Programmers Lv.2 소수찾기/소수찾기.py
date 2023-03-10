from itertools import permutations
def solution(numbers):
  result = []
  count = 0

  a = list(numbers)
  for i in range(1, len(a)+1):
    for j in permutations(a, i):
      if j[0] != '0':
        result.append(''.join(j))

  for k in set(result):
    if int(k) == 2:
      count += 1
    elif int(k) == 0 or int(k) == 1:
      continue
    else:
      for l in range(2, int(k)):
        if int(k) % l == 0:
          break
      else:
        count += 1
  return count

solution("17")

solution("011")
