import time


def main():
    #start_time = time.time()
    graph, queries = parse_input()
    #print("--- %s seconds ---" % (time.time() - start_time))
    #start_time = time.time()
    path_length = BFS(graph, queries[0][0], queries[0][1])
    #print("--- %s seconds ---" % (time.time() - start_time))

    for source, destination in queries:
        path_length = BFS(graph, source, destination)
        if path_length is None:
            print("Impossible")
        else:
            print(path_length)


def parse_input():
    # N = Number of words, Q = number of queries
    N, Q = map(int, input().split(" "))

    # Save the words
    words = []
    for i in range(N):
        words.append(input())

    # Save the queries
    queries = []
    for i in range(Q):
        queries.append((input().split(" ")))

    # Adjacency list
    graph = {}
    for w in words:
        neighbors = []
        for neighbor in words:
            if neighbor != w:
                temp = neighbor
                for char in w[1:]:
                    temp = temp.replace(char, '', 1)
                if len(temp) == 1:
                    neighbors.append(neighbor)
        graph[w] = neighbors
    return graph, queries


def BFS(graph, source, destination):
    queue = [source]
    visited = {}
    pred = {}

    # Mark source as visited
    visited[source] = True

    # If source and destination are the same, return 0
    if source == destination:
        return 0

    while queue != []:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
                pred[neighbor] = current

                if neighbor == destination:
                    # Found a path! Traverse backwards and return the path length
                    path_length = 1
                    while pred[neighbor] != source:
                        neighbor = pred[neighbor]
                        path_length += 1
                    # Return the length of the path
                    return path_length
    # Could not find a path
    return None


if __name__ == "__main__":
    main()
