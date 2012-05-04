import sys
import unittest
from mock import patch
from StringIO import StringIO

from ec2alternate.main import main
from instance_mock import get_instances_mock


class MainTest(unittest.TestCase):

    def setUp(self):
        self.access_key_id = 'xxxxxxxx'
        self.secret_access_key = 'xxxx'
        self.instance_ids = ['i-1111', 'i-2222']

        self.out = StringIO()
        self.patcher = patch('ec2alternate.instances.' \
                             'InstanceManager._get_instances')
        self.mock_method = self.patcher.start()
        self.mock_method.return_value = get_instances_mock(self.instance_ids)

    def tearDown(self):
        self.patcher.stop()

    def test_without_arguments(self):
        sys.stderr = StringIO()
        self.assertRaises(SystemExit, main)

    def test_cmd_status(self):
        argv = self._get_argv('status')
        main(argv=argv, out=self.out)
        output_lines = self.out.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('Instance:i-1111 (name-i-1111) stopped'))
        self.assertTrue(output_lines[1].startswith('Instance:i-2222 (name-i-2222) stopped'))

    def test_cmd_start(self):
        argv = self._get_argv('start')
        main(argv=argv, out=self.out)
        output_lines = self.out.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('Instance:i-1111 running'))
        self.assertTrue(output_lines[1].startswith('Instance:i-2222 running'))

    def test_cmd_stop(self):
        argv = self._get_argv('stop')
        main(argv=argv, out=self.out)
        output_lines = self.out.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('Instance:i-1111 stopped'))
        self.assertTrue(output_lines[1].startswith('Instance:i-2222 stopped'))

    def test_cmd_restart(self):
        argv = self._get_argv('restart')
        main(argv=argv, out=self.out)
        output_lines = self.out.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('Instance:i-1111 running'))
        self.assertTrue(output_lines[1].startswith('Instance:i-2222 running'))

    def test_cmd_now(self):
        self.out = StringIO()
        argv = self._get_argv('now')
        main(argv=argv, out=self.out)
        output_lines = self.out.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('Instance:i-1111 (name-i-1111) running'))
        self.assertTrue(output_lines[1].startswith('Instance:i-2222 (name-i-2222) running'))

        instance_ids = self.mock_method.call_args[0][0]
        self.mock_method.return_value = get_instances_mock(instance_ids)
        self.out = StringIO()
        argv = self._get_argv('now')
        main(argv=argv, out=self.out)
        output_lines = self.out.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('Instance:i-2222 (name-i-2222) running'))
        self.assertTrue(output_lines[1].startswith('Instance:i-1111 (name-i-1111) running'))

    def _get_argv(self, cmd):
        argv = []
        argv.append('--aws-access-key-id=%s' % self.access_key_id)
        argv.append('--aws-secret-access-key=%s' % self.secret_access_key)
        argv.append('--instances=%s' % ','.join(self.instance_ids))
        argv.append(cmd)
        return argv


if __name__ == '__main__':
    unittest.main()
