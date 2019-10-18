import unittest
import filecmp
import textwrap

def setUpModule():    pass # nothing here for now
def tearDownModule(): pass # nothing here for now

from day_09.Recursion_3 import run

class TestParallelRun(unittest.TestCase):

    def setUp(self):    pass # nothing here for now
    def tearDown(self): pass # nothing here for now


    def test_tc00(self):
            #region make input file
            valid_input = '/tmp/lets_review.input'
            lines = textwrap.dedent('''
                3
            ''').strip()
            with open(valid_input, 'w') as f:
                print(lines, file=f)
            #endregion

            #region make expected output
            expected_output = '/tmp/lets_review.expected.out'
            with open(expected_output, 'w') as fo:
                lines_o = textwrap.dedent('''
                      6     
                ''').strip()
                print(lines_o, file=fo)
            #endregion make expected output

            # run testes code
            actual_output = '/tmp/lets_review.out'
            run(valid_input, actual_output)

            # check for expected values
            assert filecmp.cmp(actual_output, expected_output)

