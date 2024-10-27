# interface.py
from trace_edge import xy_image
from collections import deque
import time

edges = xy_image("NJIT_logo.png")  # create image object
edges.detect_edge()  # returns an array of bool -True for white pixel

# create a path which the robot will follow
path = []
# double ended list
q = deque()
r, c = 0, 0  # initialize a point that we can continue searching for points from
first = edges.find(r, c)  # find first point
r, c = first  # set the point to the newly found to continue from there
# append first white to queue and path
q.append(first)
path.append(first)

# performance testing ---
start = time.time()

whites = edges.white

while len(path) != whites:
    # if queue has elements we should continue finding from there
    if q:
        node = q.popleft()
        path.append(node)
        q.extend(edges.search(node[0], node[1]))
    else:
        # if queue is exahusted find new point
        p = edges.find(r, c)
        r, c = p
        q.append(p)
        path.append(p)

end = time.time()
print(len(path), end - start)
