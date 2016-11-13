function getEpoch(type){
  var d = new Date(); 
  document.getElementById("epochTime").innerText = type + ' ' + String(d.getTime()-d.getMilliseconds()/1000)
};
