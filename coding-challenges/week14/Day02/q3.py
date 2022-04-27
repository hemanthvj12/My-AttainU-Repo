def allPathsSourceTarget(graph):
    result = []
    partialResult = []

    def findPath(node):
        if node == len(graph)-1:
            result.append(partialResult.copy())
            return

        for i in graph[node]:
            partialResult.append(i)
            findPath(i)
            partialResult.pop()

    partialResult.append(0)
    findPath(0)
    return result
