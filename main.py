import psutil
from psutil._common import bytes2human
import sys


def check_argument():
    allowed_args = ['cpu', 'mem']
    if len(sys.argv) == 1 or len(sys.argv) > 2 or not sys.argv[1].lower() in allowed_args:
        print("Provide correct argument cpu or mem.")
        sys.exit(1)
    else:
        return sys.argv[1].lower()


def print_metric(data, metric):
    for name in data._fields:
        value = getattr(data, name)
        if metric == 'mem':
            value = bytes2human(value)
        print("{:15}{:>10}".format(name.capitalize(), value))


def main():
    metric = check_argument()
    if metric == 'cpu':
        print('CPU:')
        print_metric(psutil.cpu_times_percent(percpu=False), metric)
    else:
        print('MEMORY:')
        print_metric(psutil.virtual_memory(), metric)
        print('\nSWAP:')
        print_metric(psutil.swap_memory(), metric)


if __name__ == '__main__':
    main()