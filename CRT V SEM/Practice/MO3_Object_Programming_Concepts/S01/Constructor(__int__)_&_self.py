#Count no.of objects of a class created
import math


class A:
    count = 0
    def __init__(self):
        A.count += 1
a = A()
b = A()
c = A()
print("No. of objects created:", A.count)


...
