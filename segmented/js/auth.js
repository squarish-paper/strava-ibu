Auth = {
  authorise: function () {
    //var whereTo = "https://d11g903oyygnp2.cloudfront.net/auth.html"
    var whereTo = "http://localhost:8080/auth"
    var redirectUrl = 'https://www.strava.com/oauth/authorize?client_id=14681&response_type=code&redirect_uri='+whereTo+'&approval_prompt=force';
    window.location.href = redirectUrl;
  }
}
