#!/usr/bin/env python3

import os
import sys
import subprocess

# # Define the name of the config file
# config_file = '.git/hooks/nightly-rebase-config'

# # Define the default value for the nightly rebase setting
# default_setting = 'disabled'

# # Check if the config file exists
# if os.path.isfile(config_file):
#     # If it exists, read the current setting from the file
#     with open(config_file, 'r') as f:
#         current_setting = f.read().strip()
# else:
#     # If it doesn't exist, set the current setting to the default
#     current_setting = default_setting

# # Check the command line arguments to see if the user is trying to change the setting
# if len(sys.argv) > 1:
#     new_setting = sys.argv[1]
#     if new_setting == 'enabled' or new_setting == 'disabled':
#         current_setting = new_setting
#         with open(config_file, 'w') as f:
#             f.write(current_setting)
#     else:
#         print('Invalid argument, please use "enabled" or "disabled"')
#         exit(1)

# Check if the current branch is the master branch

current_setting = 'disabled'

if len(sys.argv) == 2:
    if sys.argv[1] == 'enabled':
        current_setting = 'enabled'
    elif sys.argv[1] == 'disable':
        current_setting = 'disabled'    
    else:
        print('Error: Invalid argument')
else:
    print('Error: Missing argument')

branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
if branch_name == 'master':
    exit(0)


if current_setting == 'disabled':
    exit(0)


subprocess.run(['git', 'fetch', 'origin'])
subprocess.run(['git', 'rebase', 'origin/master'])

print('Nightly rebase completed successfully')
