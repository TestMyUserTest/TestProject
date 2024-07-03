


#    index    0          1           2
#                                   -1
my_list = ["hello1" , "hello" , "hello3",-3,60,0]

#i є елементами
for i in my_list:
    if "hello3" == i:
        print("OK")

# index - індекс елемента /  elem - елемент
for index, elem in enumerate(my_list):
    if elem == -3:
        print(index)

#index - індекс елемента
for index in range(len(my_list)):
    if my_list[index] == "hello":
        print("ok");



