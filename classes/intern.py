from classes.employee import Employee

class Intern(Employee):
    def __init__(self, name, salary, months):
        if not months in range(1, 13):
            raise ValueError("months must be 1-12")
        super().__init__(name, salary)
        self.months = months

    def title(self):
        return "Intern"

    