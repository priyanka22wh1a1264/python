import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:
    hra_percent = 20 

    def __init__(self, emp_id, name, basic_salary, leaves_taken=0):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.leaves_taken = leaves_taken
        self.salary = 0

    def calculate_salary(self):
        hra = self.basic_salary * Employee.hra_percent / 100
        self.salary = self.basic_salary + hra
        logging.info("salary calculated for %s (ID: %s): %.2f", self.name, self.emp_id, self.salary)

    def apply_leave_deduction(self, leave_deduction_per_day=500):
        deduction = self.leaves_taken * leave_deduction_per_day
        self.salary -= deduction
        logging.info("leave deduction applied for %s (ID: %s): %.2f", self.name, self.emp_id, deduction)

    def display_payslip(self):
        logging.info("payslip for %s (ID: %s): basic_salary: %.2f, HRA_per: %.2f%%,leavestaken: %d, total_sal: %.2f",
                     self.name, self.emp_id, self.basic_salary, Employee.hra_percent,
                     self.leaves_taken, self.salary)

    @classmethod
    def update_hra_percentage(cls, new_hra_percent):
        cls.hra_percent = new_hra_percent
        logging.info("updated HRA percentage: %s%%", cls.hra_percent)

e1 = Employee(101,"Priya",50000,2)
e1.calculate_salary()
e1.apply_leave_deduction()
e1.display_payslip()
e1.update_hra_percentage(25)
e1.calculate_salary()
e1.display_payslip()
