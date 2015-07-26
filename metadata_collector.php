<?php
ini_set("memory_limit","512M");
$dir = $_SERVER['argv'][1];
$metadatas = array();
sleep(3); //Safety to avoid race condition in python.

$f = fopen($dir.'\\worldspace.metadata','w+');
function scan_metadata($dir){
global $metadatas;
$dirz = scandir($dir);

	foreach($dirz as $directory){
	
		if($directory == '.' || $directory == '..')
			continue;
		
		if(is_dir($dir.'\\'.$directory))
			scan_metadata($dir.'\\'.$directory);
	
		if(preg_match("#(.*)\.metadata#",$directory,$matches))
		{
			
			$filename = $matches[1];

			if($filename == 'worldspace')
				continue;
			
			
			$d = file($dir.'\\'.$directory);
			if(empty($d[0])){
				unlink($dir.'\\'.$directory);
				continue;
			}
			
			if(isset($metadatas[$filename])){
			
				foreach($d as $command){
					$metadatas[$filename][] = $command;
				}
			
			}
			else
				$metadatas[$filename] = $d;
				
			unlink($dir.'\\'.$directory);
			
		}
	
	}

}

scan_metadata($dir);

$stringdata = array();
foreach($metadatas as $filename => $commands){

$stringdata[] = "[".$filename."]";

	foreach($commands as $command){
	
		$stringdata[] = $command;
	}

}

fwrite($f,implode('
',$stringdata));
fclose($f);