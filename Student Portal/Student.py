from LL import *
from que import *
from Home import *
class Student:
    def attendenceCheck(self):
        rollno=int(input("Enter Your Roll No : "))
        if self.stu.search(rollno):
            print("Above Is Your Search Result")
        else:
            print("No Record Is Found")

    def __init__(self,stu,qued,Home):
        self.stu = stu
        self.qued = qued
        self.Home= Home
        self.move=None
        condition = True
        while(condition):
            print("\n\t\t\t\t\t\t\t____------Welcome To Student Portal------____\n")
            num = int(input("Press 1 To See Assignments \nPress 2 To See Your Performance \nPress 3 To Exit Student Portal ")) 
            if num == 1:
                self.qued.queueDisplay()
                
            elif num == 2:
                self.attendenceCheck()
            elif num == 3:
                self.move="back"
                condition=False
                break
            else:
                print("Invalid Entry \n")
        if (self.move == "back"):
            self.Home(self.stu,self.qued)