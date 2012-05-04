"""
AWS EC2 Instances module
"""
import time
from boto.ec2.connection import EC2Connection


class InstanceManager(object):
    """
    Manager instance commands.
    """
    def __init__(self, access_key_id, secret_access_key, instance_id_list):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.instance_id_list = instance_id_list
        self.wait_update = 5

    def status(self):
        """
        Return a list with instance status.
        """
        statuses = []
        for instance in self._get_instances(self.instance_id_list):
            statuses.append((instance, instance.state, instance.ip_address))
        return statuses

    def start(self):
        """
        Start instances and return status.
        """
        statuses = []
        instances = self._get_instances(self.instance_id_list)
        for instance in instances:
            if instance.state != 'running':
                instance.start()
        for instance in instances:
            while instance.state != 'running':
                time.sleep(self.wait_update)
                instance.update()
            statuses.append((instance, instance.state, instance.ip_address))
        return statuses

    def stop(self):
        """
        Stop instances and return status.
        """
        statuses = []
        instances = self._get_instances(self.instance_id_list)
        for instance in instances:
            if instance.state != 'stopped':
                instance.stop()
        for instance in instances:
            while instance.state != 'stopped':
                time.sleep(self.wait_update)
                instance.update()
            statuses.append((instance, instance.state, instance.ip_address))
        return statuses

    def _get_instances(self, instance_id_list):
        """
        Return a list of ec2 instance objects specified by instance ids.
        """
        instances = []
        conn = EC2Connection(self.access_key_id, self.secret_access_key)
        reservations = conn.get_all_instances()
        for instance_id in instance_id_list:
            for reservation in reservations:
                for instance in reservation.instances:
                    if instance.id == instance_id:
                        instances.append(instance)
        return instances
