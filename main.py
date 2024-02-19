def shortestReach(n, edges, s):
    #start node is s
    graph = dict((i, set()) for i in range(1,n+1))
    for c, n, dist in edges:
            graph[c].add((n, dist))
            graph[n].add((c, dist))
        
    print(graph)
        
    shortest = {}
    minheap = [[0, s]]
    
    while minheap:
        w1, n1 = heapq.heappop(minheap)
        if n1 in shortest:
            continue
        
        shortest[n1] = w1
        
        for n2, w2 in graph[n1]:
            if n2 not in shortest:
                heapq.heappush(minheap, [w1+w2, n2])
    
    for i in range(1, n+2):
        print(i)
        if i not in shortest:
            shortest[i] = -1
                
    
    shortest = dict(sorted(shortest.items(), key=lambda x: x[0]))
    
    return [i for i in list(shortest.values())  if i != 0] 
