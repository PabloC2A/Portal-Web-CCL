// solicitudafiliantes/static/solicitudafiliantes/js/solicitudafiliacion.js

document.addEventListener('DOMContentLoaded', function() {

    // 1. Inicializa los tooltips de Bootstrap.
    // Esto hace que los títulos de los botones aparezcan al pasar el mouse.
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // 2. Animación de entrada para la tabla de afiliaciones.
    const afiliacionesTable = document.getElementById('afiliacionesTable');
    if (afiliacionesTable) {
        afiliacionesTable.style.opacity = '0';
        setTimeout(() => {
            afiliacionesTable.style.transition = 'opacity 0.8s ease-in';
            afiliacionesTable.style.opacity = '1';
        }, 100); 
    }

});