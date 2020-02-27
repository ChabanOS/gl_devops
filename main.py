"""
    This script was written by Oleksii Chaban for DevOps GL ProCamp
    Feb 2020
"""

import sys
import psutil
from psutil._common import bytes2human

# Variables for customization output for process
proc_num = 5    # Qty of processes that consumed the most CPU time
mem_val = 500   # in Mb, processes that consumed  more than 500Mb


def check_argument():
    """ This function checks that the argument which was provided to the script is correct
        and stops the script in case the argument is wrong.
        In case you need to add a new argument, modify allowed_args list
    """

    allowed_args = ['cpu', 'mem']
    if len(sys.argv) == 1 or len(sys.argv) > 2 or not sys.argv[1].lower() in allowed_args:
        print(
            "Provide correct argument to the script.\n cpu - for CPU metrics. \n mem - for Memory metrics"
        )
        sys.exit(1)
    else:
        return sys.argv[1].lower()


def print_metric(data, metric):
    """ print_metric function prints formatted output to the console.
        This function takes two arguments:
        data - metric data
        metrics - an argument provided by the user to the script
    """
    for name in data._fields:
        value = getattr(data, name)

        # Shows a value in a human-readable format for Memory metric (B, Kb, Mb, Gb)
        if metric == 'mem':
            value = bytes2human(value)

        print("{:15}{:>10}".format(name.capitalize(), value))


def print_process(metric):
    """ functions sort, filter and print process are based on
        metric argument provided by the user to the script.
        mem - filtered by value from mem_val variable in Mb
        cpu - filtered by value from proc_num variable qty
    """

    print('{:>8}{:>20}{:>20}{:>20}{:>20}'.format('pid', 'name', 'CPU Time', 'Memory', 'User'))

    if metric == 'mem':
        mem = psutil.process_iter(['name', 'cpu_times', 'memory_info', 'username'])
        mem_sorted = sorted(mem, reverse=True, key=lambda p: p.info['memory_info'])
        for p in mem_sorted:
            if p.info['memory_info'].rss > mem_val * 1024 * 1024:
                print('{:>8}{:>20}{:>20.2f}{:>20}{:>20}'.format(
                    p.pid,
                    p.info['name'],
                    sum(p.info['cpu_times']),
                    bytes2human(p.info['memory_info'].rss),
                    str(p.info['username'])
                )
                )
    else:
        proc = psutil.process_iter(['name', 'cpu_times', 'memory_info', 'username'])
        proc_sorted = sorted(proc, reverse=True, key=lambda p: sum(p.info['cpu_times'][:2]))
        for p in proc_sorted[:proc_num]:
            print('{:>8}{:>20}{:>20.2f}{:>20}{:>20}'.format(
                p.pid,
                p.info['name'],
                sum(p.info['cpu_times']),
                bytes2human(p.info['memory_info'].rss),
                str(p.info['username'])
            )
            )


def main():
    """The main function in the script,
        it executes all other functions and prints output to the user
    """
    metric = check_argument()
    if metric == 'cpu':
        print('CPU:')
        print_metric(psutil.cpu_times_percent(percpu=False), metric)
    else:
        print('MEMORY:')
        print_metric(psutil.virtual_memory(), metric)
        print('\nSWAP:')
        print_metric(psutil.swap_memory(), metric)

    print('\nPROCES:')
    print_process(metric)


if __name__ == '__main__':
    main()