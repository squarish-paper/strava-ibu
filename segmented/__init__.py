import requests
from . import datastore, api
from flask import Flask, render_template, json, request, send_from_directory,redirect

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
        code = request.args.get('code')
        state = request.args.get('state')
        athlete = api.oauth(code,state,app)

        #TODO: Error Handle this
        datastore.auth_user(athlete)
        return redirect('/dashboard/'+str(athlete['athlete']['id']))

    @app.route('/dashboard/<int:athlete_id>')
    def dashboard(athlete_id):
        # get user from MySQL
        data = datastore.get_user(athlete_id)

        # if user does not exist show error page
        if len(data) is 0:
            return render_template('connect.html')

        # if user does is not public, show private page
        if not(data[0][4]):
            return render_template('private.html')

        bearer = data[0][3]
        lastLogon = data[0][2]
        activities = api.get_athlete_activities(bearer,lastLogon,app)

        if len(activities) > 0:
            get_new_activities(bearer, activities, athlete_id)

        segments = datastore.get_segments(athlete_id)
        datastore.update_last_logon(athlete_id)

        return render_template('dashboard.html',segments=segments)

    def get_new_activities(bearer, activities, athlete_id):
        print("--- Fetching new activities")
        for activity in activities:
            print("---" + str(activity["name"]))
            activity_id = activity["id"]
            athlete_id = activity["athlete"]["id"]
            datastore.add_athlete_activity_xref(athlete_id,activity_id)

            detailedActivity = api.get_activity(bearer,activity_id,app)
            segments = detailedActivity["segment_efforts"]

            for segment in segments:
                segment_id = segment["segment"]["id"]
                segmentXref = datastore.get_segment_xref(athlete_id,segment_id)
                if len(segmentXref) is 0:
                    detailedSegment = api.get_segment(bearer,segment_id,app)
                    datastore.add_athlete_segment_xref(athlete_id,detailedSegment)

    return app
