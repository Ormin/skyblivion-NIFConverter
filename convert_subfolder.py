

import os
import sys
import time
import commandline
from subprocess import call
from subprocess import Popen
from subprocess import list2cmdline
from optparse import OptionParser



def cpu_count():
    ''' Returns the number of CPUs in the system
    '''
    num = 1
    if sys.platform == 'win32':
        try:
            num = int(os.environ['NUMBER_OF_PROCESSORS'])
        except (ValueError, KeyError):
            pass
    elif sys.platform == 'darwin':
        try:
            num = int(os.popen('sysctl -n hw.ncpu').read())
        except ValueError:
            pass
    else:
        try:
            num = os.sysconf('SC_NPROCESSORS_ONLN')
        except (ValueError, OSError, AttributeError):
            pass

    return num

def exec_commands(cmds):
    ''' Exec commands in parallel in multiple process 
    (as much as we have CPU)
    '''
    if not cmds: return # empty list

    def done(p):
        return p.poll() is not None
    def success(p):
        return p.returncode == 0
    def fail():
        sys.exit(1)

    max_task = cpu_count()
    processes = []
    while True:
        while cmds and len(processes) < max_task:
            task = cmds.pop()
            processes.append(Popen(task))

        for p in processes:
            if done(p):
                if success(p):
                    processes.remove(p)
                else:
                    fail()

        if not processes and not cmds:
            break
        else:
            time.sleep(0.05)


commands = []
(options,args) = commandline.create();

inputdir = args[0];
outputdir = args[1];
subfolder_stub = ["python","convert_subfolder.py"];
mesh_stub = ["python",options.usedScript+".py"];
options_stub = [];

for value in (options.__dict__.items()):
		options_stub.append("--" + value[0] + "=" + value[1]);


if not os.path.exists(outputdir):
    os.makedirs(outputdir)

listdir = os.listdir(inputdir)
i = 1
for mesh in listdir:

	if os.path.isdir(inputdir+"\\"+mesh):
		finalargs = subfolder_stub + options_stub + [inputdir+"\\"+mesh,outputdir+"\\"+mesh];
		call(finalargs);
			
	else:
		if(mesh[-3:].lower() == "nif"):		
			finalargs = mesh_stub + options_stub + [inputdir+"\\"+mesh,outputdir+"\\"+mesh];
			commands.append(finalargs);

exec_commands(commands)