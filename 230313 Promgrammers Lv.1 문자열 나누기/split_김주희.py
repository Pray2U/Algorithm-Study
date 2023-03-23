def solution(s):
  answer = 0
  count1 = 0
  count2 = 0
  while s:
    first = s[0]
    for i in range(len(s)):
      if s[i] == first:
        count1 += 1
      else:
        count2 += 1
      if count1 == count2 or i == len(s) - 1:
        s = s[i+1:]
        answer += 1
        break
  return answer