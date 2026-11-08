from classes.employee import Employee

class Menager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def title(self):
        return "Menager"

    def monthly_cost(self):
        return super().monthly_cost() + self.bonus