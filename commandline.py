

import os
import sys
import time
from optparse import OptionParser

def create():
	usage = "usage: %prog [options] arg"
	parserx = OptionParser(usage)
	parserx.add_option("-s", "--shaderPreset", dest="shaderPreset",
					  help="Shader preset to use in BSLightingShaderProperties, available: plants,signs,default",default="default")
	parserx.add_option("-c", "--generateCollision", dest="generateCollision",
					  help="Port over collision - available: convex,mopp,mopp_new",default="mopp")
	parserx.add_option("-t", "--updateTangents", dest="updateTangents",
					  help="Update Tangent Space - Will use optimize geometry, so be careful!",default="0")
	parserx.add_option("-u", "--usedScript", dest="usedScript",
					  help="The script used, default to convert_mesh which is for oblivion mesh upgrading.",default="convert_mesh")					  
	parserx.add_option("-p", "--meshlabPath", dest="meshlabPath",
					  help="Your Meshlab path ( used for simplified mopp collision generation )",default="C:/Programy/Meshlab")					  
							  
	return parserx.parse_args();