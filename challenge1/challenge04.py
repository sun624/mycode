#!usr/bin/env python3

str="* "
for i in range(1,6):
    print(i*str)
for i in range(4,0,-1):
    print(i*str)


str="* "
lst = list(range(1,6))+list(range(4,0,-1))
for i in lst:
    print(i*str)

for i in [*range(1,6),*range(4,0,-1)]:
    print(i*str)

