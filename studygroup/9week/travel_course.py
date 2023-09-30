import heapq
def solution(tickets):
    answer = []
    main_start = tickets[0][0]
    graph = {}

    for start,dest in tickets:
        if start not in graph:
            graph[start] = [dest]
        else:
            heapq.heappush(graph[start],dest)

    def dfs(start):
        answer.append(start)
        if start not in graph or len(graph[start]) == 0 :
            return
        dest = heapq.heappop(graph[start])          
        dfs(dest)
    
    dfs(main_start)
    
    return answer


if __name__ == "__main__":
    test_case1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    test_case2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    test_case3 = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]

    assert(solution(test_case1)==["ICN", "JFK", "HND", "IAD"])
    assert(solution(test_case2)==["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
    solution(test_case3)


