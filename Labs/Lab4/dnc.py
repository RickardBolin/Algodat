import math
import sys


def main():
    N, P_x = parse_input()
    # Print with 6 decimal precision
    print('%.6f'%dnc(N, P_x, 1e10))


def parse_input():
    data = sys.stdin.read().split('\n')
    N = int(data[0])
    P = [(int(d.split()[0]), int(d.split()[1])) for d in data[1:-1]]
    P.sort()#key=lambda x: x[0])
    return N, P


def dnc(N, P_x, min_dist):
    if N > 3:
        mid = N//2
        L_x, R_x = P_x[:mid], P_x[mid:]
        d_l = dnc(mid, L_x, min_dist)
        d_r = dnc(mid, R_x, min_dist)

        # Compare over the border
        delta = min(d_l, d_r)

        # Create set S from P_y
        mid_val = P_x[mid][0]
        S = [p for p in P_x if abs(p[0] - mid_val) < delta]
        S.sort(key=lambda x: x[1]) # Extra log-faktor???
        l = len(S)
        for i, point in enumerate(S):
            K = min(15, l - i)       # Is 15 correct here...?
            for j in range(1, K):
                delta = min(delta, dist(point, S[i + j]))
        return delta

    else:
        return min(min_dist, shortest_dist(N, P_x))


def shortest_dist(N, P_x):
    if N == 3:
        return min(min(dist(P_x[0], P_x[1]), dist(P_x[0], P_x[2])), dist(P_x[1], P_x[2]))
    elif N == 2:
        return dist(P_x[0], P_x[1])
    else:
        return 1e10


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == "__main__":
    main()
