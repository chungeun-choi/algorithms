if __name__ == "__main__":
    node = int(input())
    degree = int(input())
    graph = dict(zip([i for i in range(1, node + 1)], [[] for i in range(node)]))

    for i in range(degree):
        s_node, d_node = map(int, input().split())
        graph[s_node].append(d_node)
        graph[d_node].append(s_node)

    for _, value in graph.items():
        value.sort()

    def dfs(graph, start):
        keys = graph.keys()
        visited = dict(zip(keys, [0 for i in range(len(keys))]))
        stack = [start]
        visited[start] = 1
        count = 0

        while stack:
            node = stack.pop()

            for i in graph[node]:
                if visited[i] == 0:
                    visited[i] = 1
                    count += 1
                    stack.append(i)

        return count

    print(dfs(graph, 1))
