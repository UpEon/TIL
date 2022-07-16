# 모험가 길드

'''
입력 조건
- 첫째 줄에 모험가의 수 N이 주어진다. (1 <= N <= 100000)
- 둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

출력 조건
- 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

입력 예시
5
2 3 1 2 2

출력 예시
2
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)