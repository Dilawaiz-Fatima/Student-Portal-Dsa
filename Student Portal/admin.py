from Home import*
from LL import *
from que import*
class admin:
    def insertStudent(self):
        print("Enter student info : ")
        name= str(input("Student Name : "))
        fname = str(input("Father Name : "))
        rollno = int(input("Roll No. : "))
        cgpa= float(input("Enter GPA : "))
        at= input(str("Enter Current Attendance : "))
        pasword= input(str("Enter Password : "))
        gots = students(name,fname,rollno,cgpa,at,pasword)
        self.lis.insert(gots)

    def insertHomework(self):
        
        ev=str(input("Enter Event or Assigment : "))
        dat = str(input("Enter Deadline : "))
        createdevent = Events(ev,dat)
        self.qued.queueEnqueue(createdevent)
        print("Event Created")

    def deleteStudent(self,lis):
        
        if self.lis.isEmpty():
            print("No Student to delete")
        else:
            print("Press (1) to remove by name or (2) to remove by roll no : ")
            typ = int(input("Press KEY : "))
            if typ == 1:
                name = str(input("Enter Name : "))
                self.lis.deleteNode(name)
            elif typ == 2: 
                rollno = int(input("Enter Roll No. : "))
                self.lis.deleteNoded(rollno)
            else:
                print("Invalid Entry")

    def updateStudent(self):
        if self.lis.isEmpty():
            print("No Student to update")
        else:
            print("Press (1) to update CGPA or (2) to update ATTENDANCE : ")
            typ = int(input("Press KEY : "))
            if typ == 1:
                roll =int(input("Enter Roll No. : "))
                val = float(input("Enter new CGPA : "))
                self.lis.updateNode(roll,val)
            elif typ == 2:
                roll = int(input("Enter Roll No. : "))
                val = str(input("Enter New Attendance : "))
                self.lis.attendenceupdate(roll,val)
            else:
                print("Invalid Entry")

    def __init__(self,lis,qued,Home):
        self.lis = lis
        self.qued = qued
        self.move = None
        self.Home = Home
        condition =True
        while (condition):
            print("\n\t\t\t\t\t\t\t____------Welcome To Admin Panel------____\n")
            num=int(input("Press (1) To Add Student \nPress (2) To See All Students\nPress (3) To Remove Student \nPress (4) To insert Event or Assignment \nPress (5) To see all Events and Assigmnents \nPress (6) To delete event \nPress (7) To update Student Information \nPress (8) To Exit Admin Panel "))
            if num == 1:
                self.insertStudent()
            elif num == 2:
                lis.traverse()
            elif num == 3:
                self.deleteStudent(lis)
            elif num == 8:
                self.move="back"
                condition=False
            elif num == 4:
                self.insertHomework()
            elif num == 5:
                print("The Current Activies are : ")
                self.qued.queueDisplay()
            elif num == 6:
                print("Event Removed :")
                self.qued.queueFront()
                self.qued.queueDequeue()
            elif num == 7:
                self.updateStudent()
                print(" Updated ")
            else:
                print("Invalid Entry \n")

        if (self.move=="back"):
            condition = False
            self.Home(self.lis,self.qued)
