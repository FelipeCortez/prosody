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

let textBox = document.querySelector("#textBox");

let audio = document.querySelector("#audio");
let audioSource = document.querySelector("#audioSource");

let postDiv = document.querySelector("#post");
postDiv.style.display = "none";

let genBtn = document.querySelector("#generateBtn");

let drawArea = document.querySelector("#drawArea");

genBtn.addEventListener("click", function( event ) {
  while (drawArea.firstChild) {
    drawArea.removeChild(drawArea.firstChild);
  }

  console.log(textBox.value);
  const requestURL = "http://127.0.0.1:5000/api/gen_audio";

  let XHR = new XMLHttpRequest();
  let FD  = new FormData();
  FD.append("text", textBox.value);

  XHR.open("POST", requestURL);
  XHR.send(FD);

  XHR.onreadystatechange = function() {
    if (XHR.readyState === XMLHttpRequest.DONE) {
      if (XHR.status === 200) {
        const results = JSON.parse(XHR.responseText);
        console.log(results);
        console.log(results.token);

        let curLen = 0;
        let height = 250;

        for (let phone of results.sentence) {
          console.log(phone);
          let txtX = curLen + (phone.duration / 2);

          var svgns = "http://www.w3.org/2000/svg";
          var rect = document.createElementNS(svgns, 'rect');
          rect.setAttributeNS(null, 'x', curLen + phone.duration);
          rect.setAttributeNS(null, 'y', 0);
          rect.setAttributeNS(null, 'height', height);
          rect.setAttributeNS(null, 'width', '2');
          rect.setAttributeNS(null, 'fill', '#CCCCCC');
          drawArea.appendChild(rect);

          var circ = document.createElementNS(svgns, 'circle');
          var cx = curLen + ((phone.pitch_changes[0][0] / 100.0) * phone.duration);
          circ.setAttributeNS(null, 'cx', cx);
          circ.setAttributeNS(null, 'cy', height - phone.pitch_changes[0][1]);
          circ.setAttributeNS(null, 'r', 5);
          circ.setAttributeNS(null, 'fill', '#777777');
          circ.setAttributeNS(null, 'class', "dot");
          drawArea.appendChild(circ);

          var text = document.createElementNS(svgns, 'text');
          var tx = curLen + (phone.duration / 2);
          text.setAttributeNS(null, 'x', cx);
          text.setAttributeNS(null, 'y', 20);
          text.setAttributeNS(null, 'text-anchor', "middle");
          text.setAttributeNS(null, 'style', "font: 14px sans-serif");
          text.setAttributeNS(null, 'fill', '#777777');
          text.textContent = phone.phone_mbrola;
          drawArea.appendChild(text);

          curLen += phone.duration;
        }
        console.log(curLen);
        drawArea.setAttribute("width", `${curLen}px`);

        audioSource.src = `http://127.0.0.1:5000/api/get_audio/${results.token}`;
        audio.load();
        postDiv.style.display = "block";
      }
    }
  };

}, false);
