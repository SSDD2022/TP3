//para ver imagen completa de la tarjeta
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

// Para visualizar los datos del autor
var descripcionAutor = document.getElementById('descripcion-autor');
var nombresAutores = document.getElementsByClassName('alumno');

for (var i = 0; i < nombresAutores.length; i++) {
  nombresAutores[i].addEventListener('mouseover', mostrarDatosAlumno);
  nombresAutores[i].addEventListener('mouseout', ocultarDatosAlumno);
}

// Función para mostrar los datos del autor
function mostrarDatosAlumno(event) {
  var nombre = event.target.getAttribute('data-nombre');
  var apellido = event.target.getAttribute('data-apellido');
  var fechaNacimiento = event.target.getAttribute('data-fecha-nacimiento');
  
  descripcionAutor.innerHTML = '<p>Nombre: ' + nombre + '</p>' +
                               '<p>Apellido: ' + apellido + '</p>' +
                               '<p>Fecha de Nacimiento: ' + fechaNacimiento + '</p>';
  
  descripcionAutor.style.position = 'fixed';
  descripcionAutor.style.left = (event.clientX + 10) + 'px';
  descripcionAutor.style.top = (event.clientY + 10) + 'px';
  descripcionAutor.style.display = 'block';
}

// Función para ocultar los datos del alumno
function ocultarDatosAlumno() {
  descripcionAutor.style.display = 'none';
}