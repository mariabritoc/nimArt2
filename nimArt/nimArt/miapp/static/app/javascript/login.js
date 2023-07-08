// Ejecutando funciones
window.addEventListener("resize", anchoPage);

// Declarando variables
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");
var contenedor_login_register = document.querySelector(".contenedor__login-register");
var caja_trasera_register = document.querySelector(".caja__trasera-register");
var caja_trasera_login = document.querySelector(".caja__trasera-login");

// Función para ajustar el diseño de la página según el ancho
function anchoPage() {
  if (window.innerWidth > 850) {
    formulario_login.style.display = "block";
    contenedor_login_register.style.left = "10px";
    caja_trasera_register.style.display = "block";
    caja_trasera_login.style.display = "block";
    formulario_login.style.display = "block";
  } else {
    formulario_login.style.display = "block";
    contenedor_login_register.style.left = "0px";
    caja_trasera_register.style.display = "block";
    caja_trasera_login.style.display = "none";
    formulario_register.style.display = "none";
  }
}

// Llamar a la función para ajustar el diseño al cargar la página
anchoPage();

// Función para mostrar el formulario de registro
function login() {
  if (window.innerWidth > 850) {
    formulario_login.style.display = "block";
    contenedor_login_register.style.left = "10px";
    caja_trasera_register.style.opacity = "0";
  } else {
    formulario_login.style.display = "block";
    contenedor_login_register.style.left = "0px";
    caja_trasera_register.style.display = "block";
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

// Función para validar el formulario de inicio de sesión
function validacionesExitosas2() {
  var emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var email2Valido = emailRegExp.test(lemail.value);
  var passwordValido2 = lpassword.value.trim() !== "";

  return email2Valido && passwordValido2;
}


// Variables para validaciones del inicio de sesión
var lemail = document.getElementById("lemail");
var lpassword = document.getElementById("lpassword");
var formlogin = document.getElementById("formlogin");

formlogin.addEventListener("submit", function (e) {
  // Función para validar el correo
  var emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegExp.test(lemail.value)) {
    e.preventDefault();
    document.getElementById("mensaje1").style.display = "block";
  } else {
    document.getElementById("mensaje1").style.display = "none";
  }

  // Validar la contraseña
  if (lpassword.value.trim() === "") {
    e.preventDefault();
    document.getElementById("mensaje2").style.display = "block";
  } else {
    document.getElementById("mensaje2").style.display = "none";
  }

  if (validacionesExitosas2()) {
    
    // Mostrar alerta de envío exitoso
    Swal.fire({
      icon: 'success',
      title: 'Bienvenido',
      text: 'Datos ingresados correctamente',
      showConfirmButton: false,
    }).then(function() {
      // Limpiar los campos del formulario
      lemail.value = "";
      lpassword.value = "";
      // Enviar el formulario manualmente
      formlogin.submit();
    });
  } else {
    e.preventDefault(); // Evitar que el formulario se envíe si hay errores
  }
});
