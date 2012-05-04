import unittest
from ec2alternate.instances import InstanceManager
from instance_mock import get_instances_mock


class InstanceManagerTest(unittest.TestCase):
    def setUp(self):
        self.instance_list = ['i-1', 'i-2', 'i-3']
        self.im = InstanceManager('xxxxxx', 'xxxxxx', self.instance_list)
        self.im._get_instances = get_instances_mock
        self.im.wait_update = 0

    def test_status(self):
        statuses = self.im.status()
        self.assertEqual(len(statuses), len(self.instance_list))

    def test_start(self):
        statuses = self.im.start()
        for id, state, ip_addr in statuses:
            self.assertEqual(state, 'running')
        self.assertEqual(len(statuses), len(self.instance_list))

    def test_stop(self):
        statuses = self.im.stop()
        for id, state, ip_addr in statuses:
            self.assertEqual(state, 'stopped')
        self.assertEqual(len(statuses), len(self.instance_list))


if __name__ == '__main__':
    unittest.main()
