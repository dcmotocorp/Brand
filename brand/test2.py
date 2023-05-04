import subprocess
import os, sys

def is_master_branch():
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
    return branch == 'master'

def enable_nightly_rebase():
    if is_master_branch():
        subprocess.run(['git', 'config', 'branch.master.rebase', 'true'])
        print('Nightly rebase enabled')
    else:
        print('Error: Not on the master branch')

def disable_nightly_rebase():
    subprocess.run(['git', 'config', '--unset', 'branch.master.rebase'])
    print('Nightly rebase disabled')


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'enable':
            enable_nightly_rebase()
        elif sys.argv[1] == 'disable':
            disable_nightly_rebase()
        else:
            print('Error: Invalid argument')
    else:
        print('Error: Missing argument')


main()