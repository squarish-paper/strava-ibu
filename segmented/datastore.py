from flaskext.mysql import MySQL

#TODO: Error Handle this
mysql = MySQL()

def init(app):
    mysql.init_app(app)

def get_user(athlete_id):
    #try:
    # get user from MySQL
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "SELECT `strava_id`, concat(firstname, ' ' ,lastname), UNIX_TIMESTAMP(lastLogon), `bearer`, `public` from athlete WHERE strava_id="+str(athlete_id)
    print("[DATASTORE] GET | Athlete " + str(athlete_id))
    cursor.execute(stmt)

    data = cursor.fetchall()
    return data

def auth_user(athlete):

    id = athlete['athlete']['id']
    user = get_user(id)
    if len(user) is 0:
        insert_user(athlete)
    else:
        update_user_auth(id, athlete['access_token'])

def insert_user(athlete):
    id = athlete['athlete']['id']
    firstname = athlete['athlete']['firstname']
    lastname = athlete['athlete']['lastname']
    bearer = athlete['access_token']

    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "INSERT INTO `athlete` (`strava_id`,`firstname`,`lastname`,`auth`,`bearer`,`public`) VALUES ('"+str(id)+"','"+str(firstname)+"','"+str(lastname)+"',NOW(),'"+str(bearer)+"',true);"
    print("[DATASTORE] INSERT |  Athlete=" + str(id))
    cursor.execute(stmt)
    conn.commit()

def update_last_logon(athlete_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "UPDATE `athlete` SET `lastLogon`=NOW() WHERE `strava_id`='"+str(athlete_id)+"'"
    print("[DATASTORE] UPDATE | Last Logon")
    cursor.execute(stmt)
    conn.commit()

def update_user_auth(id, token):
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "UPDATE `athlete` SET `bearer`='"+token+"' WHERE `strava_id`='"+str(id)+"'"
    print("[DATASTORE] UPDATE | Auth")
    cursor.execute(stmt)
    conn.commit()

def add_athlete_activity_xref(athlete_id,activity_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "INSERT INTO `activityXref` (`strava_id`,`activity_id`) VALUES ('" + str(athlete_id) + "','" + str(activity_id) +"');"
    print("[DATASTORE] INSERT | activityXref Athlete=" + str(athlete_id) + ", Activity="+str(activity_id) )
    cursor.execute(stmt)
    conn.commit()

def add_athlete_segment_xref(athlete_id,detailedSegment):
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "INSERT INTO `segmentXref` (`strava_id`,`segment_id`,`name`,`distance`,`activity_type`,`elevation`,`total_efforts`,`athlete_count`,`user_pr`,`user_efforts`) VALUES ('" + str(athlete_id) + "','" + str(detailedSegment["id"]) +"','" + str(detailedSegment["name"]) +"','" + str(detailedSegment["distance"]) +"','" + str(detailedSegment["activity_type"]) +"','" + str(detailedSegment["total_elevation_gain"]) +"','" + str(detailedSegment["effort_count"]) +"','" + str(detailedSegment["athlete_count"]) +"','" + str(detailedSegment["athlete_segment_stats"]["pr_elapsed_time"]) +"','" + str(detailedSegment["athlete_segment_stats"]["effort_count"]) +"');"
    print("[DATASTORE] INSERT | segmentXref Athlete=" + str(athlete_id) + ", Segment="+str(detailedSegment["id"]) )
    cursor.execute(stmt)
    conn.commit()

def get_segments(athlete_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "SELECT `segment_id`,`name`,`distance`,`activity_type`,`elevation`,`total_efforts`,`athlete_count`,`user_pr`,`user_efforts` from segmentXref WHERE strava_id="+str(athlete_id)
    print("[DATASTORE] GET | Segments for Athlete " + str(athlete_id))
    cursor.execute(stmt)
    data = cursor.fetchall()
    return data

def get_segment_xref(athlete_id,segment_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    stmt = "SELECT * from segmentXref WHERE strava_id="+str(athlete_id) + " AND segment_id="+str(segment_id)
    print("[DATASTORE] GET | segmentXref: Athlete=" + str(athlete_id) + ", Segment="+str(segment_id) )
    cursor.execute(stmt)
    data = cursor.fetchall()
    return data
