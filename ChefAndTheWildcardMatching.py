T = int(input())
while T > 0:
    X = input()
    Y = input()
    flag = 0
    if len(X) == len(Y):
        for i in range(len(X)):
            if X[i] != '?' and Y[i] != '?' and X[i] != Y[i]:
                flag = 1
                break
        if flag == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    T -= 1
