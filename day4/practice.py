Number = int(input("Enter your number"))
output = []
if Number ==1:
    print("Not prime")
elif Number > 1:
        for i in range(Number):
          if i%2 ==0:
            continue
          else:
              output.append(i)
           
print(output)

