from collections import deque
queue = deque()

queue.append("monday")
queue.append("friday")
queue.append("saturday")

print(queue)

x = queue.popleft()
print(x)

