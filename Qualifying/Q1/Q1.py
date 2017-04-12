def solve(A, K):
    steps = 0
    perf = ""

    for i in range(0, len(A)):
        perf = perf + "+"

    perf = list(perf)

    for i in range(0, len(A)-K+1):
        if (perf[i] != A[i]):
            for j in range(0, K):
                if (perf[i+j] == '+'):
                    perf[i+j] = '-'
                else:
                    perf[i+j] = '+'
            #print(perf)
            steps = steps + 1

    final = ''.join(perf)
    if (final == A):
        return steps
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())

    for case in range(1, T+1):
        A, K = [x for x in f.readline().split()]
        answer = solve(A, int(K))
        print("Case #{0}: {1}".format(case, answer))
