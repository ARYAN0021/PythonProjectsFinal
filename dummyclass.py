class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
        self.name=name
        self.age=age
        self.level=level
        self.grades=grades or {}
        self.gender=gender
    def setGrade(self,course,grade):
        self.grades[course]=grade
    def getGrade(self,course):
        return self.grades[course]
    def getGpa(self):
        return sum(self.grades.values())/len(self.grades)

aryan=Student("Aryan",15,"Male",10,{"Maths":93})
Arjav=Student("Arjav",16,"Male",11,{"Maths":98})
aryan.setGrade("English",85)
print(aryan.getGpa())
print(Arjav.getGrade("Maths"))
Arjav.name="Avanian"
print(Arjav.name)


