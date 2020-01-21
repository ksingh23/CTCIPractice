from collections import deque


class Graph:
    def __init__(self, length):
        self.length = length
        self.adj = []
        for i in range(length):
            self.adj.append([])

    def add_edge(self, n1, n2):
        self.adj[n1].append(n2)

    def route_between_nodes(self, n1, n2):
        n1_visited = [False] * self.length
        n2_visited = [False] * self.length
        d1, d2 = deque(), deque()
        d1.append(n1)
        d2.append(n2)
        n1_visited[n1] = True
        n2_visited[n2] = True
        while d1 and d2:
            node1 = d1.popleft()
            node2 = d2.popleft()
            if node1 == n2 or node2 == n1:
                return True
            for n in self.adj[node1]:
                if not n1_visited[n]:
                    n1_visited[n] = True
                    d1.append(n)
            for n in self.adj[node2]:
                if not n2_visited[n]:
                    n2_visited[n] = True
                    d2.append(n)
            for i in range(self.length):
                if n1_visited[i] and n2_visited[i]:
                    return True
        return False
