import os
import pickle


def create_dir(directory):
    try:
        os.mkdir(directory)
    except OSError:
        pass    # directory already exists.


def install_default_settings(settings_file):
    if not os.path.exists(settings_file):
        default_settings = "INSTANCE_ID1 = ''\n" \
                           "INSTANCE_ID2 = ''\n\n" \
                           "AWS_ACCESS_KEY_ID = ''\n" \
                           "AWS_SECRET_ACCESS_KEY = ''\n"
        with open(settings_file, 'w') as f:
            f.write(default_settings)


def reverse_instances(instance_list, state_file):
    """Reverse instance_list and store latest state."""
    if os.path.exists(state_file):
        with open(state_file) as f:
            instance_list = pickle.load(f)
    instance_list.reverse()
    with open(state_file, 'w') as f:
        pickle.dump(instance_list, f)
    return instance_list
