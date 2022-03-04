# cook your dish here
T = int(input())
while T > 0:
    N, K = map(int, input().split())
    temp = 0
    for i in range(1, K + 1):
        if N % i > temp:
            temp = N % i
    print(temp)
    T -= 1