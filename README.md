#Skyblivion -  NIFConverter

This script allows for converting Oblivion-compatible NIFs to Skyrim-compatible NIFs. It was used for projects: Skyblivion, Skywind, Andoran Project, Silgrad Tower and saved countless hours of work.

It's a pretty old and rusty solution, but as it has proven to be quite useful before, it might just work for you :)

Requirements:

* Python 3.3~
* PyFFI ( available at http://pyffi.sourceforge.net/ )
* Any PHP 5+ ( probably will be dropped as PHP scripts don't do real work anyways )

Usage:
        python convert_folder.py <inputfolder> <outputfolder>
		
The script supports a few parameters, namely:

* -s ( "Conversion Preset" ) - Allows for choosing between a few conversion presets, which will make converter act a bit differently on the mesh. Current options are:
	* plants - Will use different shader presets to allow proper plants rendering
	* signs - Becuase of reasons unknown, moving signs in oblivion have very big inertia values, so they are lowered accordingly to be able to even move the signs
	* default - No additional actions
	
* -t ( "Update tangent space") - Will update tangets & bitangents and also run OptimizeGeometry spell from NifToaster
	
* -c ( "Collision handling mode") - Allows for choosing conversion handling mode. Available options are:
	* mopp - The default one. When encountering standard PackedNiTriStripsShape collision, it will be converted to MOPP standard skyrim collision object using the built-in MOPP_RL tool.
	* mopp_new - Experimental collision generator, useful if you don't have any collision on the mesh. Requires Meshlab server ( available at http://meshlab.sourceforge.net/ ) to be installed and provided using -p argument. It will export whole mesh as a set of vertices and triangles in Meshlab-compatible format, use decimation algorithms from Meshlab and import decimated mesh as a collision.
	* none - Will drop the collisions from the mesh.
	* convex - ( Deprecated ), will try to generate a convex shape collision using the MOPP_RL tool.
	
All converted meshes will point to textures within a ,,tes4" folder, so when moving textures to Skyrim, remember to put them within a new ,,tes4" subfolder, not in the root.	

#Worldspace conversions

Sometimes, because of technical constraints, there is a need of executing additional scripts on the game worldspace itself. This is the case with the furniture only for now ( which in-game doesn't support Z-translation, so we need to actually
move all the furniture up/down so the translation can be dropped from the mesh )

After script execution, there will be a file called ,,worldspace.metadata". If it is not empty, apply TES5Edit script provided ( MetadataParser.pas ) on all objects which use meshes you converted. To do so, copy the .metadata
file to your TES5Edit scripts folder and then simply execute it.