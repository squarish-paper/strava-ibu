import requests
from flask import Flask, render_template, json, request, send_from_directory
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

def create_app(config, debug=False, testing=False, config_overrides=None):
    mysql = MySQL()
    app = Flask(__name__)

    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = '172.19.0.2'
    mysql.init_app(app)

    app = Flask(__name__)

    @app.route('/')
    def main():
        return render_template('index.html')

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('js', path)

    @app.route('/css/<path:path>')
    def send_css(path):
        return send_from_directory('css', path)

    @app.route('/img/<path:path>')
    def send_image(path):
        return send_from_directory('img', path)

    @app.route('/auth')
    def auth():
        return render_template('auth.html')

    @app.route('/dashboard/<int:athlete_id>')
    def dashboard(athlete_id):
        try:
            # get user from MySQL
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * from athlete WHERE user_id="+str(athlete_id))
            data = cursor.fetchall()

            # if no athlete error
            if len(data) is 0:
                return render_template('connect.html')
            else:
                url = "https://www.strava.com/api/v3/athlete/activities"
                headers = {'Authorization': 'Bearer 28fb470866dbe165f358b66aa1f5198b9059cd0b'}
                r = requests.get(url, headers=headers)
                return render_template('dashboard.html',activities=r.json())

        except Exception as e:
            return json.dumps({'page error':str(e)})
        finally:
            cursor.close()
            conn.close()


    return app
