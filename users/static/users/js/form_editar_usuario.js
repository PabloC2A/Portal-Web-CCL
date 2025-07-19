document.addEventListener('DOMContentLoaded', function () {
    // Selecciona el modal de edición
    const editarModal = document.getElementById('editarUsuarioModal');

    // Escucha el evento que se dispara JUSTO ANTES de que el modal se muestre
    editarModal.addEventListener('show.bs.modal', function (evento) {
        // Identifica el botón que activó el modal
        const boton = evento.relatedTarget;

        // Extrae la información de los atributos data-* del botón
        const urlActualizar = boton.getAttribute('data-url-actualizar');
        const nombre = boton.getAttribute('data-nombre');
        const apellido = boton.getAttribute('data-apellido');
        const email = boton.getAttribute('data-email');
        const rol = boton.getAttribute('data-rol');
        const esActivo = boton.getAttribute('data-activo') === 'true';

        // Encuentra el formulario dentro del modal
        const formulario = editarModal.querySelector('#editarUsuarioForm');

        // Establece la URL correcta en la 'action' del formulario
        formulario.action = urlActualizar;

        // Rellena los campos del formulario con los datos del usuario
        formulario.querySelector('#id_first_name').value = nombre;
        formulario.querySelector('#id_last_name').value = apellido;
        formulario.querySelector('#id_email').value = email;
        formulario.querySelector('#id_rol').value = rol;
        formulario.querySelector('#id_is_active').checked = esActivo;
    });
});