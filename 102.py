
#######################################     102       ##############################################################################

###############################                                                    ################################
#####################################             Tables and Numbers             ################################################################
###############################                                                    ################################


############               abs               ###################################################################
#
# NUM = -99
#
# print(abs(NUM))
#
# ##################        round      ########################################
#
# num2 = 3.8943
# print(round(num2, 2))
#
# ##############        pow    max     min    sum  ###############################################################
#
# num3 = 4
# print(pow(num3, 2))
#

# nums = 100, 200, 300, 400, 500
#
# print(max(nums))
# print(min(nums))
# print(sum(nums))

##############          math.sqrt  remainder          ################################################

# import math
#
# print(math.sqrt(81))
# print(math.remainder(9,2))
# print(math.ceil)
# print(math.floor)

###################       random.randin          t#################################################
#
# import random
#
# rnd= random.randint(1,100)
# print(rnd)

####################         DATE    TIME       #####################################################
#
# import datetime
#
# time = datetime.time(8, 9 , 20)
# date = datetime.date(2025, 9 , 9)
#
# print(time.hour)
# print(date.year)
# print(date.month)
# print(date.day)
#
# print(date.strftime("%A, %B %d, %Y"))
#
# print(datetime.datetime.today())


###############################                                                    ################################
#####################################             ADVANCED SEQUENCE             ################################################################
###############################                                                    ################################


###################################                 INDEXING        ############################

alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# print(alphabet[-1]) # Prints Z
#
# for letter in alphabet:
#     print(letter)  # Prints all letters

###################################                 SLICING        ############################

# text = 'This is Python Course'
# print(text[8:14])
# print(text[-6:])
#
# print(alphabet[0:7:2]) # The last number is the number of jumping amount
# print(alphabet[5:0:-1]) # Reverse Jumping

###################################                 SLICE        ############################

#
# s = slice(0,5,2) # slice like slicing same work
# print(alphabet[s])

###################################                 INDEX        ############################
# print(alphabet.index('yz')) # return the index

###################################                 LEN        ############################

# print(len(alphabet)) # focus this function is written before the variable

###################################                 COUNT        ############################

# print(alphabet.count('a'))

###################################                  IN          #############################
# print('ab' in  alphabet)

###################################                 REPEAT       ##############################

# name= 'Meshal '
# print(name*3)




###############################                                                    ################################
#####################################             ADVANCED STRINGS             ####################################
###############################                                                    ################################


##############################          FIND               ##########################################

# textf= "Hello World My name is Meshal Alsaedi"
# print(textf.find('My')) # find to find first find caracters's index or -1
# print(textf.rfind('M')) # find to find last find  caracters's index or -1
# print(textf.find('M', 20 )) # chose start index to search finding

#######################################        SPLIT           ####################################

# texts = 'abd bah jij kdk'
# strig_to_list = texts.split('j') #. the second number is optional for max split
# print(strig_to_list)

######################################   JOIN         #######################################

# عكس السبليت تخلي الليست الى نص diconaty or tuple
#
# listy_to_string= ' '.join(strig_to_list)
# print(listy_to_string)

##############################  isalnum  CHECK  ########################################

# values= 'A79A8'
#
#
#
# print(values.isalnum())
# print(values.isdigit())
# print(values.isalpha())
# print(values.isupper())
# print(values.islower())
# print(values.isupper())
# print(values.isspace())
#
# #################################       REPLACE           ############################################
#
# print(values.replace('A' ,'4')) # doesnt change the real virable only at the moment printing
# print(values)

# Like this to save a new variable with the replacemrnt

# new_values= values.replace('A','4', 1) # tha last number is for count how many times do you want to change the caracter that you choose not number of index (OPTIONAL)
# print(new_values)
#
# #################            STRIP       ################################################################
#
# testext= '                 MESHAL IS THE GOAT             '
# print(testext.strip()) # remove the unneccery spaces
#
# print(testext.lstrip()) # get rid of first spaces
# print(testext.rstrip())  # get rid of last spaces

##########################       Upper Lower    ##############################################################

# str = 'this is Python Course By Meshal'
# print(str.upper()) # convert the srting to UPPERCASE
# print(str.capitalize()) # convert the First letter to UPPERCASE (maybe)
# print(str.lower()) # convert the srting to LOWERCASE
# print(str.swapcase()) # swaping (:
# print(str.title())  #   convert the First letter of each word  to UPPERCASE

