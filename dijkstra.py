import heapq

def dijkstra(graph, start, end):

    pq = [(0, start, [])]

    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        if node == end:
            return cost, path

        for next_node, weight in graph[node].items():

            if next_node not in visited:

                heapq.heappush(
                    pq,
                    (
                        cost + weight,
                        next_node,
                        path
                    )
                )

    return float("inf"), []
