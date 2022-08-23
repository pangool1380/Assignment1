#Assignment 1

import datetime

class AbstractRailwayEmployee:
    # Abstract class for railway employees with constructors: first_name(string), last_name(string), employee_id(int), date_started(date)
    def __init__(self, first_name, last_name, employee_id, date_started):
        AbstractRailwayEmployee._validate_string(first_name)
        self._first_name = first_name
        AbstractRailwayEmployee._validate_string(last_name)
        self._last_name = last_name
        AbstractRailwayEmployee._validate_int(employee_id)
        self._employee_id = employee_id
        AbstractRailwayEmployee._validate_date(date_started)
        self._date_started = date_started



    def set_id(self, employee_id):
        self._employee_id = employee_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return self._first_name + " " + self._last_name

    # Method to get the ID of the employee(int)
    def get_employee_id(self):
        return self._employee_id

    def get_date_started(self):
        return self._date_started

    #get_details(string)
    # Returns a string with the details of the employee
    def get_details(self):
        return "Employee ID: " + str(self._employee_id) + "\n" + "Name: " + self.get_full_name() + "\n" + "Date started: " + datetime(self._date_started)

    #get_type(string)
    # Returns a string with the type of the employee
    #Child must implement this method
    def get_type(self):
       #Returns a string with the type of the employee
        #Child must implement this method
        raise NotImplementedError("Child must implement this method")
        return "AbstractRailwayEmployee"





    @staticmethod
    def _validate_string(label, value):
        """ Values a string value """
        if value is None:
            raise ValueError(label + " must be defined.")
        if value == "":
            raise ValueError(label + " cannot be empty.")

    @staticmethod
    def _validate_int(label, value):
        """ Values an integer value """
        if value is None:
            raise ValueError(label + " must be defined.")
        if value == "":
            raise ValueError(label + " cannot be empty.")
        if not isinstance(value, int):
            raise ValueError(label + " must be an integer.")

    @staticmethod
    def _validate_date(label, value):
        """ Values a date value """
        if value is None:
            raise ValueError(label + " must be defined.")
        if value == "":
            raise ValueError(label + " cannot be empty.")
        if not isinstance(value, datetime.date):
            raise ValueError(label + " must be a date.")
















