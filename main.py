import os
import platform
import subprocess
import re

import startEmulator
from runTests import run_flutter_tests

checkPlatform = platform.system()
print(checkPlatform)
cmd = ''
if checkPlatform == 'Windows':
    cmd = os.popen('flutter doctor')
else:
    subprocess.run(['flutter', 'doctor'])

line = cmd.read().splitlines()
version = re.findall(r'\d+.\d+.\d+', line[1])
splitLine = re.split(r'\W+', line[1])

if splitLine[1] == 'âˆš':
    print('[:)] Flutter Installed:\n\tchannel: {}\n\tversion: {}'.format(splitLine[4], version[0]))
else:
    print('[!] Flutter not installed.....')

startEmulator.launch_emulator_win()
run_flutter_tests(r'D:\work_src\Medium Coders Asylum\Foddie\project-Foodie\project_foodie')
# ToDo: Create a function to download flutter sdk if not found
# ToDo: create a function to download android sdk if not found
