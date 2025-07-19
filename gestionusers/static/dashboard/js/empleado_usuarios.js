// gestionusers/static/dashboard/js/empleado_usuarios.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('empleado_usuarios.js cargado y DOM listo.');

    // Inicialización de Tooltips de Bootstrap (esencial para los títulos de los botones)
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
            // Disparar evento de búsqueda o recargar tabla
        });
    }

    // Lógica para el selector de "Ítems por página"
    const itemsPerPageSelect = document.getElementById('itemsPerPageSelect');

    if (itemsPerPageSelect) {
        itemsPerPageSelect.addEventListener('change', function() {
            const itemsPerPage = this.value;
            console.log(`Ítems por página cambiados a: ${itemsPerPage}`);
            // Recargar tabla con nuevo límite
        });
    }

    // --- Lógica de Modales ---

    // 1. Modal de Creación de Usuario
    const crearUsuarioModalElement = document.getElementById('crearUsuarioModal');
    if (crearUsuarioModalElement) {
        const crearUsuarioModal = new bootstrap.Modal(crearUsuarioModalElement);
        const crearUsuarioForm = document.getElementById('crearUsuarioForm');
        const formMessages = document.getElementById('formMessages');

        // Manejar el envío del formulario del modal de creación
        crearUsuarioForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita el envío normal del formulario

            const formData = new FormData(this);

            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Indica que es una solicitud AJAX
                }
            })
            .then(response => {
                if (!response.ok) { // Si la respuesta no es OK (ej. 400 Bad Request)
                    return response.json().then(errorData => { throw errorData; });
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    formMessages.innerHTML = `<div class="alert alert-success" role="alert">${data.message}</div>`;
                    crearUsuarioForm.reset(); // Limpia el formulario
                    // Opcional: Cerrar modal después de un breve retraso para que el usuario vea el mensaje
                    setTimeout(() => {
                        crearUsuarioModal.hide();
                        location.reload(); // Recarga la página para ver el nuevo usuario
                    }, 1500);
                } else {
                    // Mostrar errores de validación
                    let errorsHtml = '<div class="alert alert-danger" role="alert"><ul>';
                    for (const field in data.errors) {
                        data.errors[field].forEach(error => {
                            errorsHtml += `<li><strong>${field}:</strong> ${error}</li>`;
                        });
                    }
                    errorsHtml += '</ul></div>';
                    formMessages.innerHTML = errorsHtml;
                }
            })
            .catch(errorData => {
                // Manejar errores de red o errores específicos lanzados
                let errorMessage = 'Ocurrió un error inesperado.';
                if (errorData && errorData.errors) {
                    let errorsHtml = '<div class="alert alert-danger" role="alert"><ul>';
                    for (const field in errorData.errors) {
                        errorData.errors[field].forEach(error => {
                            errorsHtml += `<li><strong>${field}:</strong> ${error}</li>`;
                        });
                    }
                    errorsHtml += '</ul></div>';
                    formMessages.innerHTML = errorsHtml;
                } else {
                     formMessages.innerHTML = `<div class="alert alert-danger" role="alert">${errorMessage}</div>`;
                }
                console.error('Error al enviar formulario de creación:', errorData);
            });
        });

        // Limpiar mensajes y formulario al cerrar el modal de creación
        crearUsuarioModalElement.addEventListener('hidden.bs.modal', function () {
            crearUsuarioForm.reset();
            formMessages.innerHTML = ''; // Limpia los mensajes
        });
    }

    // 2. Modal de Edición de Usuario
    const editarUsuarioModalElement = document.getElementById('editarUsuarioModal');
    if (editarUsuarioModalElement) {
        const editarUsuarioModal = new bootstrap.Modal(editarUsuarioModalElement);
        const editarUsuarioForm = document.getElementById('editarUsuarioForm');
        const editFormMessages = document.getElementById('editFormMessages');

        editarUsuarioModalElement.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget; // Botón que disparó el modal
            const userId = button.getAttribute('data-user-id'); // Obtener ID del usuario

            // Aquí se haría una solicitud AJAX para obtener los datos del usuario y rellenar el formulario
            // y también para establecer la acción del formulario.
            // Ejemplo:
            // fetch(`/dashboard/usuarios/${userId}/editar/`) // Tu URL para obtener el formulario de edición
            //     .then(response => response.json()) // O response.text() si devuelves HTML
            //     .then(data => {
            //         // Suponiendo que 'data' contiene el HTML del formulario pre-llenado o los datos para llenarlo
            //         editarUsuarioForm.innerHTML = data.html_form; // Si devuelves HTML
            //         editarUsuarioForm.action = `/dashboard/usuarios/${userId}/editar/`; // Establecer la acción del formulario
            //     })
            //     .catch(error => console.error('Error al cargar datos de edición:', error));
            
            // Llenar el formulario con datos de ejemplo por ahora
            // editFormMessages.innerHTML = ''; // Limpiar mensajes anteriores
            // console.log(`Cargando datos para editar usuario ID: ${userId}`);
        });

        // Manejar el envío del formulario del modal de edición (similar al de creación)
        editarUsuarioForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);

            fetch(this.action, {
                method: 'POST', // O 'PUT'/'PATCH' si tu API lo soporta
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    // 'X-CSRFToken': obtenerCsrfToken(), // Necesitas una función para obtener el token CSRF
                }
            })
            .then(response => {
                 if (!response.ok) { return response.json().then(errorData => { throw errorData; }); }
                 return response.json();
            })
            .then(data => {
                if (data.success) {
                    editFormMessages.innerHTML = `<div class="alert alert-success" role="alert">${data.message}</div>`;
                    setTimeout(() => { editarUsuarioModal.hide(); location.reload(); }, 1500);
                } else {
                    let errorsHtml = '<div class="alert alert-danger" role="alert"><ul>';
                    for (const field in data.errors) { data.errors[field].forEach(error => { errorsHtml += `<li><strong>${field}:</strong> ${error}</li>`; }); }
                    errorsHtml += '</ul></div>';
                    editFormMessages.innerHTML = errorsHtml;
                }
            })
            .catch(errorData => {
                let errorMessage = 'Ocurrió un error inesperado al actualizar.';
                if (errorData && errorData.errors) {
                    let errorsHtml = '<div class="alert alert-danger" role="alert"><ul>';
                    for (const field in errorData.errors) { errorData.errors[field].forEach(error => { errorsHtml += `<li><strong>${field}:</strong> ${error}</li>`; }); }
                    errorsHtml += '</ul></div>';
                    editFormMessages.innerHTML = errorsHtml;
                } else {
                     editFormMessages.innerHTML = `<div class="alert alert-danger" role="alert">${errorMessage}</div>`;
                }
                console.error('Error al enviar formulario de edición:', errorData);
            });
        });
        // Limpiar mensajes al cerrar el modal de edición
        editarUsuarioModalElement.addEventListener('hidden.bs.modal', function () {
            // editarUsuarioForm.reset(); // No resetear para poder ver los datos al reabrir si hay errores
            editFormMessages.innerHTML = ''; 
        });
    }

    // 3. Modal de Detalles de Usuario
    const usuarioDetallesModalElement = document.getElementById('usuarioDetallesModal');
    if (usuarioDetallesModalElement) {
        const usuarioDetallesModal = new bootstrap.Modal(usuarioDetallesModalElement);

        usuarioDetallesModalElement.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget; // Botón que disparó el modal
            const userId = button.getAttribute('data-user-id'); // Obtener ID del usuario

            // Aquí se haría una solicitud AJAX para obtener los detalles del usuario
            // Ejemplo:
            // fetch(`/dashboard/usuarios/${userId}/detalles/`) // Tu URL para obtener detalles
            //     .then(response => response.json())
            //     .then(data => {
            //         // Llenar los spans con los datos del usuario
            //         document.getElementById('detalleCedula').textContent = data.cedula;
            //         document.getElementById('detalleNombre').textContent = data.nombre_completo;
            //         document.getElementById('detalleCorreo').textContent = data.email;
            //         document.getElementById('detalleRol').textContent = data.rol;
            //         document.getElementById('detalleEstado').textContent = data.estado;
            //         document.getElementById('detalleUltimaActualizacion').textContent = data.ultima_actualizacion;
            //     })
            //     .catch(error => console.error('Error al cargar detalles:', error));
            
            // Llenar con datos de ejemplo por ahora
            document.getElementById('detalleCedula').textContent = 'Ej. 1104721489';
            document.getElementById('detalleNombre').textContent = 'Ej. Juan Pérez';
            document.getElementById('detalleCorreo').textContent = 'ejemplo@correo.com';
            document.getElementById('detalleRol').textContent = 'Socio';
            document.getElementById('detalleEstado').textContent = 'Activo';
            document.getElementById('detalleUltimaActualizacion').textContent = '18/Jul/2025 18:00';
            console.log(`Cargando detalles para usuario ID: ${userId}`);

            // Manejar el botón "Editar" dentro del modal de detalles
            const btnEditarDesdeDetalles = document.getElementById('btnEditarDesdeDetalles');
            if (btnEditarDesdeDetalles) {
                btnEditarDesdeDetalles.onclick = () => {
                    usuarioDetallesModal.hide(); // Ocultar el modal de detalles
                    // Disparar la apertura del modal de edición para este usuario
                    // Esto requeriría programáticamente abrir el modal de edición
                    // new bootstrap.Modal(document.getElementById('editarUsuarioModal')).show();
                    // Y cargar los datos en él
                    console.log(`Intento de editar usuario ID: ${userId} desde detalles.`);
                };
            }
        });
    }

    // --- Funciones auxiliares (necesarias para AJAX si CSRF token no está en cada formulario) ---
    // function obtenerCsrfToken() {
    //     const cookieValue = document.cookie.split('; ')
    //         .find(row => row.startsWith('csrftoken='))
    //         .split('=')[1];
    //     return cookieValue;
    // }

    // --- Espacio para tus animaciones y scripts de frontend específicos ---
    const usersTable = document.getElementById('usersTable');
    if (usersTable) {
        usersTable.style.opacity = '0';
        setTimeout(() => {
            usersTable.style.transition = 'opacity 0.8s ease-in';
            usersTable.style.opacity = '1';
        }, 100); 
    }
});