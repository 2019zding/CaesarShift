import unittest # module to run unit tests
import my_method # the file holding code we want to test

class CaesarShift(unittest.TestCase):

    def test_case1(self):
                # file.function(parameters), right answer
        self.assertEqual(my_method.caesarShift("gdkkn", 1),['h', 'e', 'l', 'l', 'o'],'Output should be hello')
        self.assertEqual(my_method.caesarShift("umpjb", 2),['w', 'o', 'r', 'l', 'd'],'Output should be world')
        self.assertEqual(my_method.caesarShift("yvb", 3),['b', 'y', 'e'],'Output should be bye')

if __name__ == '__main__':
    unittest.main()
