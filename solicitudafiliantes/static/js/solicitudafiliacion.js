// solicitudafiliantes/static/js/solicitudafiliacion.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('solicitudafiliacion.js cargado y DOM listo.');

    // Inicialización de Tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Lógica para el botón "Limpiar Búsqueda"
    const clearSearchButton = document.getElementById('clearSearchButton');
    const searchInput = document.getElementById('searchInput');

    if (clearSearchButton && searchInput) {
        clearSearchButton.addEventListener('click', function() {
            searchInput.value = '';
            // Aquí irían tus animaciones o lógica de UI después de limpiar la búsqueda.
        });
    }

    // Lógica para el selector de "Ítems por página"
    const itemsPerPageSelect = document.getElementById('itemsPerPageSelect');

    if (itemsPerPageSelect) {
        itemsPerPageSelect.addEventListener('change', function() {
            const itemsPerPage = this.value;
            console.log(`Ítems por página cambiados a: ${itemsPerPage}`);
            // Aquí irían tus animaciones o lógica de UI después de cambiar los ítems por página.
        });
    }

    // --- Lógica para los botones de acción de la tabla (Ver Detalles, Aceptar, Rechazar) ---
    // Esto se manejaría si usas modales o envíos AJAX para las acciones.

    // Ejemplo: Abrir modal de detalles al hacer clic en el botón "Ver Detalles"
    // const detallesModalElement = document.getElementById('solicitudDetallesModal');
    // if (detallesModalElement) {
    //     const detallesModal = new bootstrap.Modal(detallesModalElement);
    //     document.querySelectorAll('.btn-outline-info[data-bs-target="#solicitudDetallesModal"]').forEach(button => {
    //         button.addEventListener('click', function() {
    //             const solicitudId = this.getAttribute('data-solicitud-id');
    //             console.log(`Ver detalles de la solicitud ID: ${solicitudId}`);
    //             // Aquí harías una llamada AJAX para obtener los detalles de la solicitud
    //             // y rellenar el modal antes de mostrarlo.
    //             // detallesModal.show();
    //         });
    //     });
    // }

    // Ejemplo: Manejar botones de Aceptar/Rechazar (requiere confirmación y backend)
    // document.querySelectorAll('.btn-success[data-action="aceptar"], .btn-danger[data-action="rechazar"]').forEach(button => {
    //     button.addEventListener('click', function() {
    //         const solicitudId = this.getAttribute('data-solicitud-id');
    //         const action = this.getAttribute('data-action'); // 'aceptar' o 'rechazar'
    //         console.log(`Solicitud ID: ${solicitudId}, Acción: ${action}`);
    //         // Aquí harías una solicitud AJAX al backend para procesar la acción.
    //         // fetch(`/dashboard/afiliaciones/${solicitudId}/${action}/`, { method: 'POST', headers: { 'X-CSRFToken': obtenerCsrfToken() } })
    //         // .then(response => response.json())
    //         // .then(data => { if (data.success) { location.reload(); } else { alert('Error: ' + data.message); } });
    //     });
    // });

    // --- Espacio para tus animaciones y scripts de frontend específicos ---
    const afiliacionesTable = document.getElementById('afiliacionesTable');
    if (afiliacionesTable) {
        afiliacionesTable.style.opacity = '0';
        setTimeout(() => {
            afiliacionesTable.style.transition = 'opacity 0.8s ease-in';
            afiliacionesTable.style.opacity = '1';
        }, 100); 
    }
    // --------------------------------------------------------------------
});