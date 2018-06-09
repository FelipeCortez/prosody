var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
});

const requestURL = "127.0.0.1:5000/api/espeak";

httpRequest = new XMLHttpRequest();
httpRequest.open("GET", requestURL);
httpRequest.send();

httpRequest.onreadystatechange = function() {
  if (httpRequest.readyState === XMLHttpRequest.DONE) {
    if (httpRequest.status === 200) {
      const results = JSON.parse(httpRequest.responseText);
      console.log(results);
    }
  }
}
