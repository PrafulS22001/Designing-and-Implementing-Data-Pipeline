## Basics for this semester 
---
- Small practice project for a company; just to get the hang of it. 
- Doing a full IOT pipeline. 
- Follow Mira's lead. 
- *Electric vehicles- Juha and Tommi collaboration for next semester*
- User interfaces with python and project React 
- SQL databases. 
---
## How to get things done in this sem. 
- Makes notes and save into GitHub.
- Make one GitHub Repo for projects and tasks and make a good ReadMe file.
		- ReadMe should have the info about the which folder is what. 
		- Explain more; *"More is More"* - Mira
		- Use Main Branch to save the answers to the task.
- We'll have a small practice project with Rakkaranta. (Holiday cabin app )
- All tasks in GitHub. 
- Test in Exam Room. 
- This course has grades from 1 to 5. Mainly from Test and GitHub tasks(pass or fail).
- Can skip 2 lessons this semester without consequences. After which one missed class equals to 0.5 credits reduction (Doctor's certificate in case of heavy sickness.)
- Study group for this semester we can choose teams , for company projects; Mira chooses the team. 
- From next year, we choose the project ourselves. 
- **Only return the code that you understand !!**
	- This is because if you don't understand the simple code in the beginning, you can't debug it or add any function inside it if you don't understand the basics. 
	- Using AI is okay if you use it to understand the prompt and don't cheat off to just complete the given task. 
	- DON'T USE AI JUST TO GET THE JOB DONE!!
	- *You are to do the code again if it is found to be done by AI.* 
- We will practice presentation. i.e. Review after the completion of a project. 
- Use comments to understand your code. 

___
### Assessment And Grading instructions

Exam performance
All formal assessments are graded on a scale from 0 to 5.
The grade is based on the knowledge demonstrated in exams and assessed tasks.
<h1>Attendance is mandatory. </h1>
- Up to 2 absences are allowed without documentation.
- After 2 absences, additional absences must be justified with a doctor’s certificate.
- If you exceed the allowed absences without a doctor’s certificate, each additional skipped class will reduce your final course grade by 0.5
- If you skip a test, or an assessed class activity, you will receive 0 points for that task.

Classroom performance
Your classroom performance can adjust your total score by –2 to +2 points, based on:

**Positive (+) indicators**
- Active participation in discussions
- Engagement in study groups
- Demonstrated learning in homework and class
- Good preparation and consistency

**Negative (–) indicators**
- Low participation
- Incomplete homework
- Poor preparation
- Repeated disengagement

These points are added to or subtracted from your final score.

**Your final grade consists of:**
- Formal exams and assessed tasks
- Classroom performance score (–2 to +2)
- Attendance compliance (extra undocumented absences = –0.5 per class)

<font color = "red">All requirements must be completed to receive a final grade.</font>
___
## Company project insight

- **LAB university attendance program**
- Tinder looking app for jobs in local area 
- Construction company project i.e. create a 3D model for projects (peikkodesigner.com) C sharp, python and DevOps
- media streaming service projects
- 
___

# OOP Week 1 
- make a folder to just file handling 
- another folder that reads csv file to read data and make it into object 
- we modify the content of the object and print it 
- we change the object into data and save the progress and data into a csv file.
#### Underscore Naming 
- 2 underscore means it's private and is recommended to not be changed and not accessible maybe ( ``self.__x)
- 1 underscore is just a naming convention .(``self._x)
--- 
## Homework Review
- If someone in the group has any problem then have a meeting 
- if no problem and you don't need to have a meeting; DON'T HAVE A MEETING FOR THE SAKE OF HAVING A MEETING. 
___
### Things to keep in mind while coding 
1) do docstrings for your methods/function
2) Header comments 
___

# OOP Week 2
## **4 Pillars**
- Inheritance 
- Abstraction 
- Polymorphism 
- Encapsultion

--- 
### Development example - Car 
- A program needs "Car" object with following properties and methods: 

- Properties (Things that object has to have)
    - Position 
    - Seats
    - EngineOn status

- Methods (Function the object has to follow)
    - A way to accelerate 
    - A way to steer
---
### Development example - Moto
- The development stage requires adding "Motorcycle" objects

- Properties: 
    - Position 
    - Seats
    - EngineOn status

- Methods: 
    - A way to accelerate
    - A way to steer
--- 
### The similarities in the two
They both have similarities since they both are vehicle. However, they have their differences. 
In their case, there are different times/cases where reusing existing classes will be very handy.

---
1.  **OOP - Inheritance**
    - **Purpose** : reusing existing code
    - Reusing class is generic
    - By inheriting some class, the subclass gets: 
        - Properties and methods from the super class that are "public" or "protected"

2. **OOP - Abstraction**
    - **Purpose** : Using the blueprint to build other classes
    - For example:
        - Animal is an abstract class since it is broad and it can't be described in real world. It way too broad. 
        - Cat is a concrete class since it can be described and is narrowed. 
    - 