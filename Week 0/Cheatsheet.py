'''
Store Personal information 
Define each person with data: 
    first name 
    last name
    age 
    occupation
Create a new person called Matti and assign personal details 
'''
class person:
    # def __init__(self, First_name, Last_name, Age, Occupation):
    #     self.First_name = ""
    #     self.Last_name = ""
    #     self.Age = 0
    #     self.Occupation = ""
    First_name = ""
    Last_name = ""
    Age = 0
    Occupation = ""
    
    def introduction(self): 
        return f"{self.First_name}, {self.Last_name}, {self.Age}, {self.Occupation}"

def main() -> None: 
    # Matti = person("Matti", "Suomalainen", 85, "Stripper")
    Matti = person()
    Matti.First_name = "Matti"
    Matti.Last_name = "Suomalainen"
    Matti.Age = 85
    Matti.Occupation = "Teacher"
    print(Matti.introduction())
    return

if __name__ == "__main__": 
    main()

# class person:

    
#     def introduction(self): 
#         return f"{self.First_name}, {self.Last_name}, {self.Age}, {self.Occupation}"

# def main() -> None: 

#     print(Matti.introduction())
#     return

# if __name__ == "__main__": 
#     main()