
def main():
    graph, queries = parse_input()
    BFS(graph, queries)

def parse_input():

    # N = Number of words, Q = number of queries
    N, Q = map(int, input().split(" "))

    # Save the words
    words = [] * N
    for i in range(N):
        words.append(input())

    # Save the queries
    queries = [] * Q
    for i in range(Q):
        queries.append((input().split(" ")))

    # Adjacency list
    graph = {}
    for w in words:
        neighbors = []
        for neig in words:
            # Sort it and check if abcde[1:] = bcde or abcde[:-1] = abcd
            if (''.join(sorted(neig))[1:] == ''.join(sorted(w[1:])) or ''.join(sorted(neig))[:-1] == ''.join(sorted(w[1:]))) and neig != w:
                neighbors.append(neig)
        graph[w] = neighbors
    return graph,queries

def BFS(graph,queries):
    path = []
    for q in queries:
       test = 1

if __name__ == "__main__":
    main()