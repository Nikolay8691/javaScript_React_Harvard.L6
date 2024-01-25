import ctypes

from pprint import pprint

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ANSI colors
c = (
    "\033[0m",   # End of color-0
    "\033[36m",  # Cyan-1
    "\033[91m",  # Red-2
    "\033[35m",  # Magenta-3
    "\033[33m",  # Yellow-4
    "\033[32m",  # Green-5
    "\033[34m",  # Blue-6
)

print(c[1] + '\n hello! colors come from module 7 level 1,' + c[5] + ' tervetuloa hyvät ystävät! \n'+ c[0])

s = input(c[2] + '\n hello, what is your name? '+ c[0])

print(c[3] + '------ it is nice to see you,' + c[2] + f' {s.capitalize()}! ' + c[4] + '------ welcome to L6_projects! '+ c[0])
print(c[6] + ' see you soon! '+ c[0])
# print(c[6] + ' goodbye! '+ c[0])

student_01 = {'name' : 'ivan', 'age' : 21}
student_02 = {'name' : 'nikolay', 'age' : 54}
student_03 = {'name' : 'den', 'age' : 25}

people = [student_01, student_02, student_03]
print('\n list of dictionaries :')
pprint(people)
print()

print(student_01)
print(student_02)
print(student_03)
print()

def plus_string(f):
    def wrapper(*args, **kwargs):
        print(c[6] + 'decorator function at work!'+ c[0])
        return f(*args, **kwargs)
    return wrapper

@plus_string
def f(person):
    return person['age']

def f1(person):
    print(c[5] + 'simple function at work!'+ c[0])
    return person['name']

print(f(student_01))
print(f(student_02))
print(f(student_03))

print(f1(student_01))
print(f1(student_02))
print(f1(student_03))

# print(people)
people.sort(key=f)
pprint(people)

print()

people.sort(key=f1)
pprint(people)

print('\n lambda function at work!')
people.sort(key = lambda student: student['name'])
pprint(people)