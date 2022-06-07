from admin import*
from Student import Student
from LL import *
from que import *

class Home:
    def __init__(self, studentinfo, qued):
        self.oto = None
        condition =True
        while (condition):
            print("\n\t\t\t\t\t\t\t=========____STUDENT PORTAL____=========\n")
            num=int(input("Press 1 to Enter Admin Panel \nPress 2 To Enter Student Portal \nPress 3 to EXIT "))
            if num == 1:
                self.oto="admin"
                condition=False
            elif num == 2:
                self.oto="student"
                condition=False
            elif num == 3:
                condition = False
            else:
                print("Invalid Entry \n")
        if (self.oto == "admin"):
            admin(studentinfo,qued,Home)
        elif (self.oto == "student"):
            Student(studentinfo,qued,Home)
        else:
            print("=++= GOOD BYE! =++=")



def main():
    studentinfo = LL()
    q = que(5)
    Home(studentinfo,q)

if __name__ == "__main__":
    main()