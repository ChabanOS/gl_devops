## Basic system monitoring script

### About
This script allows to check the main performance metrics.
The script can show CPU load and Memory consumption.
Also, the script shows the process that consumes the most resources.
The process result will be sorted and filtered based on the type of metrics you have provided as an argument.
The script was written on Python and uses psutil module.

### Requirements
Python 3 and psutil Python module should be installed.
To check Python version you can execute:
`python -V`
In case you have different version check "How to install Python 3" for your OS.
For further information please check the Installation section.

### Installation
Create the folder for the project and download the project into it:

`git clone https://github.com/ChabanOS/gl_devops.git`

`cd gl_devops`

Install psutil module:

`pip install -r req.txt`

or

`pip install psutil`


### Usage
To see the CPU load execute.

`python main.py cpu`

The output of the command will be the following:
```
CPU:
User                  0.0
Nice                  0.0
System                0.0
Idle                  0.0
Iowait                0.0
Irq                   0.0
Softirq               0.0
Steal                 0.0
Guest                 0.0
Guest_nice            0.0

PROCES:
     pid                name            CPU Time              Memory                User
     970                java             3657.90              388.3M       elasticsearch
     618                node             2241.91              294.5M              kibana
     967                beam             1128.29               34.8M            rabbitmq
     387        xfsaild/dm-0              128.06                0.0B                root
   21104          containerd              149.23               24.4M                root

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

### Docker
You have an option to run the script in a running docker container.
To do it just build an image (Dockerfile with all the instruction does already exist in the project folder).
To create the image, execute the following

```
docker build -t mon.script .

```

To use the created image execute

```
docker run --pid host -v /etc/passwd:/etc/passwd --rm mon.script cpu
docker run --pid host -v /etc/passwd:/etc/passwd --rm mon.script mem

```


### Customization
You can change the number of process that will be shown as output.
The variable could be changed in the script.
```
proc_num = 5    # Qty of processes that consumed the most CPU time
mem_val = 500   # in Mb, processes that consumed  more than 500Mb
```
