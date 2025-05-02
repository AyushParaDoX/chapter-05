#Q1: make a student dictionary in which the give details should be mentioned:
# Name :Ayush
# Age :14
# class: 9B

student = {
    "Name":"Ayush",
    "Age":14,
    "class":"9B"
} 
print(student)
# Adding hobby in the dict
student["hobby"] = "coding"
print(student)
# updating the age of student from 14 to 15 
student['Age'] = 15
print(student)

#sets question
# make a set of values 1,2,3,4,4
my_set = {1,2,3,4,4}
print(my_set)
print(type(my_set))
# add 5 in set
my_set.add(5) 
print(my_set)
# remove 2 from the set
my_set.remove(2)
print(my_set)
# check is there 3 in the set.
if 3 in my_set:
 print("Yes")
