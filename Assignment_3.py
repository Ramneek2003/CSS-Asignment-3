# 1 Counting the number of occurences of a word or character in a string
input_string = str(input(" 1 Enter a string: "))
split_words=input_string.split()
if len(split_words)==1:            # counting occurances of each character
    for char in input_string:
        print(char,'=',input_string.count(char))
else:                        # counting occurances of each word
    for word in split_words:
        print(word,'=',split_words.count(word))

# 2 Printing the next date of the input date
day= int(input("2 Day- "))
month= int(input("Month- "))
year= int(input("Year- "))

if (year%4 == 0):
    leap_year = True
elif (year%400 == 0):
     leap_year = True
elif (year % 100 == 0):
    leap_year = False
else:
    leap_year = False

if month in (1,3,5,7,9,11):
    days = 31
elif month == 2:
    if leap_year:
        days = 29
    else:
        days = 28
else:
    days = 30                

if day < days:
    day += 1
else:
    day = 1
    month += 1
print("Next date is: %d/%d/%d"%(day,month,year))

# 3 Creating a list of tuples with first element as the number and second element as the square of the number
input_num= []
n = int(input("3 Enter the number of numbers you want the output for: "))
print("Enter the numbers: ")
for i in range(0,n):
    num= int(input())
    input_num.append(num)
print("list= ",input_num)
square=[(num,pow(num,2))for num in input_num]
print(square)

# 4 Printing the grade and performance
grade_point=float(input("4 Enter the grade point: "))
if(grade_point>=4 and grade_point<=10):
    if(grade_point==10):
        grade="A+"
        performance="Outstanding"
    elif (grade_point==9):
        grade="A"
        performance="Excellent"
    elif(grade_point==8):
        grade="B+"
        performance="Very Good"
    elif(grade_point==7):
        grade="B"
        performance="Good"
    elif(grade_point==6):
        grade="C+"
        performance="Average"
    elif(grade_point==5):
        grade="C"
        performance="Below Average"
    elif(grade_point==4):
        grade="D"
        performance="Poor"
    evaluation="Your grade is {} and {} Performance."
    print(evaluation.format(grade,performance))
else:
    print("Error. Invalid grade point entered.")


# 5 To print a pattern
alpha_str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input("5 Enter the number of rows: "))
for i in range(0,n):
    if 2*i<n :
        new_str=alpha_str[:n-2*i]
        print(" "*i,new_str) 

# 6 
data={}
std_name=input("6 Enter a student's name: ")
SID=int(input("Enter the student's SID: "))
data[SID]=std_name
print("You have entered %d value(s) till now ."%len(data))
while True:
    more_data = str(input("Do you want to add more data ?\nPlease type 'Y' for yes or 'N' for no.: "))
    if more_data in ("Y"):
        std_name=input("Enter a student's name: ")
        SID=int(input("Enter the student's SID: "))
        data[SID]=std_name
    elif more_data in ("N"):
        break

# (a)
print("(a) Students' Details")
for i in data:
    data_str="The student's name is {} and the SID is {}"
    print(data_str.format(data[i],i))

# (b)
data_2 = {}
for sorted_values in sorted(data.values()):
    for key,value in data.items():
        if value == sorted_values:
            data_2[key] = value
print("(b) Students' Details (sorted with respect to names):")
for i in data_2:
    data_str="The student's name is {} and the SID is {}"
    print(data_str.format(data_2[i],i))

# (c)
data_3 = {}
for sorted_key in sorted(data):
    for key,value in data.items():
        if key == sorted_key:
            data_3[key] = value
print("(c) Students Details (sorted with respect to SIDs):")
for i in data_3:
    data_str="The student's name is {} and the SID is {}"
    print(data_str.format(data_3[i],i))

# (d)
print("(d) ", end=" ")
while True:
    SID_search = int(input("Enter the SID to be searched: "))
    if SID_search in data:
        data_str="The student's name whose SID is {} is {}"
        print(data_str.format(SID_search,data[SID_search]))
        break
    else:
        print("The SID you entered isn't present in the record.Please enter a valid SID to be searched. \nList of valid SIDs: %s\n" % list((data.keys())))
        continue   

# 7 To print fibonacci sequence and the average of the resultant series
n=int(input("7 Enter the number of terms you want in the fibonacci series: "))
a1=0
a2=1
count=0
if n<=0:
    print("Enter a non negative integer")
elif n==1:
    print("Fibonacci sequence upto",n,":",a1)
else:
    print("Fibonacci sequence upto",n,":")
    while count<n:
        print(a1)
        an=a1+a2
        a1=a2
        a2=an
        count += 1
avg="The average of {} terms of the fibonacci series is {} "
print(avg.format(n,an/n))

# 8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

# Creating a new set of all elements that are in Set1 and Set2 but not both
new_set1=Set1-Set2
print("8 (a) ",new_set1)

# Creatin a new set of all elements that are only in one of the three sets Set1,Set2 and Set3
new_set2=(Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set1&Set3))
print("(b) ",new_set2)

# Creating a new set of elements that are exactly two of the sets Set1, Set2 and Set3
new_set3=(Set1&Set2) | (Set1&Set3) | (Set2&Set3) - (Set1&Set1&Set3)
print("(c) ",new_set3)

# Creating a set of integers ranging from 1 to 10 that are not in Set1
set={1,2,3,4,5,6,7,8,9,10}
new_set=set-Set1
print("(d) ",new_set)
#  Creating a set of integers rangin from 1 to 10 that are not in Set1,Set2 and Set3
new_set=set-(Set1|Set2|Set3)
print("(e) ",new_set)