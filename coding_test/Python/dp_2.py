# 개미 전사

'''
입력 조건
- 첫째 줄에 식량창고의 개수 N이 주어진다. (3 <= N <=100)
- 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (0 <= K <= 1000)

출력 조건
- 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.

입력 예시
4
1 3 1 5

출력 예시
8
'''

n = int(input())

array = list(map(int, input().split()))

d = [0]*100

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])