##########################          RAW STRING                ######################################################

# str2 = r'\t Python\nMeshal' # just type r before the text quetianos it will print the string raw
# print(str2)

##########################             FORMAT                      ###################################################

# first_n= 'Meshal'
# Last_n= "Alsaedi"
# age = 21
# print('My name is  {} {}, and I am {} years old.'.format(first_n, Last_n, age) )
#
# print('My name is  {2} {0}, and I am {1} years old.'.format(first_n, Last_n, age) ) # by index number formating
#
# print('My name is  {first} {last}, and I am {AGE} years old.'.format(first=first_n, last=Last_n, AGE=age) )
#


###############################                                                    ################################
#####################################             ADVANCED Lists             ####################################
###############################                                                    ################################


####################################################              2D Lists                #################################
# Values = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]            # Lists Inside list
# print(Values[0])
# print(Values[0][2], Values[2][1])


##############################                                 FILTER                               #################################################
ages = [30,9,15,22,17,44,26,5]

# NOOP lvl1
# def Under_age (ages):
#     Kids= []
#     for age in ages:
#         if age < 18:
#             Kids.append(age)
#
#
#     return Kids
#
# print(Under_age(ages))

#PRO lvl MAX
# def filterd_ages (age):  # age is new variable
#     return age < 18
# print(list(filter(filterd_ages, ages))) # we use list function because filter returns only object

##############################                                 MAP                               #################################################

# #NOOP lvl 1
# def pow_ages(ages):
#     new_ages=[]
#     for age in ages:
#         new_ages.append(pow(age,2))
#     return new_ages
#
#
# print(pow_ages(ages))
#
# # PRO lvl MAX
# def square(num):
#     return pow(num,2)
#
# print(list(map(square, ages)))

##############################                                 SORT                               #################################################

# list_one = [4,67,1,23,4]
# list_two=['Meshal', 'Nawaf', 'Abdullah']
# list_one.sort()
# list_two.sort()
# print(list_one)
# print(list_two)
#
# list_one.sort(reverse=True)
# list_two.sort(reverse=True)
# print(list_one)
# print(list_two)

##############################                                 Reverse LISTS                               #################################################
# list_one = ['Meshal' , 'Nawaf' , "Abdullah", "ahmad"]
# list_one.reverse()
# print(list_one)


##############################                                 List comprehension                               #################################################
# list_one = [1,2,3,4]
#
# #NOOP lvl 1
# doubled_list= []
# for num in list_one:
#     doubled_list.append(num*2)
#
# print(doubled_list)

#PRO lvl MAX
# doubled_list= [num*2 for num in list_one]
# print(doubled_list)

# same but i want to add if
# doubled_list_if= [num*2 for num in list_one if num <=3]
# print(doubled_list_if)
#


###############################                                                    ################################
#####################################             ADVANCED Functions             ####################################
###############################                                                    ################################


##############################                                 Positional Arguments                               #################################################


# def info (name,age):
#     print('My name is ' , name , 'and I am ' , age , ' years old.')
#
# info('Meshal',22)


##############################                                 Keyword Arguments                               #################################################


# def info (name,age):
#     print('My name is ' , name , 'and I am ' , age , ' years old.')
#
# info(name='Abdullah',age=22) # order isnt imporntant because we used keywords



##############################                                 Default Parameter                               #################################################


# def info (name='Nawaf',age=30):
#     print('My name is ' , name , 'and I am ' , age , ' years old.')
#
# info(name='Meshal')
# info(age=1)
# info()

##############################                                 Arguments Packing                               #################################################

# def mean (*funcs) : # tuple argument
#
#     total = sum(funcs)
#     mean_1 = total / len(funcs)
#     print(mean_1)
#
# mean(4,5,6,7,43,34,5,5)

##############################                                 Arguments Unpacking                               #################################################
#
#
# def indo(name1,name2,name3) :
#     print('My name is', name1)
#     print('My friend\'s name is', name2)
#     print('My friend\'s name is', name3)
#
# names = 'Meshal', 'Nawaf','Abdullah'
# indo(names[0],names[1],names[2])
# indo(*names) # same as above

##############################                                 Unpacking and Packing                               #################################################

# def func (*items) :
#     print(items)
#
# items = ['a', 'b', 'c']
#
# # compare the two callings
# func(items)
# func(*items)

##############################                                 Dictionary  Packing                               #################################################

