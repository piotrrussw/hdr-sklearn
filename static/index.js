function onPaint(context, lastMouse, Mouse) {
  context.lineWidth = context.lineWidth;
  context.lineJoin = "round";
  context.lineCap = "round";
  context.strokeStyle = context.color;

  context.beginPath();
  context.moveTo(lastMouse.x, lastMouse.y);
  context.lineTo(Mouse.x, Mouse.y);
  context.closePath();
  context.stroke();
}

function clear(context, canvas, predictResult) {
  context.clearRect(0, 0, 280, 280);
  context.fillStyle = "white";
  context.fillRect(0, 0, canvas.width, canvas.height);
  predictResult.innerText = "";
}

function predict(canvas, predictResult) {
  const image = canvas.toDataURL("image/png");

  axios.post('/predict', image).then(({ data }) => {
    predictResult.innerText = data.prediction;
  });
}

(function() {
  const canvas = document.querySelector("#canvas");
  const clearButton = document.getElementById("clear");
  const predictButton = document.getElementById("predict");
  const predictResult = document.getElementById("result");
  const context = canvas.getContext("2d");
  const Mouse = { x: 0, y: 0 };
  const lastMouse = { x: 0, y: 0 };
  const paint = () => onPaint(context, lastMouse, Mouse);
  canvas.width = 256;
  canvas.height = 256;

  context.fillStyle = "white";
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.color = "black";
  context.lineWidth = 14;
  context.lineJoin = context.lineCap = "round";

  canvas.addEventListener(
    "mousemove",
    function(e) {
      lastMouse.x = Mouse.x;
      lastMouse.y = Mouse.y;

      Mouse.x = e.pageX - this.offsetLeft - 15;
      Mouse.y = e.pageY - this.offsetTop - 15;
    },
    false
  );

  canvas.addEventListener(
    "mousedown",
    function() {
      canvas.addEventListener("mousemove", paint, false);
    },
    false
  );

  canvas.addEventListener(
    "mouseup",
    function() {
      canvas.removeEventListener("mousemove", paint, false);
    },
    false
  );

  clearButton.addEventListener(
    "click",
    () => clear(context, canvas, predictResult),
    false
  );

  predictButton.addEventListener(
    "click",
    () => predict(canvas, predictResult),
    false
  );
})();