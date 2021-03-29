import os

my_list = ["Hello", "Bye"]
with open("my_first_text_file.txt", "w+") as text_file_1:
    f1 = text_file_1.readlines()
    for i in my_list:
        text_file_1.write(i)
        print("line in 1st file: " + i)

my_2_list = ["World", ":)"]
with open("my_second_text_file.txt", "w+") as text_file_2:
    f2 = text_file_2.readlines()
    for j in my_2_list:
        text_file_2.write(j)
        print("line in 2st file: " + j)
res_file = open("res_txt_file.txt", "w+")
f11 = open("my_first_text_file.txt", "r")
f22 = open("my_second_text_file.txt", "r")
for x in f11:
    y = f22.readline()
    res_file.write(x + y)
    print(x + '\n' + y )
os.remove("my_first_text_file.txt")
os.remove("my_second_text_file.txt")
