var app = new Vue({
  el: '#app',
  data: {
    phones: []
  },
  mounted: function() {
    var self = this;
    const requestURL = "http://127.0.0.1:5000/api/espeak";
    httpRequest = new XMLHttpRequest();
    httpRequest.open("GET", requestURL);
    httpRequest.send();

    httpRequest.onreadystatechange = function() {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
          const results = JSON.parse(httpRequest.responseText);
          console.log(results);
          self.phones = results;
        }
      }
    };
  }
});


