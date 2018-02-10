function post() {
      console.log("api.post called");
    };


function apiCall(url, handler) {
  $.ajax({
      method: "GET",
      headers: {
        'Authorization': 'Bearer '+localStorage.access_token
      },
      url: url,
      success: function(data) {
          handler(data);
      }
  });
};
function apiCall(url, handler, params) {
  console.log("CALLING API! " + url)
  $.ajax({
      method: "GET",
      headers: {
        'Authorization': 'Bearer 28fb470866dbe165f358b66aa1f5198b9059cd0b'
      },
      url: url,
      success: function(data) {
          handler(data, params);
      }
  });
};
