class Student:
    def __init__(self,fname,lname,studentRollNo):
        self.__Firstname=fname
        self.__Lastname=lname
        self.__StudentRollNumber=studentRollNo
    def setName(self,name):
        self.__Firstname=name
    def setLname(self,lname):
        self.__Lastname=lname
    def setstudentRollNo(self,roll_no):
        self.__StudentRollNumber=roll_no
    def getFName(self):
        return self.__Firstname
    def getLname(self):
        return self.__Lastname
    def getStudentRollNo(self):
        return self.__StudentRollNumber
    def print(self):
        print(self.__Firstname)
        print(self.__Lastname)
        print(self.__StudentRollNumber)
Student1=Student("osama","Ayub","L1S18BSCS0095")
Student1.print()