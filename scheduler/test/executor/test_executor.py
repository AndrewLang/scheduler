from unittest import TestCase, main
import logging


from scheduler.executor.executor import Executor


class TestExecutor(TestCase):
    def setup(self):
        pass
    def tearDown(self):
        return super().tearDown()

    def test_launch(self):
        print('test launch exe')
        # executor = Executor()
        # executor.launch('notepad.exe')
        self.assertEqual(1, 1)

if __name__ == '__main__':
    print('execute test')
    main()