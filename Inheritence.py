class person:
    def __init__(self,fname,lname):
        self.Firstname=fname
        self.Lastname=lname
    def print(self):
        print(self.Firstname)
        print(self.Lastname)
        print(self.contactNumber)
    def personContact(self,contact):
        self.contactNumber=contact
class Student(person):
    def __init(self,sname,slname):
       self.studentFname=sname
       self.studentLname=slname
       super.__init__(self,sname,slname) #student class will run all the properties of parentclass
Student1=Student("osama","Ayub")
Student1.personContact(3314828005)
Student1.print()