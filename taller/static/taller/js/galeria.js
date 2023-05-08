const trabajo = document.querySelector('.imagen-trabajo');

function verImagen(){
    trabajo.style.display = "block";
}
window.onclick = function(event) {
    if (event.target == trabajo) {
      trabajo.style.display = "none";
    }
  }