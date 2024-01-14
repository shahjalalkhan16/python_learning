# # file_object = open(file_name, "mode")
# # file_object.close

# with open("mytext1.txt", "w") as file:
#     file.write("Hello world!")



# with open("mytext1.txt", "r") as file:
#     print(file.read())


# with open("mytext1.txt", "a") as file:
#     file.write("Added this")


# # append new text
# f = open("mytext.txt",'a')
# f.write(""+" Now upgrade it")
# f.close()



# f = open("mytext.txt", "r")
# print(f.read())


# ## create a new file
# f = open("newfile.txt", "x")


## delete  file

import os

if os.path.exists("newfile.txt"):
   os.remove("newfile.txt")
else:
   print("File doesnt exits")
