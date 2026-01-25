import sys

def get_dangerous_input():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "default_value"
