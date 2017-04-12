def solve(A):
    iterate = A
    while (iterate >= 0):
        ster = list(str(iterate))
        flag = 0;
        for i in range(0, len(ster) - 1):
            if ster[i] > ster[i+1]:
                ster[i] = int(ster[i]) - 1
                for j in range(i+1, len(ster)):
                    ster[j] = 9
                for j in range(0, len(ster)):
                    ster[j] = str(ster[j])
                iterate = ''.join(ster)
                iterate = int(iterate)
                flag = 1;
                continue

        if (flag == 0):
            return iterate

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())

    for case in range(1, T+1):
        A = f.readline()
        answer = solve(int(A))
        print("Case #{0}: {1}".format(case, answer))
