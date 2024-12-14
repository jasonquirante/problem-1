class Student:
    def __init__(self, student_id, name, course, grades):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = grades

    def average_grade(self):
        if len(self.grades) == 0:
            return 0  # Avoid division by zero
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.student_id}: {self.name}, Course: {self.course}, Grades: {self.grades}, Average: {self.average_grade():.2f}"


class StudentGradeManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        course = input("Enter course: ")
        grades = []
        for i in range(1, 5):
            while True:
                try:
                    grade = float(input(f"Enter grade {i} (0-100): "))
                    if 0 <= grade <= 100:
                        grades.append(grade)
                        break
                    else:
                        print("Grade must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        new_student = Student(student_id, name, course, grades)
        self.students.append(new_student)
        print("Student added successfully!")

    def update_grade(self):
        student_id = input("Enter student ID to update: ")
        for student in self.students:
            if student.student_id == student_id:
                index = int(input("Enter the index of the grade to update (1-4): ")) - 1
                if 0 <= index < len(student.grades):
                    while True:
                        try:
                            new_grade = float(input("Enter new grade (0-100): "))
                            if 0 <= new_grade <= 100:
                                student.grades[index] = new_grade
                                print("Grade updated successfully!")
                                return
                            else:
                                print("Grade must be between 0 and 100. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                else:
                    print("Invalid index. Please try again.")
                return
        print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(student)

    def calculate_class_average(self):
        if not self.students:
            print("No students in the system.")
            return
        total_average = sum(student.average_grade() for student in self.students) / len(self.students)
        print(f"Class average grade: {total_average:.2f}")

    def menu(self):
        while True:
            print("\nStudent Grade Management Menu")
            print("1. Add Student")
            print("2. Update Student Grade")
            print("3. Display All Students")
            print("4. Calculate Class Average")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_grade()
            elif choice == '3':
                self.display_students()
            elif choice == '4':
                self.calculate_class_average()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again .")

if __name__ == "__main__":
    student_management = StudentGradeManagement()
    student_management.menu()
