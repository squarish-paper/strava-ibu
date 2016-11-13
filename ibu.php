<html>
<body>
<link rel="stylesheet" href="css/styles.css" type="text/css">
<h1>Strava Data Explorer</h1>

<script type="text/javascript">

    function getEpoch(type){
      var d = new Date(); 
      document.getElementById("epochTime").innerText = type + ' ' + String(d.getTime()-d.getMilliseconds()/1000)
}

</script>
<a href="#" onclick="getEpoch('Week'); return false;">Week</a>
<a href="#" onclick="getEpoch('Month'); return false;">Month</a>
<a href="#" onclick="getEpoch('Year'); return false;">Year</a>
<div id="epochTime"></div>

<?php
    // includes
    include('config.php');

	// curl strava 
    $ch = curl_init(); 
    curl_setopt($ch, CURLOPT_URL, $url); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
    $rawData = curl_exec($ch); 
    curl_close($ch); 


    // loop round data to get information
	$activities = json_decode($rawData, true);
    
    $totalDistance = 0;
    $totalTime = 0;
    $totalClimb = 0;
    $activityCount = 0;
    $maxSpeed = 0;
    foreach($activities as $activity) {
        $activityCount += 1;
        //echo "<br />" ;
        //echo $activity["name"] . " - " . $activity["distance"] / 1603.34 . "|" . $activity["moving_time"] / 3600 . "|" . $activity["total_elevation_gain"] . "|" . $activity["average_speed"]/ 0.44704  . "|" . $activity["max_speed"];
        $totalDistance += $activity["distance"];
        $totalTime += $activity["moving_time"];
        $totalClimb += $activity["total_elevation_gain"];
        if ($activity["max_speed"] > $maxSpeed)
            $maxSpeed = $activity["max_speed"];

    }
    $averageSpeed = $totalDistance / $totalTime;
    echo "<br />" ;
    echo "<br />" ;
    echo "<br />" ;
    echo "TOTAL DISTANCE: " . $totalDistance / 1609.34 ." miles<br />";
    echo "TOTAL TIME    : " . $totalTime / 3600 ."hours <br />";
    echo "AVERAGE SPEED : " . $averageSpeed / 0.44704 ."mph<br />";
    echo "MAX SPEED     : " . $maxSpeed  ."mph<br />";
    echo "TOTAL CLIMB   : " . $totalClimb . "metres<br />";
        
?>
</body>
</html>