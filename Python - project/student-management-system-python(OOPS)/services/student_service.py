class Service:
    def __init__(self):
        self.students = []  

    def create_table(self):
        print("Table created (memory me)")

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        for s in self.students:
            print(f"   {s.id }  || {s.name} ||   {s.age }   ||   {s.course}   ||   {s.email}  ")

    def delete(self, id):
        for s in self.students:
            if int(s.id) == id:
                self.students.remove(s)
                break