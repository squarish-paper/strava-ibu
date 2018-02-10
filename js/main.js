
    var allSegments = [];
    var athleteName = "";

    function callStrava() {
    var segMap = [];
    var url = "https://www.strava.com/api/v3/athletes/15535211";
    if (localStorage.athlete == null) {
      apiCall(url, drawAthlete);
    } else {
      drawAthlete(JSON.parse(localStorage.athlete));
    }

};

function drawAthlete(athlete) {
  //locally store athlete
  if (localStorage.athlete == null) {
    localStorage.athlete = JSON.stringify(athlete);
  }

  document.getElementById("user").innerHTML = athlete.username;
  athleteName = athlete.firstname + " " + athlete.lastname.substring(0,1) + ".";
  console.log(athleteName);

  if (localStorage.activities == null) {
    var url = "https://www.strava.com/api/v3/athlete/activities";
    apiCall(url, drawActivities);
  } else {
    drawActivities(JSON.parse(localStorage.activities));
  }
};

function drawActivities(activities) {
  //locally store activities
  if (localStorage.activities == null) {
    localStorage.activities = JSON.stringify(activities);
  }

  var activityCount = activities.length;
  document.getElementById("recentStuff").innerHTML = "Fetched the most recent " +activities.length+ " activities";
  for (var i = 0; i < activities.length; i++) {
//  for (var i = 0; i < 3; i++) {

    if (localStorage.getItem("activity"+activities[i].id) == null) {
      var url = "https://www.strava.com/api/v3/activities/" + activities[i].id;
       apiCall(url, drawActivity);
    } else {
      drawActivity(JSON.parse(localStorage.getItem("activity"+activities[i].id)));
    }
  }

};

function drawActivity(activity) {
  if (localStorage.getItem("activity"+activity.id) == null) {
    localStorage.setItem("activity"+activity.id, JSON.stringify(activity));
  }
//console.log(activity);
  for (var j = 0; j < activity.segment_efforts.length; j++) {
    var segmentEffort = activity.segment_efforts[j];
    if (allSegments.indexOf(segmentEffort.segment.id) > 0) {
      updateSegment(segmentEffort);
    } else {
      allSegments.push(segmentEffort.segment.id);
      buildSegment(segmentEffort);
    }
    $("#tableSegments").trigger("update");

  }
};

function drawSegment(leaderboard, segmentEffort) {

  if (localStorage.getItem("leaderboard"+segmentEffort.segment.id) == null) {
    localStorage.setItem("leaderboard"+segmentEffort.segment.id, JSON.stringify(leaderboard));
  }

   var leaderboardCount = leaderboard.entries.length;
   var position = 0;
   if (leaderboardCount > 10) {
    position = leaderboard.entries[leaderboardCount-3].rank;
  } else {
    for (var l = 1; l < leaderboardCount; l++) {
      if (leaderboard.entries[l].athlete_name == athleteName) {
        position = leaderboard.entries[l].rank;
        l = leaderboard;
      }

    }
  };

  var timeOffTop = segmentEffort.elapsed_time - leaderboard.entries[1].elapsed_time;
  var timeOfftenth = segmentEffort.elapsed_time - leaderboard.entries[9].elapsed_time;
  document.getElementById("segTime"+segmentEffort.segment.id).innerText = segmentEffort.elapsed_time;
  document.getElementById("segRank"+segmentEffort.segment.id).innerText = position + "/" + leaderboard.entry_count;
  document.getElementById("segCR"+segmentEffort.segment.id).innerText = leaderboard.entries[1].elapsed_time;
  document.getElementById("segCRDiff"+segmentEffort.segment.id).innerText = "+" + timeOffTop;
  document.getElementById("segTop"+segmentEffort.segment.id).innerText = leaderboard.entries[9].elapsed_time;
  document.getElementById("segTopDiff"+segmentEffort.segment.id).innerText = "+" + timeOfftenth;

  $("#tableSegments").trigger("update");

};

function buildSegment(segmentEffort) {

  var row = document.createElement('tr');
  row.id  = "segment"+segmentEffort.segment.id;

  var td= document.createElement('td');
  var a = document.createElement('a');
  a.href = "https://www.strava.com/segments/"+segmentEffort.segment.id;
  a.text = segmentEffort.segment.name;
  td.appendChild(a);
  row.appendChild(td);

  row.appendChild(newTd(segmentEffort.segment.distance, null));
  row.appendChild(newTd("1","segCount"+segmentEffort.segment.id));
  row.appendChild(newTd("", "segRank"+segmentEffort.segment.id));
  row.appendChild(newTd("", "segTime"+segmentEffort.segment.id));
  row.appendChild(newTd("", "segCR"+segmentEffort.segment.id));
  row.appendChild(newTd("", "segCRDiff"+segmentEffort.segment.id));
  row.appendChild(newTd("", "segTop"+segmentEffort.segment.id));
  row.appendChild(newTd("", "segTopDiff"+segmentEffort.segment.id));
  document.getElementById("tableRows").appendChild(row);





  if (localStorage.getItem("leaderboard"+segmentEffort.segment.id) == null) {
    var url = "https://www.strava.com/api/v3/segments/" +segmentEffort.segment.id + "/leaderboard";
    apiCall(url, drawSegment, segmentEffort);
  } else {
    drawActivity(JSON.parse(localStorage.getItem("leaderboard"+segmentEffort.segment.id)));
  }

};

function updateSegment(segmentEffort) {
  var oldCount = document.getElementById("segCount"+segmentEffort.segment.id).innerText;
  document.getElementById("segCount"+segmentEffort.segment.id).innerText = parseInt(oldCount)+1;

  var oldTime = document.getElementById("segTime"+segmentEffort.segment.id).innerText;

  if (oldTime > segmentEffort.elapsed_time) {
    document.getElementById("segTime"+segmentEffort.segment.id).innerText = parseInt(segmentEffort.elapsed_time);
  }
};

function newTd(data,id) {
  var td = document.createElement('td');
  td.innerText =  data;
  if (id != null) {
    td.id = id;
  }
  return td;
}
