'''
아이디어
1. 분을 초로 바꾼다.
2. 요리해야할 시간 T를 큰 초부터 나눈다
3. 나머지를 그 다음 작은 수로 나눠준다
'''

time = [300, 60, 10] # 5분, 1분 10초
T = int(input())

if (T % 10 != 0):
    print(-1)
else:
    for i in time:
        quotient = T // i
        print(quotient, end= ' ')
        T = T % i 