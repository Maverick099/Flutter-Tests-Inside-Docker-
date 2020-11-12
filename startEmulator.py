import os
import subprocess
import platform


def launch_emulator_win(emulator_id='Pixel_4_API_26'):
    print('[] Launching Emulator with id:{}'.format(emulator_id))
    os.system('Flutter emulators --launch {}'.format(emulator_id))


def launch_emulator_linux(emulator_id='Pixel_4_API_26'):
    print('[] Launching Emulator with id:{}'.format(emulator_id))
    subprocess.run(['Flutter', 'emulators', '--launch', emulator_id])


if __name__ == "__main__":
    checkPlatform = platform.system()
    print(checkPlatform)
    if checkPlatform == 'Windows':
        launch_emulator_win()
    else:
        launch_emulator_linux()
