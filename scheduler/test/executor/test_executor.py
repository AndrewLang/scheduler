from unittest import TestCase
import logging

from ...executor import Executor

class TestExecutor(TestCase):
    def setup(self):
        pass
    def tearDown(self):
        return super().tearDown()

    def test_launch(self):
        print('test launch exe')
        executor = Executor()
        executor.launch('notepad.exe')
        self.assertEquals(1, 2)

if __name__ == '__main__':
    print('execute ')
    unittest.main()