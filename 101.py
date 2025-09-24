
# Age = input("Enter your age")
# int(Age)
#
# print("you are",Age, "years old")
#
# if Age >= '18':
#     print("you are a teenager")
# else:
#     print("you are kid")


####################################         LISTS           #######################################

# List
# numbers = [7,2,3,4,5,0,7,8,9]
# print(numbers)
# print(type(numbers))
# numbers.sort()
# print(numbers)
# numbers[0] = 99
# print(numbers)
# numbers.append(20) # for add at last
# print(numbers)
# numbers.insert(2,18) # for specific add
# numbers.remove(20)

# print(numbers)
#

# tuples

# child_one = ("Meshal" , "Makkah", "2003/11/06") # tuples cannot be changed
# print(child_one)
# print(child_one[0])
#
# # dictionaries
# child_two = {'name': 'Meshal' , 'age': '21', 'city': 'Makkah' , 'name': 'Ahmad'}
# print(child_two['name'])
# print(child_two.values())
# print(child_two.keys())


##################################        LOOPS           ######################################################

# while loop
# num = 0
#
# while num < 10:
#     print(num)
#     num += 1
#
#
# # for loop
#
# for n in child_one:
#     print(n)
#
# # for in range loop
#
# for n in range(2):
#     print(n)
#



########################################        FUNCTIONS         ##########################################

# def greet():
#     name = input("Enter your name: ")
#     time = input("please enter the time of the day: ")
#     print ("Good" + time + "," + name + "!" )
#
# greet()



########


# def Print_numbers(to):
#     for i in range(to):
#         print(i)
#
#
#
# def add (first, second):
#     return first + second
#
#
# value = add(2,7)
#
# print(value)
# Print_numbers(add(8,2))

###############################                                                    ################################
################################         PROJECT           #########################################################
###############################                                                    ################################
#
#
# phone_book = {
#     "1111111111": "Meshal",
#     "2222222222": "Nawaf",
#     "3333333333": "Abdullah",
#     "4444444444": "Rayan",
#     "5555555555": "Ali",
#     "6666666666": "Ahmad",
#     "7777777777": "Naif"
# }
#
# def is_valid_number(number):
#     count = 0
#     for char in number:
#         count += 1
#     if count != 10:
#         return False
#     for char in number:
#         if char < '0' or char > '9':
#             return False
#     return True
#
# def find_name_by_number():
#     phone_number = input("Enter the phone number: ")
#     if is_valid_number(phone_number):
#         for number in phone_book:
#             if phone_number == number:
#                 print(phone_book[phone_number])
#                 return find_name_by_number()
#         print("Sorry, the number is not found")
#     else:
#         print("This is invalid number")
#
#
# print(find_name_by_number())

###############################           FINISH        #######################################################
