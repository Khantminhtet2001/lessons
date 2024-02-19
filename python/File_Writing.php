<?php
$file = "Texxt.txt";
$h = fopen($file, 'w');
fwrite($h, "Hola my fris");
fclose($h); 
?>