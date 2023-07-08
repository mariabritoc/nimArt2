
// Función para validar todo lo obtenido
function validacionesExitosas() {
    var nombreRegExp = /^[A-Za-z\s]+$/;
    var emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var telefonoRegExp = /^\d{9}$/;
    
    var nombreValido = nombreRegExp.test(formNombre.value);
    var emailValido = emailRegExp.test(formEmail.value);
    var telefonoValido = telefonoRegExp.test(formMovil.value);
    var asuntoValido = formAsunto.value.trim() !== "";
    var mensajeValido = formMensaje.value.trim() !== "";
    
    return nombreValido && emailValido && telefonoValido && asuntoValido && mensajeValido;
  }


// Obtener lo el valor de los input
var formNombre = document.getElementById("formNombre");
var formEmail = document.getElementById("formEmail");
var formMovil = document.getElementById("formMovil");
var formAsunto = document.getElementById("formAsunto");
var formMensaje = document.getElementById("formMensaje");
var btnEnviar = document.getElementById("btnEnviar");

// Evento al apretar el boton enviar
btnEnviar.addEventListener("click", function(event) {


  // Validar el nombre (solo letras y espacios)
  var nombreRegExp = /^[A-Za-z\s]+$/;
  if (!nombreRegExp.test(formNombre.value)) {
    event.preventDefault(); // Evita que el formulario se envíe
    document.getElementById("mensaje1").style.display = "block"; //muestra el mesnaje error
  } else {
    document.getElementById("mensaje1").style.display = "none";  //oculta el mensaje error
  }
  
  // Validar el email
  var emailRegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegExp.test(formEmail.value)) {
    event.preventDefault();
    document.getElementById("mensaje2").style.display = "block";
  } else {
    document.getElementById("mensaje2").style.display = "none";
  }
  
  // Validar el número de teléfono
  var telefonoRegExp = /^\d{9}$/;
  if (!telefonoRegExp.test(formMovil.value)) {
    event.preventDefault();
    document.getElementById("mensaje3").style.display = "block";
  } else {
    document.getElementById("mensaje3").style.display = "none";
  }
  
  // Validar el asunto
  if (formAsunto.value.trim() === "") {
    event.preventDefault();
    document.getElementById("mensaje4").style.display = "block";
  } else {
    document.getElementById("mensaje4").style.display = "none";
  }
  
  // Validar el mensaje
  if (formMensaje.value.trim() === "") {
    event.preventDefault();
    document.getElementById("mensaje5").style.display = "block";
  } else {
    document.getElementById("mensaje5").style.display = "none";
  }

  // Validar el formulario
  if (validacionesExitosas()) {
    // Mostrar alerta de envío exitoso 
   // alert("enviado con exito");                   
   formNombre.value = "";
   formEmail.value = "";
   formMovil.value = "";
   formAsunto.value = "";
   formMensaje.value = "";
   
   Swal.fire({
        icon: 'success',
        title: 'Formulario enviado',
        text: 'El formulario ha sido enviado correctamente',
        showConfirmButton: false,
      });
  } else {
    event.preventDefault(); // Evita que el formulario se envíe si hay errores
  }

});



