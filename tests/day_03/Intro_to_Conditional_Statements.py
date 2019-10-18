import filecmp
import textwrap
import unittest

from day_03.Intro_to_Conditional_Statements import run

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now


class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    def test_tc00(self):
            #region make input file
            valid_input = '/tmp/test_meal_compute.input'
            lines = textwrap.dedent('''
                3
                24   
            ''').strip()
            with open(valid_input, 'w') as f:
                print(lines, file=f)
            #endregion

            #region make expected output
            expected_output = '/tmp/test_meal_compute.expected.out'
            with open(expected_output, 'w') as fo:
                lines_o = textwrap.dedent('''
                    Weird
                    Not Weird 
                ''').strip()
                print(lines_o, file=fo)
            #endregion make expected output

            # run testes code
            actual_output = '/tmp/test_meal_compute.out'
            run(valid_input, actual_output)

            # check for expected values
            assert filecmp.cmp(actual_output, expected_output)
