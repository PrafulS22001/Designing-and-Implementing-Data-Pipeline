'''
Use class-lvl attributes (root of the class) only for values that are the same for every object.

exampple: 
- Number of wheels on a car
- Pi constant
- Configuration shared by all instances 
- Version number
'''

class Cars:
    Wheels = 4 #same for all cars as a default.

'''
These attributes live on the class, not the object.

Use constructor (__init__) for instance specific data. They are unique per object.

Examples: 
- Car color
- Max speed of the car
- Cureent speed 
- registration number
'''

class Car: 
    Wheels = 4 #Shared by default by all cars.
    
    def __init__(self, color, max_speed): 
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0
'''
Every time you create a new object, constructor (__init__) runs and gives thawt specific object it's own attributes.

Why not put ibject specific attributes in the root? Because attributes in the root are shared unless over written.

For example:  
'''


class Person: 
    hobbies = [] # shared list
    
p1 = Person()
p2 = Person()

p1.hobbies.append("Football")
p1.hobbies.append("Reading")
p2.hobbies.append("Making music")
print(p2.hobbies)

'''
If the list was inside __init__, each would get its own list.
'''

class Student: 
    def __init__(self):
        self.hobbies = [] # shared list
    
s1 = Student()
s2 = Student()

s1.hobbies.append("Football")
s1.hobbies.append("Walking")
s2.hobbies.append("Reading")
print(s2.hobbies)