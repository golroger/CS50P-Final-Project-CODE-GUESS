from project import generate_code
from project import is_validguess
from project import injured_number
from project import dead_number
import pytest

def main() :
    test_is_validguess()
    test_injured_number()
    test_dead_number()



def test_is_validguess():

    assert is_validguess("1234") == (True,"")
    assert is_validguess("0231") == (False, "Can't start with 0, enter a valid number !")
    assert is_validguess("123456") == (False , "Your Guess number is too large !")
    assert is_validguess("5567") == (False , "Your guess number contain doubles ! ")
    assert is_validguess("df4ee") == (False , " Type a valid number !")

def test_injured_number():
    code = "1234"
    assert injured_number(code, "2567") == 1
    assert injured_number(code, "2314") == 3

def test_dead_number() :
    code = "5678"
    assert dead_number(code, "5678") == 4
    assert dead_number(code , "5123") == 1

if __name__ == "__main__" :
    main()

