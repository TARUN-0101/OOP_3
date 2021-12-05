class Student:
  def __init__(self,nam,reg,ag,gen,bran,sem):
    self.name = nam
    self.regNo = reg
    self.age = ag
    self.gender = gen
    self.branch = bran
    self.semester = sem

  def displayBasic(self):
    print("""Student details: Name: {}
                              Reg No: {}
                              Age: {}
                              Gender: {}
                              Branch: {}
                              Semester: {} """.format(self.name,self.regNo,self.age,self.gender,self.branch,self.semester))
    
  
class StudentResultInfo(Student):
  def __init__(self,nam,reg,ag,gen,bran,sem,tot,perc,grad):
    Student.__init__(self,nam,reg,ag,gen,bran,sem)
    self.totalMarks = tot
    self.percentage = perc
    self.grade = grad

  def displayBasic(self):
    print("""Stdent details: Name: {} 
                             Reg No: {}
                             Age: {}
                             Gender: {}
                             Branch: {}
                             Semester: {}
                             Total Marks: {}
                             Percentage: {}
                             Grade: {}""".format(self.name,self.regNo,self.age,self.gender,self.branch,self.semester,self.totalMarks,self.percentage,self.grade))

S = StudentResultInfo("Adithya","20bcs006",19,"M","CSE",2,500,80,"B")
S.displayBasic()
