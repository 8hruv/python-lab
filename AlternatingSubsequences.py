T = int(input())
while T > 0:
    N = int(input())
    A = list(map(int, input().split()))[:N]
    temp1 = 0
    temp2 = 0
    for i in range(N):
        if i % 2 == 0:
            temp1 += A[i]
        else:
            temp2 += A[i]
    if temp1 > temp2:
        print(temp1)
    else:
        print(temp2)
    T -= 1
