from models.student import Student
from services.student_service import Service

ser = Service()

ser.create_table()

while True:
    print('1. Press 1 to add Student')
    print('2. Press 2 to View all the students')
    print('3. Press 3 to delete student')
    print('4. Press 4 to exit')

    option = int(input('Enter the Option: '))

    if option == 1:
        id = input('Enter the Student ID: ')
        name = input('Enter the name of the student: ')
        age = int(input('Enter the age of the student: '))
        course = input('Enter the course detail of the student: ')
        email = input('Enter the email of the student: ')

        obj = Student(id, name, age, course, email)
        ser.add_student(obj)

        print('The student added successfully!')

    elif option == 2:
        data = ser.view_students()
        print(data)

    elif option == 3:
        id = int(input('Enter the id of the student: '))
        ser.delete(id)

        print('Student deleted successfully!')

    elif option == 4:
        print("Exiting program...")
        break

    else:
        print('Please enter a valid input')