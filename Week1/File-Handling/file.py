# class Test(): 
#     def __init__(self):
#         self.x = 10
        
# t = Test()
# print (t.x)

class Test: 
    def __init__(self):
        self.__x = 10
        
t = Test()
#print(t.__x) this doesn't work

print(t._Test__x)