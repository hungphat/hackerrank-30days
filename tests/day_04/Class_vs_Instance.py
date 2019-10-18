import unittest
import filecmp
import textwrap

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now

from day_04.Class_vs_Instance import run

class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    def test_tc00(self):
            #region make input file
            valid_input = '/tmp/test_meal_compute.input'
            lines = textwrap.dedent('''
                4
                -1
                10
                16
                18  
            ''').strip()
            with open(valid_input, 'w') as f:
                print(lines, file=f)
            #endregion

            #region make expected output
            expected_output = '/tmp/test_meal_compute.expected.out'
            with open(expected_output, 'w') as fo:
                lines_o = textwrap.dedent('''
                    Age is not valid, setting age to 0.
                    You are young.
                    You are young.

                    You are young.
                    You are a teenager.

                    You are a teenager.
                    You are old.

                    You are old.
                    You are old.                  
                ''').strip()
                print(lines_o, file=fo)
            #endregion make expected output

            # run testes code
            actual_output = '/tmp/test_meal_compute.out'
            run(valid_input, actual_output)

            # check for expected values
            assert filecmp.cmp(actual_output, expected_output)

