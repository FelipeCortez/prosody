function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

var app = new Vue({
  el: '#app',
  data: {
    phones: [],
    height: 300
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
          self.phones = results;
        }
      }
    };
  },
  computed: {
    totalDuration: function() {
      let durations = this.phones.map((phone) => phone.duration);
      console.log(durations.reduce((acc, val) => acc + val, 0));
      return durations.reduce((acc, val) => acc + val, 0);
    }
  }
});


