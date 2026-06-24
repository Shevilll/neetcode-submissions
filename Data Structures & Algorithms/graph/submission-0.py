class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        queue = deque()
        queue.append(src)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
        
        return False

