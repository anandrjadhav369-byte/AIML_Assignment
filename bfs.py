from collections import deque 
graph = {} 

n = int(input("Enter number of nodes: ")) 

for _ in range(n): 
    node = input("Node: ") 
    graph[node] = input(f"Neighbours of {node}: ").split()
start = input("Enter starting node: ") 

def bfs(start): 
    q = deque([start]) 
    vis = {start} 
    while q: 
        v = q.popleft() 
        print(v, end=" ") 

        for i in graph[v]: 
            if i not in vis: 
                vis.add(i) 
                q.append(i) 

print("\nBFS Traversal:")
bfs(start)


#BFS HOGAYA
