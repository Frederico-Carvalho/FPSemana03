from collections import deque
stack = deque()
a = input("").split()
for i in a:
    stack.append(int(i))
print(stack)
while stack:
    x = stack.pop()
    print(x * 2)