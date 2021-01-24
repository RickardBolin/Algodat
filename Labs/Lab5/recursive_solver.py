import sys
sys.setrecursionlimit(10**9)


def main():
    global matrix, letters, queries, lookUp
    matrix, queries, letters = parse_input()

    for q in queries:
        m, n = len(q[0]), len(q[1])
        lookUp = [[[0, -1] for x in range(n)] for x in range(m)]
        recursive_solver(q[0], q[1], m, n)

        print(assemble(q[0], q[1]))


def parse_input():
    letters = input().split(" ")
    k = len(letters)
    matrix = []
    for line in range(k):
        row = input().split(" ")
        matrix.append(row)

    nbQueries = int(input())
    queries = []
    for q in range(nbQueries):
        queries.append(input().split(" "))

    return matrix, queries, letters


def recursive_solver(str1, str2, m, n):

    global lookUp, matrix, letters

    if lookUp[m][n][0] is not 0:
        return lookUp[m][n]
    else:

        # If first string is empty
        if m == 0:
            lookUp[m][n] = [-4*n, 1]

        # If second string is empty
        elif n == 0:
            lookUp[m][n] = [-4*m, 2]

        else:
            letter1 = str1[m - 1]
            letter2 = str2[n - 1]

            p1, _ = recursive_solver(str1, str2, m-1, n - 1)
            p1 += int(matrix[letters.index(letter1)][letters.index(letter2)])
            p2, _ = recursive_solver(str1, str2, m, n - 1)
            p2 -= 4
            p3, _ = recursive_solver(str1, str2, m-1, n)
            p3 -= 4
            p = max(p1, p2, p3)

            if p == p1:
                position = 0
            elif p == p2:
                position = 1
            else:
                position = 2

            lookUp[m][n] = [p, position]
        return lookUp[m][n]


def assemble(DNA1, DNA2):
    global lookUp
    word1 = ""
    word2 = ""

    pos1 = len(DNA1)
    pos2 = len(DNA2)
    print(lookUp)
    # Append until no more cases left
    while pos1 > -1 or pos2 > -1:
        _, case = lookUp[pos1][pos2]

        new_letter1 = DNA1[pos1-1] if pos1 > -1 else "*"
        new_letter2 = DNA2[pos2-1] if pos2 > -1 else "*"

        if case == 0:
            word1 = new_letter1 + word1
            word2 = new_letter2 + word2
            pos1 -= 1
            pos2 -= 1
        elif case == 1:
            word1 = "*" + word1
            word2 = new_letter2 + word2
            pos2 -= 1
        else:
            word1 = new_letter1 + word1
            word2 = "*" + word2
            pos1 -= 1

    return word1 + " " + word2


if __name__ == "__main__":
    main()
