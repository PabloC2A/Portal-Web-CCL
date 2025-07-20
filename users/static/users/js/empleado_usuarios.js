// users/static/users/js/empleado_usuarios.js

document.addEventListener('DOMContentLoaded', function() {

    // 1. Inicializa los tooltips de Bootstrap.
    // Esto hace que los títulos de los botones aparezcan al pasar el mouse.
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

});