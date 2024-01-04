data = []

n = int(input("Enter a number: "))
for i in range(1,n+1):
    # print('Here is', i)
    if  n % i == 0:
        data.append(i)
       # print(i)

print(data)


#divisor
# def divisors(n):
#     for i in range(1,n+1):
#         print('here is ', i)
#         if n%i ==0:
#             print(i)
#             data.append(i)


# divisors(int(input("Enter a value: ")))

# print(data)