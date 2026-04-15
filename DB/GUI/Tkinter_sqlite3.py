from tkinter import *
import sqlite3

root = Tk()
root.title ("Tietokanta")
root.geometry("400x400")

conn = sqlite3.connect("tasklist.db")

c = conn.cursor()

c.execute ("DROP TABLE IF EXISTS tasks")

sql = '''CREATE TABLE tasks (
    task VARCHAR(255)
)'''

c.execute(sql)

conn.commit()

conn.close()

root.mainloop