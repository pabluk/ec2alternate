import random


class EC2InstanceMock():
    def __init__(self, id):
        self.id = id
        self.state = 'stopped'
        self.ip_address = self.random_ip_addr()

    def start(self):
        self.state = 'running'
        if not self.ip_address:
            self.ip_address = self.random_ip_addr()

    def stop(self):
        self.state = 'stopped'
        self.ip_address = None

    def update(self):
        pass

    def random_ip_addr(self):
        return ".".join([str(random.randint(1, 254)) for i in range(4)])

    def __str__(self):
        return "Instance:%s" % self.id


def get_instances_mock(instance_list):
    return [EC2InstanceMock(id) for id in instance_list]
