import sys
import optparse

from ec2alternate import settings
from ec2alternate.instances import InstanceManager
from ec2alternate.utils import create_dir, install_default_settings


def bootstrap():
    """Initialize app dir and settings."""
    create_dir(settings.APP_DIR)
    install_default_settings(settings.USER_SETTINGS)


def process_command_line(argv):
    """
    Return a 2-tuple of command and options.
    """
    if argv is None:
        argv = sys.argv[1:]
    available_commands = "|".join(settings.COMMANDS)
    usage = "Usage: %prog [options] " + available_commands
    parser = optparse.OptionParser(usage=usage, version='%prog 0.1')
    parser.add_option('-i', '--instances', action="store",
                      dest="instances", help='run command on instances, ' \
                      'specify them in a comma-separated list')
    parser.add_option('--aws-access-key-id', action="store",
                      dest="aws_access_key_id",
                      help='use AWS access key id from command line')
    parser.add_option('--aws-secret-access-key', action="store",
                      dest="aws_secret_access_key",
                      help='use AWS secret access key from command line')
    options, args = parser.parse_args(argv)

    if not args:
        parser.error("No command specified. Use -h to see more options.")
    if len(args) > 1:
        parser.error("Too many arguments")
    if args and not args[0] in settings.COMMANDS:
        parser.error("Invalid command. Available commands: %s" \
                     % available_commands)
    if not (settings.AWS_ACCESS_KEY_ID and settings.AWS_SECRET_ACCESS_KEY) \
       and not (options.aws_access_key_id and options.aws_secret_access_key):
        parser.error("You must set your AWS credentials. " \
            "Please edit your configuration file %s" % settings.USER_SETTINGS)
    if not (settings.INSTANCE_ID1 or settings.INSTANCE_ID2) \
       and not options.instances:
        parser.error("You must specify your AWS instances. " \
            "Please edit your configuration file %s" % settings.USER_SETTINGS)
    return args[0], options


def main(argv=None, out=sys.stdout):
    bootstrap()
    cmd, options = process_command_line(argv)
    if options.instances:
        instances = options.instances.split(',')
    else:
        instances = [settings.INSTANCE_ID1, settings.INSTANCE_ID2]
    if options.aws_access_key_id and options.aws_secret_access_key:
        access_key_id = options.aws_access_key_id
        secret_access_key = options.aws_secret_access_key
    else:
        access_key_id = settings.AWS_ACCESS_KEY_ID
        secret_access_key = settings.AWS_SECRET_ACCESS_KEY

    im = InstanceManager(access_key_id, secret_access_key, instances)

    if cmd == 'status':
        statuses = im.status()
        for id, state in statuses:
            msg = "%s %s\n" % (id, state)
            out.write(msg)
    if cmd == 'start':
        statuses = im.start()
        for id, state in statuses:
            msg = "%s %s\n" % (id, state)
            out.write(msg)
    if cmd == 'stop':
        statuses = im.stop()
        for id, state in statuses:
            msg = "%s %s\n" % (id, state)
            out.write(msg)
    if cmd == 'restart':
        statuses = im.stop()
        statuses = im.start()
        for id, state in statuses:
            msg = "%s %s\n" % (id, state)
            out.write(msg)

    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
