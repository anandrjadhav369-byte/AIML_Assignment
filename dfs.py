graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n): 
    node = input("Node: ") 
    graph[node] = input(f"Neighbours of {node}: ").split() 

start = input("Enter starting node: ") 

def dfs(v, vis): 
    print(v, end=" ") 
    vis.add(v) 

    for i in graph[v]:
        if i not in vis: 
            dfs(i, vis) 

print("\nDFS Traversal:")
dfs(start, set())

