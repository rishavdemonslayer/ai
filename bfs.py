from collections import deque
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }

def bfs(graph,start,goal):
    visited=set([start])
    queue=deque([(start,[start])])   
    while queue:
        (node,path)=queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                if next_node==goal:
                    return path+[next_node]
                else:
                    visited.add(next_node)
                    queue.append((next_node,path+[next_node]))

    

print("bfs of the graph is :",bfs(graph,'5','7'))
