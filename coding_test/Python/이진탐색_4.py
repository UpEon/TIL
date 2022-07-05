# 떡볶이 떡 만들기
'''
입력 조건
- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
- 둘째 줄에 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님이 필요한 양만큼
떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

출력 조건
- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

입력 예시
4 6
19 15 10 17

출력 예시
15
'''

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid -1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid
        start = mid + 1

print(result)
