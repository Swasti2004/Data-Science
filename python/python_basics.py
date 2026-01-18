# learning from corey schafer youtube channel
#textual data
# my_string = "Hello World"
# print(my_string)
# # single quote and double quote
# # also string slicing
# print(my_string[0])  # H
# print(my_string[2:5])  # llo
# print(my_string.lower())  # hello world
# print(my_string.upper())  # HELLO WORLD
# print(my_string.count("l"))  # 3
# print(my_string.find("o"))  # 4
# newmessage = my_string.replace("World", "Universe")
# print(my_string )
# print(newmessage)
# # concatenation
# greeting = "Hello"
# name = "Corey"
# message = greeting + ", " + name + ". Welcome!"
# print(message)
# message="{}, {}. Welcome!".format(greeting, name)
# print(message)
# message=f"{greeting}, {name}. Welcome!"
# print(message)
# # dir() and help()
# print(dir(my_string))
# print(help(str))

# integers and floats

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# lists

# courses = ["History", "Math", "Physics", "CompSci"]
# print(courses)
# print(courses[0])  # History
# print(courses[1:3])  # ['Math', 'Physics']
# courses.append("Art")
# print(courses)  # ['History', 'Math', 'Physics', 'CompSci', 'Art']
# courses.insert(0, "Biology")
# print(courses)  # ['Biology', 'History', 'Math', 'Physics', 'CompSci', 'Art']
# # extend and append difference
# more_courses = ["Education", "Economics"]
# courses.extend(more_courses)
# print(courses)  # ['Biology', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education', 'Economics']
# courses.append(more_courses)
# print(courses)  # ['Biology', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education', 'Economics', ['Education', 'Economics']]
# courses.remove("Math")
# print(courses)  # ['Biology', 'History', 'Physics', 'CompSci', 'Art', 'Education', 'Economics', ['Education', 'Economics']]
# courses.pop()
# print(courses)  # ['Biology', 'History', 'Physics', 'CompSci', 'Art', 'Education', 'Economics']
# courses.reverse()
# print(courses)  # ['Economics', 'Education', 'Art', 'CompSci', 'Physics', 'History', 'Biology']
# courses.sort()
# print(courses)  # ['Art', 'Biology', 'CompSci', 'Economics', 'Education', 'History', 'Physics']
# print(sorted(courses))  # ['Art', 'Biology', 'CompSci', 'Economics', 'Education', 'History', 'Physics']
# print(courses.sort(reverse=True))
# # ['Physics', 'History', 'Education', 'Economics', 'CompSci', 'Biology', 'Art']
# # difference between sort and sorted is sort method modifies the list in place and returns None
# # sorted function returns a new sorted list and leaves the original list unchanged
# print(min(courses))  # Art
# print(max(courses))  # Physics
# print(courses.index("CompSci"))  # 4
# print("Math" in courses)  # False
# for course in courses:
#     print(course)
    
# for course in enumerate(courses):
#     print(course)

# for index, course in enumerate(courses, start=1):
#     print(index, course)
    
# course_str = " - ".join(courses)
# print(course_str)  # Economics - Education - Art - CompSci - Physics - History - Biology
# new_list = course_str.split(" - ")
# print(new_list)  # ['Economics', 'Education', 'Art', 'CompSci

# tuples
# tuple is immutable
# example of mutablity
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2=list_1

# print(list_1)
# print(list_2)

# list_1[0]='Art'

# print(list_1)
# print(list_2)
# and immutability
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1   
# print(tuple_1)
# print(tuple_2)  
# # tuple_1[0] = 'Art'  # This will raise a TypeError
# print(tuple_1)
# print(tuple_2)

# # sets
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}
# print(cs_courses)
# print('Math' in cs_courses)  # True
# print(cs_courses.intersection(art_courses))  # {'History', 'Math'}
# print(cs_courses.difference(art_courses))  # {'Physics', 'CompSci'}
# print(cs_courses.union(art_courses))  # {'History', 'Math', 'Physics', 'CompSci', 'Art', 'Design'}


# empty_list = []
# empty_list = list()
# empty_tuple = ()
# empty_tuple = tuple()
# empty_set = set()
# empty_set = {}  # This creates an empty dictionary, not a set


# dicionary
student={'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])  # John
print(student['courses'])  # ['Math', 'CompSci']
print(student.get('age'))  # 25
# default get value
print(student.get('phone', 'Not Found'))  # Not Found
# update dictionary
student['age'] = 26
student.update({'name': 'Jane', 'phone': '555-5555'})
print(student)  # {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
# delete
del student['age']
print(student)  # {'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
age = student.pop('age', 'Not Found')
print(age)  # Not Found
print(student)  # {'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
print(len(student))  # 3
print(student.keys())  # dict_keys(['name', 'courses', 'phone'])
print(student.values())  # dict_values(['Jane', ['Math', 'CompSci'], '555-5555'])
print(student.items())  # dict_items([('name', 'Jane'), ('courses', ['Math', 'CompSci']), ('phone', '555-5555')])

# loop through dictionary
for key, value in student.items():
    print(key, value)
