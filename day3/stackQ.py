stack = []

#append | push
#pop
#size
#check if empty
#view topmost element


stack.append("a")
stack.append("b")
stack.append("c")


print(stack)

# stack.pop()
print("Top most stack", stack.pop())

print("After poping ", stack)

print("Size of stack", len(stack)) 

print(list(stack)) 






# #using library 
# from collections import deque

# numbers = deque()

# numbers.append(88)
# numbers.append(33)
# numbers.append(11)

# print(numbers)

# print(list(numbers))


#queue
from collections import deque

queue = deque()

queue.append(88)
queue.append(33)
queue.append(11)

print(queue)

print(list(queue))

first_item = queue.popleft()
print("After queue ",first_item )

