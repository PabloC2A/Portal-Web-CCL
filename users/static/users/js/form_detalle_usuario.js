document.addEventListener('DOMContentLoaded', function () {
    const detallesModal = document.getElementById('usuarioDetallesModal');
    const editarModalEl = document.getElementById('editarUsuarioModal');
    const editarModal = new bootstrap.Modal(editarModalEl);

    detallesModal.addEventListener('show.bs.modal', function (evento) {
        const boton = evento.relatedTarget;

        // Extrae la información del botón
        const nombre = boton.getAttribute('data-nombre-completo');
        const cedula = boton.getAttribute('data-cedula');
        const correo = boton.getAttribute('data-correo');
        const rol = boton.getAttribute('data-rol');
        const estado = boton.getAttribute('data-estado');
        const urlEditar = boton.getAttribute('data-url-editar');

        // Rellena el modal de detalles (esto no cambia)
        detallesModal.querySelector('#detalleNombre').textContent = nombre;
        detallesModal.querySelector('#detalleCedula').textContent = cedula;
        detallesModal.querySelector('#detalleCorreo').textContent = correo;
        detallesModal.querySelector('#detalleRol').textContent = rol;
        detallesModal.querySelector('#detalleEstado').textContent = estado;

        // --- LÓGICA ACTUALIZADA PARA EL BOTÓN 'EDITAR' ---
        const btnEditar = detallesModal.querySelector('#btnEditarDesdeDetalles');
        btnEditar.onclick = function () {
            // 1. Prepara el formulario de edición antes de mostrarlo
            const formularioEditar = editarModalEl.querySelector('#editarUsuarioForm');
            const nombreCompleto = nombre.split(' ');

            // Asigna la URL correcta al 'action' del formulario de edición
            formularioEditar.action = urlEditar;

            // Rellena los campos del formulario de edición
            formularioEditar.querySelector('#id_first_name').value = nombreCompleto[0] || '';
            formularioEditar.querySelector('#id_last_name').value = nombreCompleto.slice(1).join(' ') || '';
            formularioEditar.querySelector('#id_email').value = correo;
            formularioEditar.querySelector('#id_rol').value = rol.toLowerCase(); // 'socio' o 'empleado'
            formularioEditar.querySelector('#id_is_active').checked = (estado === 'Activo');

            // 2. Cierra el modal de detalles
            const modalDetallesBootstrap = bootstrap.Modal.getInstance(detallesModal);
            modalDetallesBootstrap.hide();

            // 3. Abre el modal de edición ya preparado
            editarModal.show();
        }
    });
});