class student:
    def __init__(self,name,reg_no,age,gender,branch,sem):
        self.name = name
        self.reg_no = reg_no
        self.age = age
        self.gender = gender
        self.branch = branch
        self.sem = sem

class StudentResultInfo(student):
    def __init__(self,name,reg_no,age,gender,branch,sem,students_total_marks, percentage,grade):
     super().__init__(name,reg_no,age,gender,branch,sem)
     self.students_total_marks = students_total_marks
     self.percentage = percentage
     self.grade = grade

st_1 = StudentResultInfo('Tarun','20bcs133',20,'male','cs','3rd',999,'99.9%','A+')

print(st_1.name,st_1.reg_no,st_1.age,st_1.gender,st_1.branch,st_1.sem,st_1.students_total_marks,st_1.percentage,st_1.grade)


