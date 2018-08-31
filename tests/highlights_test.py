import unittest
from .models import highlights
Highlights = highlights,Highlights

class HighlightsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Highligths class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_highlights = Highlights(1234,'man kills his family and himself at last','voting in county 001','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_highlights,Highlights))


if __name__ == '__main__':
    unittest.main()