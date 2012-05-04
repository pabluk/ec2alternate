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
    """
    Reverse instance_list and store latest state.

    >>> from tempfile import NamedTemporaryFile
    >>> state_file = NamedTemporaryFile()

    >>> reverse_instances(['i-1111', 'i-2222'], state_file.name)
    ['i-2222', 'i-1111']
    >>> reverse_instances(['i-1111', 'i-2222'], state_file.name)
    ['i-1111', 'i-2222']
    >>> reverse_instances(['i-1111', 'i-2222'], state_file.name)
    ['i-2222', 'i-1111']

    >>> reverse_instances(['i-3333', 'i-4444'], state_file.name)
    ['i-4444', 'i-3333']
    >>> reverse_instances(['i-3333', 'i-4444'], state_file.name)
    ['i-3333', 'i-4444']
    >>> reverse_instances(['i-3333', 'i-4444'], state_file.name)
    ['i-4444', 'i-3333']

    """
    if os.path.exists(state_file):
        with open(state_file) as f:
            try:
                stored_instance_list = pickle.load(f)
                if (set(stored_instance_list) & set(instance_list)):
                    instance_list = stored_instance_list
            except EOFError:
                # file empty
                pass
    instance_list.reverse()
    with open(state_file, 'w') as f:
        pickle.dump(instance_list, f)
    return instance_list
