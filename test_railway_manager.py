#Assignment 1
import unittest
import datetime
from railway_manager import RailwayManager
from abstract_railway_employee import AbstractRailwayEmployee

#Test for the RailwayManager Class

class TestRailwayManager(unittest.TestCase):
    """TestRailwayManager class"""
    def setUp(self):
        self.rm = RailwayManager()
        self.employee1 = AbstractRailwayEmployee("John", "Doe", 1, datetime.date(2018, 1, 1))

    def tearDown(self):
        self.rm = None
        self.employee1 = None

    def logPoint(self, msg):
        """Log point"""
        print(msg)

    def test_add_employee_success(self):
        """Test add_employee method"""
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_all_employees(), [self.employee1])

    def test_add_employee_failure(self):
        """Test add_employee method"""
        self.rm.add_employee(self.employee1)
        self.assertRaises(ValueError, self.rm.add_employee, self.employee1)

    def test_remove_employee_success(self):
        """Test remove_employee method"""
        self.rm.add_employee(self.employee1)
        self.rm.remove_employee(1)
        self.assertEqual(self.rm.get_all_employees(), [])


    def test_remove_employee_failure(self):
        """Test remove_employee method"""
        self.rm.add_employee(self.employee1)
        self.assertRaises(ValueError, self.rm.remove_employee, 2)

    def test_get_employee(self):
        """Test get_employee method"""
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_employee(1), self.employee1)

    def test_employee_exists(self):
        """Test employee_exists method"""
        self.rm.add_employee(self.employee1)
        self.assertTrue(self.rm.employee_exists(1))
        self.assertFalse(self.rm.employee_exists(2))


    def test_get_all_employees(self):
        """Test get_all_employees method"""
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_all_employees(), [self.employee1])

    #Test get_all_by_type method in the RailwayManager class
    def test_get_all_by_type(self):
        """Test get_all_by_type method"""
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_all_by_type("Train Driver"), [self.employee1])



    def test_update_employee(self):
        """Test update_employee method"""
        self.rm.add_employee(self.employee1)
        self.rm.update_employee(self.employee1)
        self.assertEqual(self.rm.get_all_employees(), [self.employee1])




if __name__ == "__main__":
    unittest.main()




































if __name__ == '__main__':
    unittest.main()