#This file will hold the test cases for my calculator module

#Pytest is a module that allows us to write our unit tests
#Name our file with our tests using test_.. OR .._test.py
#the module searches for files with the 'test' beginning or end

#in order to write our tests with pytest, we need to import 2 things:
#pytest itself
#code from the module we are testing

#Unit testing allows us to test the smallest portion of our code("bite-sized pieces")
#Unit test directly call the code under the test
#this introduces some considerations for when your code communicates with other systems
#external APIs, databases

import pytest
from calculator import add, subtract, multiply, divide

#naming convention for python tests
#test_{method name}_{what you are testing for}

def test_add_success():

    #unit tests typically follow an A-A-A structure
    #Arrange, Act, Assert

    #Arrange - any variables or test data that we need to set up
    x = 4
    y = 8

    #Act - here is where we actually call the code under test
    result = add(x, y)

    #Assert - we know what data was fed in, we know what we SHOULD get back
    #we assert that the result is what was intended
    assert result == 12

def test_divide_success():

    #AAA

    #Arrange
    x = 4
    y = 2

    #Act
    result = divide(x, y)

    #Assert
    assert result == 2

def test_divide_divide_by_zero_exception():
    #Arrange
    x = 400
    y = 0 #intentionally dividing by 0

    #Act
    with pytest.raises(ValueError) as ex:
        divide(x, y) #inside this with we call the method
    
    #Assert
    #Cast to a string for easy comparison
    assert str(ex.value) == "Cannot divide by zero"
