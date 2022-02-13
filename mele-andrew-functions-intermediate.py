#QUESTION 1

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#part1
x[1][0] = 15
print(x)

#part2
students[0]['last_name'] = 'Bryant'
print(students[0])

#part3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#part4
z[0]['y'] = 30
print(z)

#QUESTION 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for name in students:
        print('first_name - ', name['first_name'],' last_name - ', name['last_name'])

iterateDictionary(students)

#QUESTION 3
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateFirstName(students):
    for name in students:
        print(name['first_name'])

iterateFirstName(students)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateLastName(students):
    for name in students:
        print(name['last_name'])

iterateLastName(students)

#QUESTION 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(len(dojo['locations']), 'LOCATIONS' '\n')
    for city in range(0, len(dojo['locations'])):
        print(dojo['locations'][city], '\n')
    print(len(dojo['instructors']), 'INSTRUCTORS' '\n')
    for name in range(0, len(dojo['instructors'])):
        print(dojo['instructors'][name], '\n')


printInfo(dojo)
