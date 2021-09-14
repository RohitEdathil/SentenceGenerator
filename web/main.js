const HOST = "https://sentence-generator-markov.herokuapp.com/";
var model;
function $(id) {
  return document.getElementById(id);
}

fetch(`${HOST}list_models`)
  .then((response) => response.json())
  .then((data) => gotAvailable(data));

function gotAvailable(data) {
  $("loading").style.display = "none";
  model = data.models[0];
  $("title").innerHTML = `<em>${model}</em>Simulator`;
  data.models.forEach((model) => {
    var ele = document.createElement("option");
    ele.value = model;
    ele.innerHTML = model;
    $("models-options").appendChild(ele);
  });
}

$("models").onchange = (e) => {
  model = $("models").value;
  $("title").innerHTML = `<em>${model}</em>Simulator`;
};

$("get-button").onclick = (e) => {
  $("out").innerHTML = "Loading";
  $("get-button").disabled = true;
  fetch(`${HOST}get/${model}`)
    .then((res) => res.text())
    .then((data) => {
      $("out").innerHTML = data.substring(1, data.length - 1);
      $("get-button").disabled = false;
    });
};
