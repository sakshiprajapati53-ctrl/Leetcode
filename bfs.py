from collections import deque # import deque

visited = set() # store visted value in set
queue = deque() # queue of 

queue.append(0) # first append 0 node in queue
visited.add(0) # add 0 th node to visited

while queue: # whike queue is not empty
    node = queue.popleft() # pop the node from the left side

    print(node)

    for neighbour in graph[node]: # visit every neighbour of that started node 
        if neighbour not in visited: # not visited neighbour
            visited.add(neighbour) # add it to visisted 
            queue.append(neighbour) # push neighbour into queue