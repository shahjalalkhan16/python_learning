output = []

#continue ,  break and pass
# for i in range(100):
#     if i%2 == 0:
#         continue
#     output.append(i)

# print(output)

# for i in range(100):
#    print('number is', i)
# else:
#    print('All done!')

# for i in range(5):
#     pass

# for i in range(5):
#     print('here i is ', i)
#     if i > 3: 
#         break
# else:
#     print("all done!")

def is_prime(n):
    if n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    for i in range(2, n):
        print('checking ', i)
        if n % i == 0:
            return False
        
    return True


number = int(input("Enter a number: "))

if is_prime(number) == True:
    print(f"{number} is prime")
else:
    print(f'{number} is not prime')