import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id, self.name, self.position, self.salary = employee_id, name, position, salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_csv(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"


class EmployeeManager:
    FILENAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILENAME):
            open(self.FILENAME, 'w').close()

    def load_employees(self):
        try:
            with open(self.FILENAME, 'r') as file:
                return [Employee.from_csv(line) for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save_employees(self, employees):
        with open(self.FILENAME, 'w') as file:
            file.writelines(emp.to_csv() + '\n' for emp in employees)

    def add_employee(self):
        print("\n--- Add New Employee ---")
        emp = Employee(input("Enter Employee ID: "), input("Enter Name: "), input("Enter Position: "), float(input("Enter Salary: ")))
        employees = self.load_employees()
        employees.append(emp)
        self.save_employees(employees)
        print("Employee added successfully!")

    def view_all_employees(self):
        print("\n--- All Employee Records ---")
        employees = self.load_employees()
        if not employees:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for emp in employees:
                print(emp)

    def search_employee(self):
        print("\n--- Search Employee by ID ---")
        employee_id = input("Enter Employee ID to search: ")
        employees = self.load_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(emp)
                return
        print(f"No employee found with ID: {employee_id}")

    def update_employee(self):
        print("\n--- Update Employee Information ---")
        employee_id = input("Enter Employee ID to update: ")
        employees = self.load_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                print("Employee Found. Enter new details:")
                emp.name = input("Enter new Name: ")
                emp.position = input("Enter new Position: ")
                emp.salary = float(input("Enter new Salary: "))
                self.save_employees(employees)
                print("Employee updated successfully!")
                return
        print(f"No employee found with ID: {employee_id}")

    def delete_employee(self):
        print("\n--- Delete Employee Record ---")
        employee_id = input("Enter Employee ID to delete: ")
        employees = self.load_employees()
        initial_count = len(employees)
        employees = [emp for emp in employees if emp.employee_id != employee_id]
        if len(employees) < initial_count:
            self.save_employees(employees)
            print("Employee record deleted successfully!")
        else:
            print(f"No employee found with ID: {employee_id}")

    def run_menu(self):
        print("Welcome to the Employee Records Manager!")
        while True:
            print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
            choice = input("Enter your choice: ")
            actions = {
                '1': self.add_employee,
                '2': self.view_all_employees,
                '3': self.search_employee,
                '4': self.update_employee,
                '5': self.delete_employee,
                '6': lambda: print("Goodbye!") or exit()
            }
            action = actions.get(choice, lambda: print("Invalid choice. Please try again."))
            action()


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run_menu()