# def info(**kwargs): # Dictionary
#     print(kwargs)
#     print(type(kwargs))
#     print('My name is ' , kwargs['name'])
#
# info(name='Ali', age=21)

##############################                                 Dictionary  UnPacking                               #################################################

# def info(name,age) :
#     print("Hello " , name , "! You are " , age , " years old.")
#
# d={'name':'Meshal' ,'age':22}
# info(**d)

##############################                                PROJECT                               #################################################

## Read this
#
# بنهاية هذا المشروع سيكون الطالب قادرًا على:
# التعامل مع التواريخ Dates.
# التعامل مع الأرقام Numbers.
# التعامل مع أنواع البيانات المتقدمة Sequence والدوال الخاصة بها.
# التعامل مع الدوال بشكل أعمق.


# المتطلبات Requirements
# قم ببناء برنامج يقوم باستقبال عدد لا محدود من أسماء الأشخاص مع أعمارهم.
# يقوم البرنامج بحساب العُمر
# ، بحيث يقوم باستقبال التاريخ، ويعود لنا بالعُمر الحالي، كذلك
# اسم اليوم الذي وُلد فيه. يقوم البرنامج أيضًا بطباعة عمر أكبر شخص
# وأصغر شخص، ومجموع الأشخاص الذين
# تم تمريرهم. في حال تم تمرير شخص واحد فقط، لا يتم حساب أكبر وأصغر شخص، ويتم طباعة
# العبارة There is no oldest or youngest person. يتم أيضًا التأكد من قيمة
# التاريخ، أي أن قيمة السنة، الشهر واليوم يجب أن تكون
# قيم صحيحة (مثال: قيمة الشهر 14 غير صحيحة)، وأيضاً
# لا تحتوي على رموز أو قيم سالبة، وفي حال ذلك يتم
# إرجاع الرسالة Invalid date، مصحوبًا
# باسم الشخص ذو التاريخ الخاطئ.


# مثال:
# المُدخلات
#
# khalid, 1-2-1989
# Nouf, 2-9-2004
# Ali, 9-12-2009
#
#
# المُخرجات المتوقعة
#
# Khalid is 31 years old and she/he was born on Saturday
# Nouf is 16 years old and she/he was born on Thursday
# Ali is 11 years old and she/he was born on Wednesday
# The oldest one is Khalid
# The youngest one is Ali
# Total People: 3


# ملاحظة
#
# المخرجات أعلاه تم حسابها بناءً على التاريخ 2021-1-1
# التاريخ أعلاه يتبع النظام dd-mm-yyyy
#
# def input_func():
#     import datetime
#     current_year = datetime.datetime.now().year
#
#     num_people = int(input("How many people do you want to enter? "))
#
#     people = []
#
#     for i in range(num_people):
#         print("\n --- Person", i + 1, "---")
#         name = input("Enter your name: ")
#
#         print("Enter your date of birth:")
#         while True:
#             year = int(input("Year: "))
#             if 1900 <= year <= current_year:
#                 break
#             else:
#                 print(f"Invalid year! Please enter between 1900 and {current_year}.")
#
#         while True:
#             month = int(input("Month: "))
#             if 1 <= month <= 12:
#                 break
#             else:
#                 print("Invalid month! Please enter between 1 and 12.")
#
#         while True:
#             day = int(input("Day: "))
#             if 1 <= day <= 31:
#                 break
#             else:
#                 print("Invalid day! Please enter between 1 and 31.")
#
#
#         dob = datetime.date(year, month, day) # نخزن التاريخ في datetype
#
#         day_name = dob.strftime("%A")  # اسم اليوم
#
#         today = datetime.date.today()
#         age = today.year - dob.year
#         if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
#             age -= 1
#
#
#
#         person = {"name": name, "year": year, "month": month, "day": day, "day_name": day_name , "age": age ,"dob": dob}
#         people.append(person)
#
#
#     print("\n--- People Entered ---")
#     for p in people:
#         print(f"{p['name']} is {p['age']} years old and was born on {p['day_name']}")
#
#     oldest = people[0]
#     youngest = people[0]
#
#     for p in people:
#         if p["dob"] < oldest["dob"]:
#             oldest = p
#         if p["dob"] > youngest["dob"]:
#             youngest = p
#
#     print("\n--- Summary ---")
#     print("The oldest one is", oldest["name"])
#     print("The youngest one is", youngest["name"])
#     print("Total People:", len(people))
#
# input_func()

##################################################                FINISH                                                    ##################################################################################################################################################################################