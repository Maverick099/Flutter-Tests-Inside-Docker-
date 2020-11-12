import os
import subprocess
import platform


def run_flutter_tests(path, test_file='widget_test.dart'):
    if path == '' or path is None:
        path = r'D:\work_src\Medium Coders Asylum\Foddie\project-Foodie\project_foodie'

    check_path = path.split(':')
    dir_check = check_path[0].lower()
    print(dir_check)
    os.chdir(path)
    flutter_run = os.popen('flutter attach')
    print(flutter_run.read())


if __name__ == '__main__':
    checkPlatform = platform.system()

    if checkPlatform == 'Windows':
        print(checkPlatform)
        run_flutter_tests(r'D:\work_src\Medium Coders Asylum\Foddie\project-Foodie\project_foodie')
