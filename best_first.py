import heapq
def heuristic(n):
    H_dist={
        'A':11,'B':6,'C':5,'D':7,'E':3,
        'F':6,'G':5,'H':3,'I':1,'J':0
    }                
    return H_dist[n]
Graph_nodes={
    'A':[('B',6),('F',3)],
    'B':[('A',6),('C',3),('D',2)],
    'C':[('B',3),('D',1),('E',5)],
    'D':[('B',2),('C',1),('E',8)],
    'E':[('C',5),('D',8),('I',5),('J',5)],
    'F':[('A',3),('G',1),('H',7)],
    'G':[('F',1),('I',3)],
    'H':[('F',7),('I',2)],
    'I':[('E',5),('G',3),('H',2),('J',3)],
}

def best_first(start_node,stop_node):
    open_set=[(heuristic(start_node),start_node)]
    closed_set=set()
    parents={start_node:start_node}

    while open_set:
        _,n=heapq.heappop(open_set)
        if n==stop_node or (Graph_nodes[n] is None):
            break
        closed_set.add(n)
        for m,_ in Graph_nodes[n]:
            if m not in closed_set and (m not in parents):
                heapq.heappush(open_set,(heuristic(m),m))
                parents[m]=n
    if stop_node not in parents:
        print("path does not exist")
        return None
    path=[]
    while stop_node!=start_node:
        path.append(stop_node)
        stop_node=parents[stop_node]
    path.append(start_node)
    path.reverse()
    print("path found:{}".format(path))
    return path
best_first('A','J')