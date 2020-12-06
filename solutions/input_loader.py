import os, inspect

def load_input() -> str:
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    caller_filename = module.__file__.split(os.path.sep)[-1]
    target_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'inputs', caller_filename.replace('py', 'txt'))

    with open(target_filename, 'r') as f:
        return f.read().strip()