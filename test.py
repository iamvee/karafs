#!/usr/bin/env python3

""" Running the tests for karafs """

import os
import subprocess
from karafs.karafs import gen_str, gen_str_without_space

KARAFS_BIN = 'karafs/karafs.py'
if os.name == 'nt':
    KARAFS_BIN = KARAFS_BIN.replace('/', '\\')

def run_command(cmd='') -> str:
    """ Runs a command on karafs and returns the output as string """
    if os.name == 'nt':
        python_exe = 'python'
    else:
        python_exe = 'python3'
    return subprocess.check_output(
        python_exe + ' ' + KARAFS_BIN + ' ' + cmd,
        shell=True,
        stderr=subprocess.PIPE,
    ).decode().strip()

def test():
    """ Test the program """
    # run the command
    assert len(run_command().splitlines()) == 2

    assert len(run_command('-n 10').splitlines()) == 20

    assert len(run_command('en').splitlines()) == 1
    assert len(run_command('-en').splitlines()) == 1

    assert len(run_command('fa').splitlines()) == 1
    assert len(run_command('-fa').splitlines()) == 1

    assert len(run_command('fa -n 5').splitlines()) == 5
    assert len(run_command('-fa -n 5').splitlines()) == 5

    assert len(run_command('en -n 5').splitlines()) == 5
    assert len(run_command('-en -n 5').splitlines()) == 5

    assert len(run_command('other').splitlines()) == 0

    assert ' ' in run_command('-n 10')

    assert ' ' not in run_command('-n 10 --no-space')

    assert type(gen_str()) == str
    assert type(gen_str('fa')) == str

    assert type(gen_str_without_space()) == str
    assert type(gen_str_without_space('fa')) == str

    assert ' ' in gen_str()
    assert ' ' not in gen_str_without_space()

    assert len(run_command('-n').splitlines()) == 2

    assert len(run_command('-n abc').splitlines()) == 2

if __name__ == '__main__':
    test()
    print('Tests passed successfully.')
