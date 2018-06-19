function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

var self = this;
const requestURL = "http://127.0.0.1:5000/api/espeak";
let XHR = new XMLHttpRequest();
let FD  = new FormData();

// FD.append("text", "Bom dia, gente");

// XHR.open("POST", requestURL);
// XHR.send(FD);

// XHR.onreadystatechange = function() {
//   if (XHR.readyState === XMLHttpRequest.DONE) {
//     if (XHR.status === 200) {
//       const results = JSON.parse(XHR.responseText);
//       console.log(results);
//     }
//   }
// };

// console.log(durations.reduce((acc, val) => acc + val, 0));

let audio = document.querySelector("#audio");
let audioSource = document.querySelector("#audioSource");

let postDiv = document.querySelector("#post");
postDiv.style.display = "none";

let genBtn = document.querySelector("#generateBtn");

genBtn.addEventListener("click", function( event ) {
  const requestURL = "http://127.0.0.1:5000/api/gen_audio";

  let XHR = new XMLHttpRequest();
  let FD  = new FormData();

  XHR.open("GET", requestURL);
  XHR.send();

  XHR.onreadystatechange = function() {
    console.log("hmm");
    if (XHR.readyState === XMLHttpRequest.DONE) {
      if (XHR.status === 200) {
        const results = JSON.parse(XHR.responseText);
        console.log(results);
        console.log(results.token);
        audioSource.src = `http://127.0.0.1:5000/api/get_audio/${results.token}`;
        audio.load();
        postDiv.style.display = "block";
      }
    }
  };

}, false);
