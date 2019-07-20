class Employee:
    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self._normal_hours = 0
        self._overtime_hours = 0

    def register_time(self, hours):
        if hours > 8:
            self._normal_hours += 8
            self._overtime_hours += (hours - 8)
        else:
            self._normal_hours += hours

    def pay_salary(self):
        salary = self._normal_hours * self.rate_per_hour + 2 * self.rate_per_hour * self._overtime_hours
        self._overtime_hours = 0
        self._normal_hours = 0
        return salary


class PremiumEployee(Employee):

    def __init__(self, first_name, last_name, rate_per_hour):
        super().__init__(first_name, last_name, rate_per_hour)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        salary = super().pay_salary()
        salary += self.bonus
        self.bonus = 0
        return salary


class TestEmployee:

    def test_employee_initialization(self):
        employee = Employee("Rafał", "Korzeniewski", 100.0)

        assert employee.first_name == "Rafał"
        assert employee.last_name == "Korzeniewski"
        assert employee.rate_per_hour == 100.0

    def test_pay_salary_without_register_time(self):
        employee = Employee("Rafał", "Korzeniewski", 100.0)
        assert employee.pay_salary() == 0.0

    def test_pay_salary(self):
        employee = Employee("Rafał", "Korzeniewski", 100.0)
        employee.register_time(5)
        assert employee.pay_salary() == 500.0
        assert employee.pay_salary() == 0.0

    def test_pay_salary_overtime(self):
        employee = Employee("Rafał", "Korzeniewski", 100.0)
        employee.register_time(10)
        assert employee.pay_salary() == 1200.0
        assert employee.pay_salary() == 0.0

    def test_pay_salary_overtime_two_registrations(self):
        employee = Employee("Rafał", "Korzeniewski", 100.0)
        employee.register_time(5)
        employee.register_time(5)
        assert employee.pay_salary() == 1000.0
        assert employee.pay_salary() == 0.0

    def test_pay_salary_many_registrations_also_with_overtime(self):
        employee = Employee("Rafał", "Korzeniewski", 100.0)
        employee.register_time(10)
        employee.register_time(5)
        employee.register_time(10)
        employee.register_time(5)
        assert employee.pay_salary() == (5 + 5 + 8 + 8) * 100 + 4 * 200
        assert employee.pay_salary() == 0.0


class TestPremiumEployee:

    def test_pay_salary_with_bonus(self):
        employee = PremiumEployee("Jan", "Nowak", 100)
        employee.register_time(5)
        employee.give_bonus(1000)
        assert employee.pay_salary() == 1500.0
