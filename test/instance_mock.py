class EC2InstanceMock():
    def __init__(self, id):
        self.id = id
        self.state = 'stopped'

    def start(self):
        self.state = 'running'

    def stop(self):
        self.state = 'stopped'

    def update(self):
        pass

    def __str__(self):
        return "Instance:%s" % self.id


def get_instances_mock(instance_list):
    return [EC2InstanceMock(id) for id in instance_list]
