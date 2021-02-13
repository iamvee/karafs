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
        python_exe + ' ' + KARAFS_BIN + ' ' + cmd, shell=True
    ).decode().strip()

def test():
    """ Test the program """
    # run the command
    output = run_command()
    assert len(output.splitlines()) == 2

    output = run_command('-n 10')
    assert len(output.splitlines()) == 20

    output = run_command('en')
    assert len(output.splitlines()) == 1

    output = run_command('fa')
    assert len(output.splitlines()) == 1

    output = run_command('fa -n 5')
    assert len(output.splitlines()) == 5

    output = run_command('en -n 5')
    assert len(output.splitlines()) == 5

    output = run_command('other')
    assert len(output.splitlines()) == 0

    output = run_command('-n 10')
    assert ' ' in output

    output = run_command('-n 10 --no-space')
    assert ' ' not in output

    assert type(gen_str()) == str
    assert type(gen_str('fa')) == str

    assert type(gen_str_without_space()) == str
    assert type(gen_str_without_space('fa')) == str

    assert ' ' in gen_str()
    assert ' ' not in gen_str_without_space()

if __name__ == '__main__':
    test()
    print('Tests passed successfully.')
