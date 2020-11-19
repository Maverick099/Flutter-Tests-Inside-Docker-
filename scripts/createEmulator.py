"""
Script to Create the emulator.
Currently, the scripts support only google api x86 images on Pixel device
"""

import os
import subprocess
import argparse
import platform


def create_emulator_win(api=26, name='Pixel_4', device='pixel'):
    """
    This program is for **Windows Platform**.
    The program will create the emulator for the given API and using the x86 images, supports API>=26
    and will evoke the *sdkmanager* to download the unavailable api.
    :param api: API level number.
    :param name: Name of the emulator
    :param device: The device that you would like to run the API
    :return: None
    """
    cmd = os.popen(
        'avdmanager --verbose create avd --force --name "{}" --device "{}" --package "system-images;android-{};google_apis;x86" --tag "google_apis" --abi "x86"'.format(
            name, device, api))

    print(cmd.read())


def create_emulator_linux(api=26, name='Pixel_4', device='pixel'):
    """
    This program is for **Linux Platform**.
    The program will create the emulator for the given API and using the x86 images, supports API>=26
    and will evoke the *sdkmanager* to download the unavailable api.
    :param api: API level number.
    :param name: Name of the emulator
    :param device: The device that you would like to run the API
    :return: None
    """
    cmd = subprocess.Popen([
        'avdmanager', '--verbose', 'create', 'avd', '--force',
        '--name "{}"'.format(name),
        '--device "{}"'.format(device),
        '--package "system-images;android-{};google_apis;x86"'.format(api),
        '--tag "google_apis"', ' --abi "x86"'
    ])
    print(cmd.communicate())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api",
        help='Enter the Android API version, supported >= 26',
        default=26

    )

    parser.add_argument(
        '--name',
        help='Name of the Android Emulator',
        required=True,
    )

    # parser.add_argument(
    #     '--device',
    #     help=' the device on which the emulator should run, the default is pixel'
    # )
    args = parser.parse_args()
    check_platform = platform.system()
    if check_platform == 'Windows':
        create_emulator_win(api=args.api, name=args.name)

    else:
        create_emulator_linux(api=args.api, name=args.name)
