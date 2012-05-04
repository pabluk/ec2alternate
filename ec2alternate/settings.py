import os.path
# App specific settings
APP_DIR = os.path.expanduser('~/.ec2alternate')
USER_SETTINGS = os.path.join(APP_DIR, 'settings.py')
STATE_FILE = os.path.join(APP_DIR, 'state.db')

COMMANDS = ['status', 'start', 'stop', 'restart', 'now']

# Default settings
INSTANCE_ID1 = ''
INSTANCE_ID2 = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# Import user settings
try:
    execfile(USER_SETTINGS)
except IOError:
    pass    # first run file doesn't exists
