#!/usr/bin/python3
""" Unittests for City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Defines tests for the City class"""

    def __init__(self, *args, **kwargs):
        """ Constructor, Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the data type of the 'state.id' attribute in City class"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the data type of the 'name' attribute in City class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
