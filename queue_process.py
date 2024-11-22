from collections import deque
stack = deque()
a = input()
a = a.split(" ")
for i in range(len(a)):
    stack.appendleft(a[i])
print(stack)
while stack:
    b = stack.pop()
    if "a" in b:
        print(b)