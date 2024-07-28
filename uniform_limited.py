import heapq
def uls(graph,start_node,goal_node,max_cost):
    priority_queue=[]
    heapq.heappush(priority_queue,(0,[start_node]))
    visited=set()
    while priority_queue:
        cost,path=heapq.heappop(priority_queue)
        current_node=path[-1]
        if current_node==goal_node:
            return path,cost
        if cost<=max_cost:
            if current_node not in visited:
                visited.add(current_node)

                for neighbor,edge_cost in graph.get(current_node,{}).items():
                    if neighbor not in visited:
                        new_cost=cost+edge_cost
                        new_path=path+[neighbor]
                        heapq.heappush(priority_queue,(new_cost,new_path))
    return None,float('inf')
                    
graph={
    'A':{'B':1,'C':4},
    'B':{'A':1,'D':2},
    'C':{'A':4,'D':3},
    'D':{'B':2,'C':3,'E':1},
    'E':{'D':1},
} 
path,total_cost=uls(graph,'A','E',6)

if path:
    print(f"Found path:{path}")
    print(f"Total cost:{total_cost}")
else:
    print("No path found within the specified cost limit")    
