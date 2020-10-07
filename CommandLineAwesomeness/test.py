import os
from subprocess import getstatusoutput, getoutput 

prg = './CommandLineAwesomeness.py'

def test_file_exist():
    """ Purpose: Check if file exist """
    assert os.path.isfile(prg)
    

def test_runnable():
    """ Purpose: Check if program runs """
    out = getoutput(f'python3 {prg}')
    assert out.strip() == "Hello, World!"

def test_executable():
    out = getoutput(prg)
    assert out.strip() == "Hello, World!"

def test_input():
    for val in ['Universe', 'Multiuniverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            print (out)

            assert rv == 0
            assert out.strip() == f'Hello, {val}!'