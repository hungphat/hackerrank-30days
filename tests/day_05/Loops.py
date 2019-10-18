import unittest
import filecmp
import textwrap

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now

from day_05.Loops import run

class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    def test_tc00(self):
            #region make input file
            valid_input = '/tmp/loop.input'
            lines = textwrap.dedent('''
               2
            ''').strip()
            with open(valid_input, 'w') as f:
                print(lines, file=f)
            #endregion

            #region make expected output
            expected_output = '/tmp/loop.expected.out'
            with open(expected_output, 'w') as fo:
                lines_o = textwrap.dedent('''
                    2 x 1 = 2
                    2 x 2 = 4
                    2 x 3 = 6
                    2 x 4 = 8
                    2 x 5 = 10
                    2 x 6 = 12
                    2 x 7 = 14
                    2 x 8 = 16
                    2 x 9 = 18
                    2 x 10 = 20               
                ''').strip()
                print(lines_o, file=fo)
            #endregion make expected output

            # run testes code
            actual_output = '/tmp/loop.out'
            run(valid_input, actual_output)

            # check for expected values
            assert filecmp.cmp(actual_output, expected_output)

