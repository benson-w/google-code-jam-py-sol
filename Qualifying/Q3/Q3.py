def solve(N, K):
    people = K
    a= [0] * (N + 2)
    for i in range(0, N+2):
        a[i] = [i,N + 2 - i -1]
    a[0] = [0,0]
    a[N+1] = [0,0]
    minl = [0] * (N)
    maxl = [0] * (N)

    while (people > -1):
        currmax = 0
        setindex = 0
        x = []
        localmax = 0;

        # find placing person
        for i in range(1, N):
            if (min(a[i]) > currmax and max(a[i]) != 0):
                x = []
                x.append([a[i], i])
                currmax = min(a[i])
            if (min(a[i]) == currmax and max(a[i]) != 0):
                x.append([a[i], i])

        for i in range(1, len(x)):
            if (max(x[i][0]) > localmax):
                maxl[i] = max(x[i][0])
                minl[i] = min(x[i][0])
                localmax = max(x[i][0])
                setindex = x[i][1]

            if (people -1 == 0):
                return (maxl[i]-1, minl[i]-1)

        a[setindex] = [0,0]

        # check left
        for i in range(1, N+2):
            if (a[setindex - i] == [0,0]):
                break;
            if (i < a[setindex - i][1]):
                a[setindex - i][1] = i;

        # check right
        for i in range(1, N+2):
            if (a[setindex + i] == [0,0]):
                break;
            if (i < a[setindex + i][0]):
                a[setindex + i][0] = i;

        people = people - 1


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())

    for case in range(1, T+1):
        N, K = [x for x in f.readline().split()]
        (answer1, answer2) = solve(int(N), int(K))
        print("Case #{0}: {1} {2}".format(case, answer1, answer2))
