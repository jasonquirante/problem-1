class Employee:
    def __init__(self, employee_id, name, organization):
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = []

    def mark_attendance(self, present):
        self.attendance.append(present)

    def attendance_percentage(self):
        if not self.attendance:
            return 0
        return (sum(self.attendance) / len(self.attendance)) * 100

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}), Organization: {self.organization}, Attendance: {self.attendance_percentage():.2f}%"


class AttendanceTracker:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        organization = input("Enter organization name: ")
        new_employee = Employee(employee_id, name, organization)
        self.employees.append(new_employee)
        print("Employee added successfully!")

    def mark_attendance(self):
        employee_id = input("Enter employee ID to mark attendance: ")
        for employee in self.employees:
            if employee.employee_id == employee_id:
                present = input("Is the employee present? (y/n): ").lower() == 'y'
                employee.mark_attendance(1 if present else 0)
                print("Attendance marked successfully!")
                return
        print("Employee not found.")

    def display_attendance(self):
        if not self.employees:
            print("No employees in the system.")
        else:
            for employee in self.employees:
                print(employee)

    def menu(self):
        while True:
            print("\nEmployee Attendance Tracker Menu")
            print("1. Add Employee")
            print("2. Mark Attendance")
            print("3. Display All Attendance Records")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.mark_attendance()
            elif choice == '3':
                self.display_attendance()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    attendance_tracker = AttendanceTracker()
    attendance_tracker.menu()
