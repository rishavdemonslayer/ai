import heapq
def ucs(graph,start,goal):
    queue=[(0,start,[start])]
    visited=set([start])
    while queue:
        (cost,node,path)=heapq.heappop(queue)
        if node==goal:
            return path
        for next_node,weight in graph[node].items():
            if next_node not in visited:
                visited.add(next_node)
                heapq.heappush(queue,(cost+weight,next_node,path+[next_node]))
    return None

graph={
    '5':{'3':1,'7':4},
    '3':{'2':2,'4':5},
    '7':{'8':3},
    '2':{},
    '4':{'8':1},
    '8':{}
}            
print("UCS PATH:",ucs(graph,'5','8'))