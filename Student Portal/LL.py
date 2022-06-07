class students:
    def __init__(self, name, fname, rol, cg, at, password):
        self.credintal = [None for _ in range(2)]
        self.studentName = name
        self.studentfatherName =fname
        self.rollno=rol
        self.cgpa=cg
        self.attendence =at
        self.credintal[0]=rol
        self.credintal[1]=password
class Node:
    def __init__(self,outerInstance, data):
        self.next = None
        self.outerInstance = outerInstance
        self.data = data
        
    def getData(self):
        return " Name : "+self.data.studentName+"\n Father Name:"+self.data.studentfatherName+"\n Roll No:"+str(self.data.rollno)+"\n CGPA:"+str(self.data.cgpa)+"\n Attendence:"+self.data.attendence
    def setData(self,rol):
        self.data.rollno =rol
    def setData2(self,attendence):
        self.data.attendence = attendence
    def setData3(self, gpa):
        self.data.cgpa=gpa
    def setdata4(self, password):
        self.data.credintal[1]=password

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

   
    def traverse(self):
        element =self.head
        if (element == None):
            print("No Student Inserted")
        else:
            while (element != None):
                print(element.getData()+"\n")
                element=element.next
    
    def isEmpty(self):
        if (self.head != None):
            return False
        return True
    
    def insert(self, data):
        a = Node(self, data)
        if self.head == None and self.tail == None:
            self.head=a
        else:
            self.tail.next =a
        self.tail=a
    
    def deleteNoded(self, rollno):
        # Store head node
        element = self.head
        prevelement = None
        # If head node itself holds the key to be deleted
        if element is not None and element.data.rollno == rollno:
            print("Student Removed : ")
            print(element.getData())
            self.head = element.next
            element=None
            return # Changed head
        # Search for the key to be deleted
        while element != None and element.data.rollno != rollno:
            prevelement = element
            element = element.next
        # If roll no was not present in linked list
        if element == None:
            print("No Such Roll No")
            return
        print("Student Remove : ")
        print(element.getData())
        # Unlink the node from linked list
        prevelement.next = element.next
    
    
    def deleteNode(self, name):
        # Store head node
        element = self.head
        prevelement = None
        # If head node itself holds the key to be deleted
        if element is not None and element.data.studentName == name:
            print("Student removed : ")
            print(element.getData())
            self.head = element.next
            return # Changed head
        # Search for the key to be deleted
        while element != None and element.data.studentName != name:
            prevelement = element
            element = element.next
        # If name was not present in linked list
        if element == None:
            print("No such name")
            return
        print("Student remove : ")
        print(element.getData())
        # Unlink the node from linked list
        prevelement.next = element.next
        
       
    def updateNode(self, rollno, cgpa):
        # Store head node
        element = self.head
        prevelement = None
        # If head node itself holds the key to be deleted
        if element is not None and element.data.rollno == rollno:
            print("Student Update : ")
            element.setData3(cgpa)
            print(element.getData())
            return # Changed head
        # Search for the key to be deleted
        while element is not None and element.data.rollno != rollno:
            prevelement = element
            element = element.next
        # If roll no was not present in linked list
        if element==None:
            print("No such Roll No")
            return
        print("Student Update : ")
        element.setData3(cgpa)
        print(element.getData())
        
        
    def attendenceupdate(self,rollno,attendence):
        # Store head node
        element = self.head
        prevelement = None
        # If head node itself holds the key to be deleted
        if element is not None and element.data.rollno == rollno:
            print("Student Update : ")
            element.setData2(str(attendence))
            print(element.getData())
            return # Changed head
        # Search for the key to be deleted
        while element is not None and element.data.rollno != rollno:
            prevelement = element
            element = element.next
        # If roll no was not present in linked list
        if element==None:
            print("No such Roll No")
            return
        print("Student Update : ")
        element.setData2(str(attendence))
        print(element.getData())
        
    
        
    def search(self, rollno):
        current = self.head #Initialize current
        while (current != None):
            if (current.data.rollno == rollno):
                print(current.getData())
                return True #data found
            current = current.next
        return False #data not found