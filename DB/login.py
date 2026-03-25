# // Source - https://stackoverflow.com/a/65366184
# // Posted by furas, modified by community. See post 'Timeline' for change history
# // Retrieved 2026-03-18, License - CC BY-SA 4.0

import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

def menu(): 
    print("1- Register")
    print("2- login")
    print ("3- Quit")
    
def create_table():
    query = "DROP TABLE IF EXISTS login"
    cursor.execute(query)
    conn.commit()
    
    query = "CREATE TABLE login(Username VARCHAR UNIQUE, Password VARCHAR)"
    cursor.execute(query)
    conn.commit()

def enter(username, password):
    query = "INSERT INTO login (Username, Password) VALUES (?, ?)"
    cursor.execute(query, (username, password))
    conn.commit()

def check(username, password):
    query = 'SELECT * FROM login WHERE Username = ? AND Password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    # print('[DEBUG][check] result:', result)
    return result

def login():
    # answer = input("Login (Y/N): ")

    # if answer.lower() == "y":
        username = input("Username: ")
        password = input("Password: ")
        if check(username, password):
            print("Username correct!")
            print("Password correct!")
            print("Logging in...")
            get_student_credits("school.db")
        else:
            print("Something wrong")

def get_student_credits(student_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    
    query = """
    SELECT Student.name, Credits.credits, Credits.grade, Credits.date, Course.name
    FROM Student
    INNER JOIN Credits ON Credits.id_student = Student.id
    INNER JOIN Course ON Course.id = Credits.id_course
    WHERE Student.id = ?;
"""
    
    
    cursor.execute(query, [student_id])
    rows = cursor.fetchall()
    
    conn.close()
    return rows
# --- main ---


def main() -> None:
    while True:
        menu()
        choice = input("Insert option: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Value must be an integer.")

        if(choice == 1):
            create_table()
            Username = input("Create username: ")
            Password = input("Create password: ")
            enter(Username, Password)
            #check(Username, Password)

        elif(choice == 2):
            login()
            results = get_student_credits(1)

            if results : 
                print("Student credits: ")
                for name, credits, grade, date, course in results: 
                    print (f" {name}: {course}, {credits} credits, grade {grade}, date {date}")
                else: 
                    print("Not found")
            cursor.close()
            conn.close()
            
        elif (choice == 3):
            break
        
        else:
            print("Unknown option. Try again!")

if __name__ == "__main__":
    main()


