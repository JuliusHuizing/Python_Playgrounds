import unittest
from EmployeeClass import Employee

class test_EmployeeClasss(unittest.TestCase):
    def test_init(self):
        Julius = Employee('Julius', 'Huizing')
        self.assertIsInstance(Julius, Employee)
        self.assertEqual(Julius.get_name(), 'Julius Huizing')
            
if __name__ == '__main__':
    unittest.main()