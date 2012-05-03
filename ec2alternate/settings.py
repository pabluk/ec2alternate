import os.path
# App specific settings
APP_DIR = os.path.expanduser('~/.ec2alternate')
USER_SETTINGS = os.path.join(APP_DIR, 'settings.py')

COMMANDS = ['status', 'start', 'stop', 'restart']

# Default settings
INSTANCES = []
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# Import user settings
try:
    execfile(USER_SETTINGS)
except IOError:
    pass    # first run file doesn't exists
