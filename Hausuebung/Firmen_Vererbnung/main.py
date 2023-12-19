class Person:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender


class Employee(Person):
    def __init__(self, firstname, lastname, gender, salary):
        super().__init__(firstname, lastname, gender)
        self.salary = salary

class Department_Manager(Employee):
    def __init__(self, firstname, lastname, gender, salary):
        super().__init__(firstname, lastname, gender, salary)

class Department:
    def __init__(self, name):
        self.name = name
        self.department_manager = None
        self.employees = []

    def add_department_manager(self, department_manager):
        if self.department_manager == None:
            self.department_manager=department_manager
        else:
            print("Es ist schon ein Abteilungsleiter vorhanden!")

    def add_employee(self, employee):
        self.employees.append(employee)


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.departments = []

    def add_departments(self, department):
        self.departments.append(department)

    def count_employee_department_manager(self):
        employees = 0
        department_manager = 0
        for d in self.departments:
            employees += len(d.employees)
            department_manager += 1

        return employees, department_manager

    def count_departments(self):
        return len(self.departments)

    def largest_department(self):
        max_employees = 0
        largest_department = None
        for department in self.departments:
            if len(department.employees) > max_employees:
                max_employees = len(department.employees)
                largest_department = department
        return largest_department.name

    def calc_male_percentage(self):
        male_count = 0
        employee_total = 0
        for d in self.departments:
            employee_total += len(d.employees)
            for e in d.employees:
               if e.gender == 'male':
                   male_count += 1

        return male_count / employee_total * 100



if __name__ == "__main__":
    felix = Department_Manager("Felix", "Haider", "male", 3000)
    paula = Department_Manager("Paula", "Egger", "female", 3000)
    patrick = Employee("Patrick", "Klaric", "male", 2500)
    musterfrau = Employee("Martina", "Musterfrau", "female", 2500)
    beate = Person("Beate", "Müller", "female")

    finance = Department("finance")
    finance.add_department_manager(paula)
    finance.add_employee(musterfrau)
    finance.add_employee(patrick)

    software = Department("software")
    software.add_department_manager(felix)
    software.add_employee(patrick)
    software.add_employee(musterfrau)
    software.add_employee(musterfrau)

    lethal_company = Company("Lethal Company")
    lethal_company.add_departments(finance)
    lethal_company.add_departments(software)


    print("Anzahl der Mitarbeiter: " + str(lethal_company.count_employee_department_manager()[0]))
    print("Anzahl der Abteilungsleiter: " + str(lethal_company.count_employee_department_manager()[1]))
    print("Anzahl der Abteilungen: " + str(lethal_company.count_departments()))
    print("Größte Abteilung: " + str(lethal_company.largest_department()))
    print("Männlicher Anteil: " + str(lethal_company.calc_male_percentage()))
    print("Frauen Anteil: " + str(100 - lethal_company.calc_male_percentage()))