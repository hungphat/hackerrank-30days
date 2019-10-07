import filecmp
import textwrap
import unittest

from day_02.Operators import meal_compute
from day_02.Operators import run


def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    def test_meal_compute(self):
        cost = meal_compute(meal=10, tip=5, tax=10)
        assert cost == 11  #-- tu so sanh bang lenh assert


    def test_tc00(self):
            #region make input file
            valid_input = '/tmp/test_meal_compute.input'
            lines = textwrap.dedent('''
                5
                10
                10   
            ''').strip()
            with open(valid_input, 'w') as f:
                print(lines, file=f)
            #endregion

            #region make expected output
            expected_output = '/tmp/test_meal_compute.expected.out'
            with open(expected_output, 'w') as fo:
                lines_o = textwrap.dedent('''
                    6 
                ''').strip()
                print(lines_o, file=fo)
            #endregion make expected output

            # run testes code
            actual_output = '/tmp/test_meal_compute.out'
            run(valid_input, actual_output)

            # check for expected values
            assert filecmp.cmp(actual_output, expected_output)
