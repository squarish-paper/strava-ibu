from flaskext.mysql import MySQL

#TODO: Error Handle this
mysql = MySQL()

def init(app):
    mysql.init_app(app)

def get_user(athlete_id):
    stmt = "SELECT `strava_id`, concat(firstname, ' ' ,lastname), UNIX_TIMESTAMP(lastLogon), `bearer`, `public` from athlete WHERE strava_id="+str(athlete_id)
    return select(stmt)

def auth_user(athlete):

    id = athlete['athlete']['id']
    user = get_user(id)
    if len(user) is 0:
        insert_user(athlete)
    else:
        update_user_auth(id, athlete['access_token'])

def insert_user(athlete):
    stmt = "INSERT INTO `athlete` (`strava_id`,`firstname`,`lastname`,`auth`,`bearer`,`public`) VALUES ('"+str(athlete['athlete']['id'])+"','"+str(athlete['athlete']['firstname'])+"','"+str( athlete['athlete']['lastname'])+"',NOW(),'"+str(athlete['access_token'])+"',true);"
    insert(stmt)

def update_last_logon(athlete_id):
    stmt = "UPDATE `athlete` SET `lastLogon`=NOW() WHERE `strava_id`='"+str(athlete_id)+"'"
    insert(stmt)

def update_user_auth(id, token):
    stmt = "UPDATE `athlete` SET `bearer`='"+token+"' WHERE `strava_id`='"+str(id)+"'"
    insert(stmt)

def add_athlete_activity_xref(athlete_id,activity_id):
    stmt = "INSERT INTO `activityXref` (`strava_id`,`activity_id`) VALUES ('" + str(athlete_id) + "','" + str(activity_id) +"');"
    insert(stmt)

def add_athlete_segment_xref(athlete_id,detailedSegment,leaderboard):
    first = leaderboard["entries"][0]["elapsed_time"]
    #TODO: if < 10 entries?
    tenth = leaderboard["entries"][9]["elapsed_time"]
    rank = 0
    if len(leaderboard["entries"]) > 10:
        rank = leaderboard["entries"][12]["rank"]

    stmt = "INSERT INTO `segmentXref` (`strava_id`,`segment_id`,`name`,`distance`,`activity_type`,`elevation`,`total_efforts`,`athlete_count`,`user_pr`,`user_efforts`,`first_place`,`tenth_place`,`rank`) VALUES ('" + str(athlete_id) + "','" + str(detailedSegment["id"]) +"','" + str(detailedSegment["name"]) +"','" + str(detailedSegment["distance"]) +"','" + str(detailedSegment["activity_type"]) +"','" + str(detailedSegment["total_elevation_gain"]) +"','" + str(detailedSegment["effort_count"]) +"','" + str(detailedSegment["athlete_count"]) +"','" + str(detailedSegment["athlete_segment_stats"]["pr_elapsed_time"]) +"','" + str(detailedSegment["athlete_segment_stats"]["effort_count"])  + "','"+str(first) +  "','"+str(tenth) + "','"+str(rank) + "');"
    insert(stmt)

def get_segments(athlete_id):
    stmt = "SELECT `activity_type`,`name`,`distance`,`elevation`,`user_efforts`,`user_pr`,`first_place`,`tenth_place`,`rank`,`athlete_count`,`total_efforts` from segmentXref WHERE strava_id="+str(athlete_id)
    return select(stmt)

def get_segment_xref(athlete_id,segment_id):
    stmt = "SELECT * from segmentXref WHERE strava_id="+str(athlete_id) + " AND segment_id="+str(segment_id)
    return select(stmt)

def select(stmt):
    print("[DATASTORE] | SELECT | " + stmt)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(stmt)
    return cursor.fetchall()

def insert(stmt):
    print("[DATASTORE] | INSERT | " + stmt)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(stmt)
    conn.commit()
