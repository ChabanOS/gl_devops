## Basic system monitoring script

### About
This script allows to check the main performance metrics.
The script can show CPU load and Memory consumption.
The script was written on Python and uses psutil module.

### Requirements
Python 3 and psutil Python module should be installed.
To check Python version you can execute
`python -V`
In case you have different version check "How to install Python 3" for your OS
For further information please check the Installation section.

### Installation
Create the folder for the project and download the project into it.

`git clone https://github.com/ChabanOS/gl_devops.git`

`cd gl_devops`

Install psutil module

`pip install -r req.txt`

or

`pip install psutil`


### Usage
To see the CPU load execute

`python main.py cpu`

The output of the command will be the following:
```
CPU:
User                 95.2
System                3.6
Idle                  0.0
Interrupt             1.2
Dpc                   0.0
```
To see the Memory consumption execute the following:

`python main.py mem`

The output of the command will be the following:
```
MEMORY:
Total               19.9G
Available            6.7G
Percent             66.1B
Used                13.1G
Free                 6.7G

SWAP:
Total               42.4G
Used                35.7G
Free                 6.8G
Percent             84.1B
Sin                  0.0B
Sout                 0.0B

```
