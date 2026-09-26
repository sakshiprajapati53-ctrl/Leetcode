visited = set() # create  an empty set of visited value store hogi

def dfs(node): # put all node 
    if node in visited: #agar visited true hai hai to 
        return          #return kar do usi ko
       

    visited.add(node) #Current node ko visited mark kar do.
    print(node)

    for neighbour in graph[node]: # Ab current node ke neighbours dekho.
        dfs(neighbour) # dfs ab node ---> neighbour ke depth me jaye ga and check kare ga ,DFS call hoga

dfs(0) # first dfs(0) se start hoga