function authorise() {

  //var whereTo = "https://d11g903oyygnp2.cloudfront.net/auth.html"
  var whereTo = "http://localhost/auth.html"
  var redirectUrl = 'https://www.strava.com/oauth/authorize?client_id=14681&response_type=code&redirect_uri='+whereTo+'&approval_prompt=force';
  window.location.href = redirectUrl;
};

function handshake() {
  var url_string = window.location.href;
  var url = new URL(url_string);
  var code = url.searchParams.get("code");
  var state = url.searchParams.get("state");
  console.log(code);
  console.log(state);
  oauth(code);
};


function oauth(code) {
  var form = new FormData();
form.append("client_id", "14681");
form.append("client_secret", "11a7876f133ab52f30681e1b97e271153b18fa2f");
form.append("code", code);

var settings = {
  "async": false,
  "crossDomain": true,
  "url": "https://www.strava.com/oauth/token",
  "method": "POST",
  "processData": false,
  "contentType": false,
  "mimeType": "multipart/form-data",
  "data": form
}

$.ajax(settings).done(function (response) {
  var auth = JSON.parse(response);
  console.log(auth.athlete);
  localStorage.access_token = auth.access_token;
  localStorage.athlete = JSON.stringify(auth.athlete);
  window.location.href = "/test.html" ;
});




};
// REDIRECT TO

 // This will redirect to {REDIRECT_URL} with PARAMS ?state=&code=6af7bc8e833cab900f1232fd1ebc9b5b7afe0e15

 // You then need shake hands with this token (where the client ID and secret are set in the APP itself):
 // curl -X POST \
 // https://www.strava.com/oauth/token \
   // -F client_id=14681 \
   // -F client_secret=11a7876f133ab52f30681e1b97e271153b18fa2f \
   // -F code=19e674f02e5a3e567ca4296a4b9c71e625a99b1e

   // This will will respond with:
                     //     {
                     // "access_token": "28fb470866dbe165f358b66aa1f5198b9059cd0b",
                     // "token_type": "Bearer",
                     // "athlete": {
                     // "id": 15535211,
                     // "username": "matthew_startin",
                     // "resource_state": 2,
                     // "firstname": "Matthew",
                     // "lastname": "Startin",
                     // "city": "",
                     // "state": "",
                     // "country": null,
                     // "sex": "M",
                     // "premium": true,
                     // "created_at": "2016-05-31T14:57:20Z",
                     // "updated_at": "2018-01-13T18:00:17Z",
                     // "badge_type_id": 1,
                     // "profile_medium": "https://graph.facebook.com/10100790023620364/picture?height=256&width=256",
                     // "profile": "https://graph.facebook.com/10100790023620364/picture?height=256&width=256",
                     // "friend": null,
                     // "follower": null,
                     // "email": "m.j.startin@googlemail.com"
                     // }
                     // }


       // And the access_token is what is needed in the app. done
