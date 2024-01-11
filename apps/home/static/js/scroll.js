// Mostrar u ocultar el botón dependiendo del scroll
window.addEventListener('scroll', function() {
  var botonFlotante = document.getElementById("botonFlotante");

  if (window.scrollY > 100) {
    botonFlotante.classList.add("mostrar");
  } else {
    botonFlotante.classList.remove("mostrar");
  }
});

// Función para desplazarse hacia arriba al hacer clic en el botón
document.getElementById('botonFlotante').addEventListener('click', function(e) {
  e.preventDefault(); // Evitar el comportamiento predeterminado del enlace
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});