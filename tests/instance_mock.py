import random
import datetime


class EC2InstanceMock():
    def __init__(self, id):
        self.id = id
        self.state = 'stopped'
        self.ip_address = self._random_ip_addr()
        self.launch_time = self._launch_time()
        self.tags = {'Name': 'name-%s' % id}

    def start(self):
        self.state = 'running'
        if not self.ip_address:
            self.ip_address = self._random_ip_addr()
        self.launch_time = self._launch_time()

    def stop(self):
        self.state = 'stopped'
        self.ip_address = None

    def update(self):
        pass

    def _random_ip_addr(self):
        return ".".join([str(random.randint(1, 254)) for i in range(4)])

    def _launch_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    def __str__(self):
        return "Instance:%s" % self.id


def get_instances_mock(instance_list):
    return [EC2InstanceMock(id) for id in instance_list]
