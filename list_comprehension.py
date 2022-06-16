""" list comprehension : new_list = [new_item for item in list] """
numbers = [1, 2, 3]
new_list = [item + 1 for item in numbers]
print(new_list)  # [2, 3, 4]

name = "rahel"
letters_list = [letter for letter in name]
print(letters_list)  # ['r', 'a', 'h', 'e', 'l']

range_list = [i * 2 for i in range(1, 5)]
print(range_list)  # [2, 4, 6, 8]

""" Conditional list comprehension : new_list = [new_item for item in list if test] """
names = ["rahel", "tamanna", "khusi", "khusbu", "tam", "rexona", "ayan", "alina"]
short_name = [name for name in names if len(name) < 5]
print(short_name)  # ['tam', 'ayan']

uppercase_list = [name.upper() for name in names if len(name) > 5]
print(uppercase_list)  # ['TAMANNA', 'KHUSBU', 'REXONA']

""" List comprehension  Exercise 1 """
numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_number_list = [num ** 2 for num in numbers_1]
print(squared_number_list)  # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

""" List comprehension Exercise 2 """
even_number_list = [num for num in numbers_1 if num % 2 == 0]
print(even_number_list)  # [2, 8, 34]

""" List comprehension Exercise 3 """
with open("./Text Data/text_1.txt") as file_1:
    content_1 = file_1.readlines()
    list_1 = [item.strip() for item in content_1]
    print(list_1)
with open("./Text Data/text_2.txt") as file_2:
    content_2 = file_2.readlines()
    list_2 = [item.strip() for item in content_2]
    print(list_2)

result = [int(item) for item in list_1 if item in list_2]
print(result)  # [3, 6, 5, 33, 12, 7, 42, 13]



