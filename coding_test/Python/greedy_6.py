# 곱하기 혹은 더하기

'''
입력 조건
- 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 s가 주어집니다. (1<=s의 길이 <=20)

출력 조건
- 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

입력 예시 1
02984

출력 예시 1
576
'''

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)