from collections import deque
from queue import PriorityQueue

pqueue=PriorityQueue()

pqueue.put([-10,10])

pqueue.put([-10000,10000])

pqueue.put([-1000,1000])

while pqueue:
    g=pqueue.get()
    print(g[1])
