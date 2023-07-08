function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "block";
  }
  
  // Cierra el modal cuando se hace clic fuera de él
  window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
      event.target.style.display = "none";
    }
  }
  