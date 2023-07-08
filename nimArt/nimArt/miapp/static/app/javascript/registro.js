// Ejecutando funciones
window.addEventListener("resize", anchoPage);

// Declarando variables
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");
var contenedor_login_register = document.querySelector(".contenedor__login-register");
var caja_trasera_register = document.querySelector(".caja__trasera-register");

// Función para ajustar el diseño de la página según el ancho
function anchoPage() {
  if (window.innerWidth > 850) {
    formulario_register.style.display = "block";
    contenedor_login_register.style.left = "410px";
    caja_trasera_register.style.display = "block";
    formulario_login.style.display = "none";
  } else {
    formulario_register.style.display = "block";
    contenedor_login_register.style.left = "0px";
    caja_trasera_register.style.display = "none";
    formulario_login.style.display = "none";
  }
}

// Llamar a la función para ajustar el diseño al cargar la página
anchoPage();

// Función para mostrar el formulario de registro
function register() {
  if (window.innerWidth > 850) {
    formulario_register.style.display = "block";
    contenedor_login_register.style.left = "410px";
    caja_trasera_register.style.opacity = "0";
  } else {
    formulario_register.style.display = "block";
    contenedor_login_register.style.left = "0px";
    caja_trasera_register.style.display = "none";
    caja_trasera_register.style.opacity = "1";
  }
}


// Función para validar el formulario de registro
function validacionesExitosas() {
  var nombreRegExp = /^[A-Za-z\s]+$/;
  var emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  var nombreValido = nombreRegExp.test(rnombre.value);
  var emailValido = emailRegExp.test(remail.value);
  var usuarioValidado = ruser.value.trim() !== "";
  var passwordValido = rpassword.value.trim() !== "";

  return nombreValido && emailValido && usuarioValidado && passwordValido;
}

// Obtener los valores de los inputs
var rnombre = document.getElementById("rnombre");
var remail = document.getElementById("remail");
var ruser = document.getElementById("ruser");
var rpassword = document.getElementById("rpassword");
var formregistro = document.getElementById("formregistro");

formregistro.addEventListener("submit", function (e) {
  // Validar el nombre (solo letras y espacios)
  var nombreRegExp = /^[A-Za-z\s]+$/;
  if (!nombreRegExp.test(rnombre.value)) {
    e.preventDefault();
    document.getElementById("mensaje3").style.display = "block";
  } else {
    document.getElementById("mensaje3").style.display = "none";
  }

  // Función para validar el correo
  var emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegExp.test(remail.value)) {
    e.preventDefault();
    document.getElementById("mensaje4").style.display = "block";
  } else {
    document.getElementById("mensaje4").style.display = "none";
  }

  // Validar el usuario
  if (ruser.value.trim() === "") {
    e.preventDefault();
    document.getElementById("mensaje5").style.display = "block";
  } else {
    document.getElementById("mensaje5").style.display = "none";
  }

  // Validar la contraseña
  if (rpassword.value.trim() === "") {
    e.preventDefault();
    document.getElementById("mensaje6").style.display = "block";
  } else {
    document.getElementById("mensaje6").style.display = "none";
  }

  // Validar el formulario
  if (validacionesExitosas()) {
    // Mostrar alerta de envío exitoso
    Swal.fire({
      icon: 'success',
      title: 'Registrado',
      text: 'Datos ingresados correctamente',
      showConfirmButton: false,
    }).then(function() {
      // Limpiar los campos del formulario
      rnombre.value = "";
      remail.value = "";
      ruser.value = "";
      rpassword.value = "";
      // Enviar el formulario manualmente
      formregistro.submit();
    });
  } else {
    e.preventDefault(); // Evitar que el formulario se envíe si hay errores
  }
});
