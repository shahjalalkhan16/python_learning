def make_set():
    n = int(input("Enter how many numbers to input: ")
            )
    emty_arr = []

    for i in range(n):
        element = int(input("Ener element: "))
        emty_arr.append(element)

        in_set = set(emty_arr)

    return in_set

A = make_set()
B = make_set()

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))