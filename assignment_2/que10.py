from collections import namedtuple
from collections import OrderedDict
student = namedtuple('student', 'first_name last_name roll_number')
p1 = student('shyam', 'koju', '722')
print(p1.first_name)
print(p1.last_name)


print("Before deleting:\n")
dict= OrderedDict()
dict['a'] = 1
dict['b'] = 2
dict['c'] = 3
dict['d'] = 4

for key, value in dict.items():
    print(key, value)

print("\nAfter deleting:\n")
dict.pop('c')
for key, value in dict.items():
    print(key, value)

print("\nAfter re-inserting:\n")
dict['c'] = 3
for key, value in dict.items():
    print(key, value)