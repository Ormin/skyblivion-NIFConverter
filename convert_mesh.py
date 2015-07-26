
#from nif_common import NifImportExport
#from nif_common import NifConfig
#from nif_common import NifFormat
#from nif_common import EgmFormat
#from nif_common import __version__
#from itertools import izip
import os
import os.path
import sys
import time
import subprocess
import commandline
from subprocess import check_output
from subprocess import call
from subprocess import check_call
from optparse import OptionParser
#from subprocess import Popen
#from subprocess import list2cmdline
(options,args) = commandline.create();

path_mesh = args[0];
path_output = args[1];

finalargs = ["python","copyover_legacy_nif_animations.py"];

for value in (options.__dict__.items()):

		finalargs.append("--" + value[0] + "=" + value[1]);

finalargs = finalargs + [path_mesh,path_output+"_temp"];		

print("Converting "+path_mesh)

try:
	#output = call(finalargs);
	output = check_output(finalargs);
except subprocess.CalledProcessError:
	print(path_mesh + " conversion failed!")
	quit()
	
if(len(output) > 1):
	mopp = int(output[-3:])
else:
	mopp = int(output)

if(mopp == 1):
	check_output(["php","inject_bsfadenode.php",path_output+"_temp",path_output+"_temp"])

	if(options.generateCollision == "mopp" and mopp == 1):
		check_output(["mopp_rl",path_output+"_temp",path_output]);
		
	if(options.generateCollision == "mopp_new" and mopp == 1):
	#	print(join([options.meshlabPath + "/meshlabserver.exe","-i \""+path_output+"_temp.obj\"","-o \""+path_output+"_temp_col.obj\"","-s merge.mlx","-om vc vq vn"]));
		
		check_output(["helper_meshlab.bat",options.meshlabPath+"/meshlabserver.exe",path_output+"_temp.obj",path_output+"_col.obj",path_output+"_temp.mlx"]);
		check_output(["mopp_rl",path_output+"_temp",path_output,path_output+"_col.obj"]);
		os.remove(path_output+"_col.obj")
		os.remove(path_output+"_temp.obj")
		os.remove(path_output+"_temp.mlx")
		
	if(options.generateCollision == "convex" or mopp == 2):
		call(["mopp_rl",path_output+"_temp",path_output,"convex"]);
		#os.renames(path_output+"_temp",path_output);
	
	if(options.generateCollision != "mopp" and options.generateCollision != "convex" and options.generateCollision != "mopp_new"):
		print("Unknown Collision generation method!")
		quit()
	
else:
	call(["php","inject_bsfadenode.php",path_output+"_temp",path_output])

if(os.path.isfile(path_output+"_temp.metadata")):
	if(os.path.isfile(path_output+".metadata")):
		os.remove(path_output+".metadata");
	
	os.renames(path_output+"_temp.metadata",path_output+".metadata");


os.remove(path_output+"_temp")
