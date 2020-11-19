import os
import subprocess
import platform
import argparse


def launch_emulator_win(emulator_id='Pixel_4_API_26', debug=False):
    """
    This for **Windows OS**
    The Function will launch the emulator for testing if needed.
    If id is not explicitly provided then the default *Pixel-4 emulator with API 26* will launch.
    :param emulator_id: pass id of the emulator that you want to start.
    :param debug: pass true for enabling debugging outputs.
    :return: None.
    """

    if debug:
        print('[D] Launching Emulator with id:{}'.format(emulator_id))

    emu = os.popen('Flutter emulators --launch {}'.format(emulator_id))
    print(emu.read())


def launch_emulator_linux(emulator_id='Pixel_4_API_26', debug=False):
    """
        This for **Linux OS**
        The Function will launch the emulator for testing if needed.
        If id is not explicitly provided then the default *Pixel-4 emulator with API 26* will launch.
        :param emulator_id: pass id of the emulator that you want to start
        :param debug: pass true for enabling debugging outputs.
        :return: None
        """
    if debug:
        print('[D] Launching Emulator with id:{}'.format(emulator_id))

    emu = subprocess.Popen(['Flutter', 'emulators', '--launch', emulator_id])
    print(emu.communicate())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug",
        action='store_true',
        help='Enable Debugging'
    )

    parser.add_argument(
        '-e', '--emulator',
        help='Start emulator with the respective emulator id',
        default='Pixel_4_API_26'
    )
    args = parser.parse_args()

    checkPlatform = platform.system()
    print(checkPlatform)
    if checkPlatform == 'Windows':
        launch_emulator_win(emulator_id=args.emulator, debug=args.debug)
    else:
        launch_emulator_linux(emulator_id=args.emulator, debug=args.debug)
