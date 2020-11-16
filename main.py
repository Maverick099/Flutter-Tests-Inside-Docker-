"""
 This is the script will run the tests
"""
import os
import platform
import subprocess
import re
import argparse

import scripts.runTests
import scripts.startEmulator

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
        help='''Add the test file name/s with .dart extension for running test,
             if name is other than `widget_test.dart`''',
        type=str,
        nargs='+',
        default=['widget_test.dart'],
    )
    parser.add_argument(
        "-d", "--debug",
        help='Turn on Debugging mode',
        action='store_true'
    )
    parser.add_argument(
        '-e', '--emulator',
        help='Start default the emulator',
        action='store_true'
    )
    args = parser.parse_args()
    checkPlatform = platform.system()
    if args.debug:
        print('[D] Platform: {}'.format(checkPlatform))

    if checkPlatform == 'Windows':
        cmd = os.popen('flutter doctor')
        lines = cmd.read().splitlines()
        version = re.findall(r'\d+.\d+.\d+', lines[1])
        splitLine = re.split(r'\W+', lines[1])
        if args.debug:
            print('[D] Flutter Version: {}'.format(splitLine[0]))

        if args.emulator:
            scripts.startEmulator.launch_emulator_win()

        scripts.runTests.run_flutter_tests_win(
            path=args.path,
            test_file=args.file,
            debug=args.debug
        )

    else:
        p = subprocess.Popen(['flutter', 'doctor'])
        out, err = p.communicate()
        lines = out.decode("utf-8").splitlines()
        version = re.findall(r'\d+.\d+.\d+', lines[1])
        splitLine = re.split(r'\W+', lines[1])
        if args.debug:
            print('[D] Flutter Version: {}'.format(splitLine[0]))

        if args.emulator:
            scripts.startEmulator.launch_emulator_linux()

        scripts.runTests.run_flutter_tests_linux(
            path=args.path,
            test_file=args.file, 
            debug=args.debug
        )
