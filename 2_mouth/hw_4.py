class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def str(self):
        return f"Имя: {self.name},email: {self.email},номер: {self.phone}"
    
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study
        
    def study(self):
        print(f"Имя - {self.name}, почта - {self.email}, телефон - {self.phone}, ID - {self.student_id}, группа - {self.group_where_study}")
   
student = Student('Байэл','tasievbajel@gmail.com', '0702 132 006', 1, 'back08')
student.study()

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach ):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach
        
    def teach(self):
        print(f"Имя - {self.name}, email - {self.email}, телефон - {self.phone}, ID - {self.teacher_id}, группа где он препаданет - {self.group_where_teach}")

teacher = Teacher('Нурай', 'nuraj9663@gmail.com', '0755 750 238', 2, '15-2B')
teacher.teach()
    
class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self,name, email, phone)
        self.admin_id = admin_id
    
    def create_group(self):
        print(f"Имя админа - {self.name}, email админа - {self.email}, телефон админа - {self.phone}, ID админа - {self.admin_id}")
        
admin = Admin('Камола', 'kamolaboribaevak13@gmail.com', '0708 492 045', 6)
admin.create_group()

class Mentor(Student, Teacher):
    def __init__(self, name, email, phone,student_id, group_where_study, teacher_id, group_where_teach ):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach )
        
    def study(self):
        print(f'Группа где он учится- {self.group_where_study}')

            
    def teach(self):
        print(f'Имя - {self.name}, email - {self.email}, телефон - {self.phone}, группа где он менторит - {self.group_where_teach}')
        
mentor = Mentor('Кудбухон', 'qweimxs@gmail.com', '0999 000 722', 4, '15-2B', 3, '16-1B')
mentor.study()
mentor.teach()
        