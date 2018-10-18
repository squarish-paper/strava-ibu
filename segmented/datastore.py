from flaskext.mysql import MySQL

mysql = MySQL()

def init(app):
    mysql.init_app(app)

def get_user(athlete_id):
    #try:
    # get user from MySQL
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from athlete WHERE user_id="+str(athlete_id))

    data = cursor.fetchall()
    print(data)
#    except Exception as e:
#        print(str(e))
#   finally:
#    cursor.close()
#        conn.close()

    return data
