from flaskext.mysql import MySQL

mysql = MySQL()

def init(app):
    mysql.init_app(app)

def get_user(athlete_id):
    #try:
    # get user from MySQL
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from athlete WHERE strava_id="+str(athlete_id))

    data = cursor.fetchall()
    print(data)
#    except Exception as e:
#        print(str(e))
#   finally:
#    cursor.close()
#        conn.close()

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
    print("--about to insert")
    cursor.execute("INSERT INTO `athlete` (`strava_id`,`firstname`,`lastname`,`auth`,`lastLogon`,`bearer`,`public`) VALUES ('"+str(id)+"','"+str(firstname)+"','"+str(lastname)+"',NOW(),NOW(),'"+str(bearer)+"',true);")
    conn.commit()
    print("--done to insert")

def update_user_auth(id, token):
    conn = mysql.connect()
    cursor = conn.cursor()
    print("--about to update")
    cursor.execute("UPDATE `athlete` SET `bearer`='"+token+"' WHERE `strava_id`='"+str(id)+"'")
    conn.commit()
    print("--done to update")
