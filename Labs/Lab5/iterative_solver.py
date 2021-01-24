
def main():
    global dp, w, letters
    w, queries, letters = parse_input()
    for q1, q2 in queries:
        dp = solver(q1, q2)
        print(assemble(q1, q2))


def parse_input():
    letters = input().split(" ")
    w = []
    for _ in range(len(letters)):
        w.append(list(map(int, input().split(" "))))

    queries = []
    for _ in range(int(input())):
        queries.append(input().split(" "))
    return w, queries, letters


def solver(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = -4*i
    for j in range(m+1):
        dp[0][j] = -4*j

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j-1]+w[letters.index(s1[i-1])][letters.index(s2[j-1])], dp[i-1][j]-4, dp[i][j-1]-4)
    return dp


def assemble(s1, s2):
    alignment = []
    n = len(s1)
    m = len(s2)
    while n > 0 and m > 0:
        letter1 = s1[n-1] if n > 0 else "*"
        letter2 = s2[m-1] if m > 0 else "*"
        if dp[n - 1][m - 1] + w[letters.index(s1[n-1])][letters.index(s2[m-1])] == dp[n][m]:
            alignment.append((letter1, letter2))
            n -= 1
            m -= 1

        elif dp[n-1][m] - 4 == dp[n][m]:
            alignment.append((letter1, "*"))
            n -= 1

        else:
            alignment.append(("*", letter2))
            m -= 1

    while n > 0:
        alignment.append((s1[n-1] if n > 0 else "*", "*"))
        n -= 1

    while m > 0:
        alignment.append(("*", s2[m-1] if m > 0 else "*"))
        m -= 1

    alignment.reverse()

    q1 = []
    q2 = []
    for (b, t) in alignment:
        q1.append(b)
        q2.append(t)

    return ''.join(q1) + " " + ''.join(q2)


if __name__ == "__main__":
    main()
