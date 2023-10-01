import heapq


def dijckstra(graph, start):
    INF = 999999999
    distance = {i: INF for i in graph}
    visited = {i: [] for i in graph}
    queue = []
    distance[start] = 0
    heapq.heappush(queue, [distance[start], start])

    while queue:
        current_distance, current_position = heapq.heappop(queue)
        if current_distance > distance[current_position]:
            continue
        for node, value in graph[current_position].items():
            distacne_value = current_distance + value
            if distance[node] > distacne_value:
                visited[node].append(current_position)
                distance[node] = distacne_value
                heapq.heappush(queue, [distacne_value, node])
            else:
                continue

    return distance


def solution(N, road, K):
    answer = 0
    graph = {str(k): {} for k in range(N + 1)}

    for i in road:
        node, end_node, value = i
        node = str(node)
        end_node = str(end_node)

        if end_node not in graph[node] or node not in graph[end_node]:
            graph[node].setdefault(end_node, value)
            graph[end_node].setdefault(node, value)
        else:
            graph[node][end_node] = min(graph[node][end_node], value)
            graph[end_node][node] = min(graph[end_node][node], value)

    test = dijckstra(graph, "1")

    for k, v in test.items():
        if v <= K:
            answer += 1
    return answer



if __name__ == "__main__":
    test_case1 = {
        "N":5,
        "road": [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],
        "K":	3
    }
    test_case2 = {
        "N":6,
        "road": [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],
        "K":4
    }

    assert(solution(**test_case1)==4)
    assert(solution(**test_case2)==4)
    