from HTMLTestRunner import HTMLTestRunner
from db_fixture import test_data
import unittest, time

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    test_data.init_data()
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='Guest Manage System Interface Test Report', description='Implementation Example with:')
        runner.run(discover)