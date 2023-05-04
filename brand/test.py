#!/usr/bin/env python3

import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description='Git utility to enable/disable nightly rebase')
    parser.add_argument('--enable', action='store_true', help='Enable nightly rebase')
    parser.add_argument('--disable', action='store_true', help='Disable nightly rebase')
    return parser.parse_args()

def get_current_branch():
    return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')

def is_master_branch():
    return get_current_branch() == 'master'

def enable_nightly_rebase():
    subprocess.call(['git', 'config', '--local', 'rebase.autoSquash', 'true'])
    subprocess.call(['git', 'config', '--local', 'rebase.autostash', 'true'])
    subprocess.call(['git', 'config', '--local', 'pull.rebase', 'true'])
    print('Nightly rebase enabled')

def disable_nightly_rebase():
    subprocess.call(['git', 'config', '--local', '--unset', 'rebase.autoSquash'])
    subprocess.call(['git', 'config', '--local', '--unset', 'rebase.autostash'])
    subprocess.call(['git', 'config', '--local', '--unset', 'pull.rebase'])
    print('Nightly rebase disabled')

def main():
    args = parse_args()
    # if is_master_branch():
    #     print('Cannot enable/disable nightly rebase on the master branch')
    #     return
    if args.enable and not args.disable:
        enable_nightly_rebase()
    elif args.disable and not args.enable:
        disable_nightly_rebase()
    else:
        print('Please specify either --enable or --disable')

if __name__ == '__main__':
    main()


# ./git-utility.py --enable  # Enable nightly rebase
# ./git-utility.py --disable # Disable nightly rebase