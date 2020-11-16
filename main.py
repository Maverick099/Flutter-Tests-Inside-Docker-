import os
import platform
import subprocess
import re

import scripts.runTests

checkPlatform = platform.system()
print(checkPlatform)
CMD = ''
if checkPlatform == 'Windows':
    CMD = os.popen('flutter doctor')
else:
    subprocess.run(['flutter', 'doctor'])

line = CMD.read().splitlines()
version = re.findall(r'\d+.\d+.\d+', line[1])
splitLine = re.split(r'\W+', line[1])

if splitLine[1] == 'âˆš':
    print('[:)] Flutter Installed:\n\tchannel: {}\n\tversion: {}'.format(splitLine[4], version[0]))
else:
    print('[!] Flutter not installed.....')

# startEmulator.launch_emulator_win()
scripts.runTests.run_flutter_tests_win(r'D:\work_src\test\flutter test\cli_test_app')
# ToDo: Create a function to download flutter sdk if not found
# ToDo: create a function to download android sdk if not found
