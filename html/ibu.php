<html>
<head>
    <script src="js/jquery-3.1.1.min.js" type="text/javascript"></script>
    <!-- script src="js/bootstrap.js" type="text/javascript"></script -->

    <!-- flipclock -->
    <link rel="stylesheet" href="/assets/css/flipclock.css">
    <script src="/assets/js/flipclock/flipclock.min.js"></script>

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    
    <!-- custom stuff -->
    <script src="js/main.js" type="text/javascript"></script>
    <link rel="stylesheet" href="css/styles.css" type="text/css">
    
    <?php include('config.php'); ?>
    <?php include('activities.php'); ?>

</head>
<body class="deep-purple lighten-2">

    <div class="brown darken-4 header">
        <div>Strava Data Explorer</div>
    </div>
        
    <div class="brown darken-2 menu">
        <div class="row">
            <div class="col s4 center-align">
                <a href="#" onclick="getEpoch('Week'); return false;">Week</a>
            </div>
            <div class="col s4 center-align">
                <a href="#" onclick="getEpoch('Month'); return false;">Month</a>
            </div>
            <div class="col s4 center-align">
                <a href="#" onclick="getEpoch('Year'); return false;">Year</a>
            </div>
        </div>    
        <div id="epochTime"></div>
    </div>

    <?php #echo $activityCount  ?>

    <div class="data-section purple lighten-4">
        <div class="row">
            <div class="col s6">
                <div>Distance</div>
            </div>
            <div class="col s6">
                <div class="stat"><?php echo $totalDistance ?></div>
                <div class="measure">miles</div>
            </div>       
        </div>
    </div>
    <div class="data-section yellow lighten-4">
        <div class="row">
            <div class="col s6">
                <div class="your-clock"></div>
                <div class="stat"><?php echo $totalTime  ?></div>
                <div class="measure">hours</div>
            </div>
            <div class="col s6">
                <div>Time</div>
            </div>       
        </div>
    </div>
    <div class="data-section purple lighten-4 ">
        <div class="row">
            <div class="col s6 valign-wrapper">
                <div>Climb</div>
            </div>
            <div class="col s6 valign-wrapper">
                <div class="stat valign"><?php echo $totalClimb  ?></div>
                <div class="measure">metres</div>
            </div>       
        </div>
    </div>
    <div class="data-section yellow lighten-4">
        <div class="row">
            <div class="col s6">
                <div class="stat"><?php echo $maxSpeed  ?></div>
                <div class="measure">mph</div>
            </div>
            <div class="col s6">
                <div>Max Speed</div>
            </div>       
        </div>
    </div> 


    <footer class="brown darken-4 footer">
        footer
    </footer>

</body>
</html>