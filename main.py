"""
    This script was written by Oleksii Chaban for DevOps GL ProCamp
    Feb 2020
"""

import psutil
from psutil._common import bytes2human
import sys


""" This function checks that the argument which was provided to the script is correct   
    and stops the script in case the argument is wrong. 
    In case you need to add a new argument, modify allowed_args list"""
def check_argument():
    allowed_args = ['cpu', 'mem']
    if len(sys.argv) == 1 or len(sys.argv) > 2 or not sys.argv[1].lower() in allowed_args:
        print("Provide correct argument cpu or mem.")
        sys.exit(1)
    else:
        return sys.argv[1].lower()


""" print_metric function prints formatted output to the console.
    This function takes two arguments:
    data - metric data
    metrics - an argument provided by the user to the script"""
def print_metric(data, metric):
    for name in data._fields:
        value = getattr(data, name)

        # Shows a value in a human-readable format for Memory metric (B, Kb, Mb, Gb)
        if metric == 'mem':
            value = bytes2human(value)

        print("{:15}{:>10}".format(name.capitalize(), value))

# The main function in the script, it executes all other functions and prints output to the user
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