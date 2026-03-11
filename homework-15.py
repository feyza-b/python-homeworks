from collections import deque
queue = deque()

queue.append("sunday")
queue.append("friday")
queue.append("saturday")

print(queue)

x = queue.popleft()
print(x)

