<?php
    echo "STRAVA DATA VIEWER";

    include('config.php');
    
	// create curl resource 
    $ch = curl_init(); 
    
    // curl strava 
    curl_setopt($ch, CURLOPT_URL, $url); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 

    // $output contains the output string 
    $output = curl_exec($ch); 

    // close curl resource to free up system resources 
    curl_close($ch); 


    // spew onto page
	echo "<br />start<br/>";
   	echo $output;	
	echo "<br />end";
        
?>
