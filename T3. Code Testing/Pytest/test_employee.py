import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp1 = Employee('James', 'Bond', 50000)
        emp2 = Employee('Vika', 'Zhaliy', 35000)

        self.assertEqual(emp1.email, "James.Bond@email.com.ua")
        self.assertEqual(emp2.email, "Vika.Zhaliy@email.com.ua")

        emp1.last = 'Zhaliy'
        emp2.last = 'Bond'

        self.assertEqual(emp1.email, "James.Zhaliy@email.com.ua")
        self.assertEqual(emp2.email, "Vika.Bond@email.com.ua")

    def test_fullname(self):
        emp1 = Employee('James', 'Bond', 50000)
        emp2 = Employee('Vika', 'Zhaliy', 35000)

        self.assertEqual(emp1.fullname, "James Bond")
        self.assertEqual(emp2.fullname, "Vika Zhaliy")

        emp1.last = 'Zhaliy'
        emp2.last = 'Bond'

        self.assertEqual(emp1.fullname, "James Zhaliy")
        self.assertEqual(emp2.fullname, "Vika Bond")

    def test_apply_raise(self):
        emp1 = Employee('James', 'Bond', 50000)
        emp2 = Employee('Vika', 'Zhaliy', 35000)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 1.05 * 50000)
        self.assertEqual(emp2.pay, 1.05 * 35000)


class TestEmployee(unittest.TestCase):

    def test_weekly_report(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            report = Employee('Sergii', 'T', 1).weekly_report('W40')
            mocked_get.assert_called_with('http://company/com/Sergii/reports/W40')
            self.assertEqual(report, "Success")

            mocked_get.return_value.ok = False

            report = Employee('S', 'T', 1).weekly_report('W52')
            mocked_get.assert_called_with('http://company/com/S/reports/W52')
            self.assertEqual(report, "No response!")


if __name__ == "__main__":
    unittest.main()
