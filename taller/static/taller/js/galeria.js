
function verImagen(urlImagen) {
  var imagenPopup = document.getElementById("imagen-completa");
  imagenPopup.src = urlImagen;
  document.querySelector('.imagen-trabajo').style.display = "block";
}

window.onclick = function (event) {
  var trabajo = document.querySelector('.imagen-trabajo');
  if (event.target == trabajo) {
    trabajo.style.display = "none";
  }
}
