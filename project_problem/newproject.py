import os


files = os.listdir("submission")

extentions = []

for file in files:
    filename_parts = file.split(".")
    extention = filename_parts[-1]
    extentions.append(extention)


print(extentions)

#find unique extentions
unique_exts = list(set(extentions))

countTotal = {}
for i in unique_exts:
    count = extentions.count(i)
    countTotal[i] = count

print(countTotal)

## using library function
from collections import Counter

countTotalUsingLibrary = Counter(extentions)
print(countTotalUsingLibrary)