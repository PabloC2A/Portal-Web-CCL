// solicitudafiliantes/static/solicitudafiliantes/js/solicitudafiliacion.js

document.addEventListener('DOMContentLoaded', function() {

    // 1. Habilita los tooltips de Bootstrap en toda la página.
    // Esto hace que los títulos de los botones aparezcan al pasar el mouse.
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });


    // 2. Prepara los popovers de confirmación para los botones de acción.
    const actionButtons = document.querySelectorAll('button[data-action="aceptar"], button[data-action="rechazar"]');

    actionButtons.forEach(button => {
        const action = button.getAttribute('data-action');
        const isAccept = action === 'aceptar';
        const title = isAccept ? 'Aceptar Solicitud' : 'Rechazar Solicitud';
        const buttonClass = isAccept ? 'btn-success' : 'btn-danger';

        // Contenido HTML del popover con los botones de confirmación.
        const popoverContent = `
            <div class="text-center">
                <p class="mb-2">¿Estás seguro?</p>
                <button class="btn btn-sm ${buttonClass} btn-confirm-action">Sí</button>
                <button class="btn btn-sm btn-outline-secondary btn-cancel-action">No</button>
            </div>
        `;

        // Crea la instancia del popover para cada botón.
        new bootstrap.Popover(button, {
            container: 'body',
            placement: 'top',
            html: true,
            title: title,
            content: popoverContent,
            sanitize: false, // Requerido para usar HTML en el contenido.
        });
    });


    // 3. Maneja el cierre de los popovers.
    // Esto escucha clics en toda la página para cerrar el popover activo.
    document.body.addEventListener('click', function(event) {
        const target = event.target;
        
        // Busca el popover que está actualmente abierto.
        const activePopoverTrigger = document.querySelector('[aria-describedby]');
        if (!activePopoverTrigger) return; // Si no hay ninguno, no hace nada.

        // Cierra el popover si se hace clic en "Sí", "No", o en cualquier lugar fuera del popover.
        if (target.classList.contains('btn-confirm-action') ||
            target.classList.contains('btn-cancel-action') ||
            !target.closest('.popover')) {
            
            bootstrap.Popover.getInstance(activePopoverTrigger).hide();
        }
    });

});