from collections import deque


def bfs(graph, start, visited):
    queue = deque([(start)])

    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            queue.extend(graph[node])
            visited[node] = 1
            print(node, end=" ")
        else:
            continue


def dfs(graph, start, visited):

    print(start, end=" ")

    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(graph, i, visited)


if __name__ == "__main__":
    len_node, degree, start = map(int, input().split())

    graph = dict(
        zip([i for i in range(1, len_node + 1)], [[] for i in range(len_node)])
    )

    for i in range(degree):
        node_s, node_d = map(int, input().split())
        graph[node_s].append(node_d)
        graph[node_d].append(node_s)

    for key, value in graph.items():
        value.sort()

    visited = dict(
        zip([i for i in range(1, len_node + 1)], [0 for i in range(len_node)])
    )
    visited[start] = 1
    dfs(graph, start, visited)
    print("")
    visited = dict(
        zip([i for i in range(1, len_node + 1)], [0 for i in range(len_node)])
    )
    bfs(graph, start, visited)
