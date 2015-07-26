

import os
import sys
import time
import commandline
from subprocess import call
from subprocess import Popen
from subprocess import list2cmdline

print("MOPP_RL.exe uses havok. Copyright 1999-2013 Havok.com Inc. (and its Licensors).");
print("All Rights Reserved. See www.havok.com for details.");

(options,args) = commandline.create();



finalargs = ["python","convert_subfolder.py"];
for value in (options.__dict__.items()):

		finalargs.append("--" + value[0] + "=" + value[1]);

finalargs = finalargs + args;		
outputdir = args[1];
		
call(finalargs);

#After folder call the metadata collector
call(["php","metadata_collector.php",outputdir])