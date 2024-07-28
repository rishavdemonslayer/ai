def dfs(graph,start,goal):
    stack=[(start,[start])]
    visited=set([start])
    while stack:
        (node,path)=stack.pop()
        for next_node in graph[node]:
            if next_node not in visited:
                if next_node==goal:
                    return path+[next_node]
                else:
                    visited.add(next_node)
                    stack.append((next_node,path+[next_node]))

    return None

graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
print("dfs:",dfs(graph,'5','7'))                