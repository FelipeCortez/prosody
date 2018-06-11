function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

var app = new Vue({
  el: '#app',
  data: {
    phones: []
  },
  mounted: function() {
    var self = this;
    const requestURL = "http://127.0.0.1:5000/api/espeak";
    let XHR = new XMLHttpRequest();
    let FD  = new FormData();

    FD.append("text", "Bom dia, comunidade");

    XHR.open("POST", requestURL);
    XHR.send(FD);

    XHR.onreadystatechange = function() {
      if (XHR.readyState === XMLHttpRequest.DONE) {
        if (XHR.status === 200) {
          const results = JSON.parse(XHR.responseText);
          console.log(results);
          self.phones = results;
        }
      }
    };
  },
  computed: {
    firstPhone: function () {
      return `${getRandomInt(99)}%`;
    }
  }
});


