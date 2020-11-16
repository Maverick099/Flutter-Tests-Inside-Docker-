"""
This file is used for running test files
"""
import os
import subprocess
import platform
import argparse


def run_flutter_tests_win(path=r'home/tester/repo', test_file=None, debug=False):
    """
    This is for **Windows OS**.
    This will run the test file inside of your Flutter  project.
    It excepts the path to the file if your main flutter project is inside some folders in the repo,
    then  add the relative path.See docs for more info on this.
    It excepts list of file name/s as a parameter.
    Call it multiple times if you have more than one test file.
    """

    if test_file is None:
        test_file = ['widget_test.dart']

    os.chdir(path)
    if debug:
        print('[D] Directory Changed to: {}'.format(path))
        print('[D] Number of test files: {}'.format(len(test_file)))
    for file in test_file:
        flutter_test = os.popen(r'flutter test test\{}'.format(file))
        if debug:
            print('[D] Running Flutter Test from testFile : {} \n{}'.format(file, flutter_test.read()))
        else:
            print('Running Flutter Test: \n{}'.format(flutter_test.read()))


def run_flutter_tests_linux(path=r'home/tester/repo', test_file=None, debug=False):
    """
        This is for **LINUX OS**.
        This will run the test file inside of your Flutter  project.
        It excepts the path to the file if your main flutter project is inside some folders in the repo,
        then  add the relative path.See docs for more info on this.
        It excepts list of file name/s as a parameter.
        Call it multiple times if you have more than one test file.
    """
    if test_file is None:
        test_file = ['widget_test.dart']

    change_dir = subprocess.Popen(['cd', '{}'.format(path)])
    if debug:
        print(change_dir.communicate())
        print('[D] Number of test files: {}'.format(len(test_file)))

    for file in test_file:
        flutter_test = subprocess.Popen(['flutter', 'test', r'test\{}'.format(file)])
        if debug:
            print('[D] Running Flutter Test from testFile : {} \n{}'.format(file, flutter_test.communicate()))
        else:
            print('Running Flutter Test: \n{}'.format(flutter_test.communicate()))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p", "--path",
        help='Add the file path here, only if test folder is located other than repo/',
        type=str,
        default=r'home/tester/repo',
    )
    parser.add_argument(
        "-f", "--file",
        help='Add the test file name/s with .dart extension for running test, if name is other than `widget_test.dart`',
        type=str,
        nargs='+',
        default=['widget_test.dart'],
    )
    parser.add_argument(
        "-d", "--debug",
        help='Turn on Debugging mode',
        action='store_true'
    )
    parser.parse_args()
    args = parser.parse_args()

    checkPlatform = platform.system()
    if args.debug:
        print('Platform: {}'.format(checkPlatform))
        print(r'Test File Path:{}\test'.format(args.path))

    if checkPlatform == 'Windows':
        run_flutter_tests_win(path=args.path, test_file=args.file, debug=args.debug)
    else:
        run_flutter_tests_linux(path=args.path, test_file=args.file, debug=args.debug)
