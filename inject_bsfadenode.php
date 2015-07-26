<?php
$f = file_get_contents($_SERVER['argv'][1]);
$originalsize = ord($f[62]);
$f[62] = chr($originalsize + 1);
$pointer = 64;

for($i = 1; $i <= $originalsize; $i++){
$size = ord($f[$pointer]);
$pointer += $size + 4;
}

$datatext = substr($f,64,$pointer-64);
$f[$pointer] = chr($originalsize);
$f = str_replace($datatext,$datatext.chr(10).chr(0).chr(0).chr(0)."BSFadeNode",$f);
file_put_contents($_SERVER['argv'][2],$f);

