#Assignment 1

from abstract_railway_employee import AbstractRailwayEmployee


class RailwayManager:
    """Railway Manager class"""
    #Constructor: employees(list of AbstractRailwayEmployee)
    def __init__(self):
        self._employees = []

    #Add employee(employee: AbstractRailwayEmployee)
    def add_employee(self, employee):
        """Add a new employee to the list of employees"""
        if not isinstance(employee, AbstractRailwayEmployee):
            raise ValueError("Employee must be an instance of AbstractRailwayEmployee")
        #If the employee already exists, raise an error
        for e in self._employees:
            if e.get_employee_id() == employee.get_employee_id():
                raise ValueError("Employee already exists")
        self._employees.append(employee)

        #Remove employee by ID(employee_id: int)
    def remove_employee(self, employee_id):
        """Remove an employee from the list of employees"""
        for e in self._employees:
            if e.get_employee_id() == employee_id:
                self._employees.remove(e)
                return True
        #If the employee does not exist, raise an error
        if not self.employee_exists(employee_id):
            raise ValueError("Employee does not exist")
        return False

    # get(id : int) : AbstractEmployee
    def get_employee(self, employee_id):
        """Get an employee from the list of employees"""
        for e in self._employees:
            if e.get_employee_id() == employee_id:
                return e
        #If the employee does not exist, raise an error
        if not self.employee_exists(employee_id):
            raise ValueError("Employee does not exist")
        return None


    # employee_exists(id : int) : bool
    def employee_exists(self, employee_id):
        """Check if an employee exists in the list of employees"""
        for e in self._employees:
            if e.get_employee_id() == employee_id:
                return True
        return False

    #get_all_employees() : list of AbstractRailwayEmployee
    def get_all_employees(self):
        """Get all employees from the list of employees"""
        return self._employees

    # get_all_by_type(type : string) : AbstractEmployee[]
    def get_all_by_type(self, type):
        """Get all employees of a certain type from the list of employees"""
        employees = []
        for e in self._employees:
            if e.get_type() == type:
                employees.append(e)
        return employees

    # update(employee : AbstractEmployee)
    def update_employee(self, employee):
        """Update an employee in the list of employees"""
        if not isinstance(employee, AbstractRailwayEmployee):
            raise ValueError("Employee must be an instance of AbstractRailwayEmployee")
        #If the employee does not exist, raise an error
        if not self.employee_exists(employee.get_employee_id()):
            raise ValueError("Employee does not exist")
        for e in self._employees:
            if e.get_employee_id() == employee.get_employee_id():
                self._employees.remove(e)
                self._employees.append(employee)
                return True
        return False








