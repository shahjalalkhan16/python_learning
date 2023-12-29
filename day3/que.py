from queue import Queue

q = Queue()

q.put("a")
q.put("b")
q.put("c")

print(q.get())

if q.empty() is True:
    print("Queue is  empty")

else:
    print("Queue is not empty")