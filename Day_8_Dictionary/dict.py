#Dictionary is a collection of key-value pair
# a = {}
# b = dict()

# print(type(a))
# print(type(a))

#dictionary is heterogeneous and mutable
# student_grade = {'ram': 25, 'shyam': 50}  # order does not matter here, meaning indexing of pair does not matter.
# print(len(student_grade))

#acess value
# print(student_grade['ram'])
# print(student_grade['shyam'])

# student_grade['ram'] = 100  #this changes value of ram  
# student_grade['rama'] = 100     #this creates a new pair of rama, having the value 100

# student_grade = {'ram': 25, 'shyam': 50, 'hari': 20, 'shyam':100} #key are unique, so shyam's value gets replaced ; shyam = 100
# print(student_grade)
# print(len(student_grade))

# print('shyam' in student_grade)
# print('shyama' in student_grade)

# print(student_grade.keys())
# print(student_grade.values())

# print(student_grade.items())

# student_grade = {'ram': 25, 'shyam': 50, 'hari': 20, 'shyam':100}
# del student_grade['shyam']
# print(student_grade)

# student_grade.clear()
# print(student_grade)

# info = {'name': 'umesh', 'age': 24, 'address': {'city': 'balaju', 'district': 'kathmandu'}}

# print(info['name'])
# print(info['age'])
# print(info['address']['city'])
# print(info['address']['district'])

# ram 25, shyam 35, hari 80, rita 65

# student_grade = {'ram': 25, 'shyam': 35, 'hari': 80, 'rita': 65}
# name = input('Enter your name - ').lower()
# print(f'Hi, {name.capitalize()} your grade is {student_grade[name]}.')
