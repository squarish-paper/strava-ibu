import requests
from . import datastore
from flask import Flask, render_template, json, request, send_from_directory

def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)
    datastore.init(app)

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
        # get user from MySQL
        data = datastore.get_user(athlete_id)
        # if no athlete error
        if len(data) is 0:
            return render_template('connect.html')
        else:
            #url = "https://www.strava.com/api/v3/athlete/activities"
            #headers = {'Authorization': 'Bearer 28fb470866dbe165f358b66aa1f5198b9059cd0b'}
            #r = requests.get(url, headers=headers)
            return render_template('dashboard.html',activities=json.dumps([]))

    return app
