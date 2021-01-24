def main():
    N, edges = parse_input()
    T, sum = kruskal(N, edges)
    print(sum)


def parse_input():
    # O(M)
    N, M = map(int, input().split(" "))
    edges = [[]] * M
    for i in range(M):
        u, v, w = map(int, input().split(" "))
        edges[i] = [u-1, v-1, w]

    # O(Mlog(M))
    # Sort by weight
    edges.sort(key=lambda x: x[2])
    return N, edges


def kruskal(N, edges):
    global parents
    global children
    parents = [None]*N
    children = [0]*N
    T = []
    sum = 0
    # O(M)
    for edge in edges:
        if union(edge):
            T.append(edge)
            sum += edge[2]
    return T, sum


def union(e):
    global parents, children
    u = find(e[0])
    v = find(e[1])
    if u == v:
        return False
    else:
        if children[u] < children[v]:
            parents[u] = v
            children[v] += children[u]
        else:
            parents[v] = u
            children[u] += children[v]
        return True


def find(v):
    global parents
    p = v
    while parents[p] is not None:
        p = parents[p]

    while parents[v] is not None:
        w = parents[v]
        parents[v] = p
        v = w
    return p


if __name__ == "__main__":
    main()
