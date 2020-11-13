import os
import subprocess
import platform


def run_flutter_tests(path, test_file='widget_test.dart'):
    if path == '' or path is None:
        path = r'D:\work_src\test\flutter test\cli_test_app'

    os.chdir(path)
    flutter_test = os.popen(r'flutter test test/{}'.format(test_file))
    print(flutter_test.read())


if __name__ == '__main__':
    checkPlatform = platform.system()

    if checkPlatform == 'Windows':
        print(checkPlatform)
        run_flutter_tests(r'D:\work_src\test\flutter test\cli_test_app')
