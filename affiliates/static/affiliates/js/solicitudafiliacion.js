document.addEventListener('DOMContentLoaded', function () {
    const detallesModalEl = document.getElementById('solicitudDetallesModal');
    if (!detallesModalEl) return;

    const detallesModal = new bootstrap.Modal(detallesModalEl);
    const tablaAfiliaciones = document.getElementById('afiliacionesTable');
    if (!tablaAfiliaciones) return;

    // Obtener las URLs base desde los atributos de datos de la tabla (DTL)
    const urlAprobarBase = tablaAfiliaciones.dataset.urlAprobarBase;
    const urlRechazarBase = tablaAfiliaciones.dataset.urlRechazarBase;

    // --- MANEJO DEL CLIC PARA VER DETALLES ---
    tablaAfiliaciones.addEventListener('click', function (evento) {
        const boton = evento.target.closest('button[data-bs-target="#solicitudDetallesModal"]');
        if (!boton) return;

        const url = boton.dataset.url;
        if (!url) return;

        detallesModal.show();
        limpiarYMostrarCargando(detallesModalEl);

        fetch(url)
            .then(response => response.ok ? response.json() : Promise.reject('Error en la respuesta del servidor'))
            .then(datos => {
                llenarModalConDatos(detallesModalEl, datos, urlAprobarBase, urlRechazarBase);
            })
            .catch(error => {
                console.error("Error al cargar detalles:", error);
                const modalBody = detallesModalEl.querySelector('.modal-body');
                modalBody.innerHTML = '<p class="text-center text-danger">No se pudieron cargar los detalles de la solicitud.</p>';
            });
    });

    // --- MANEJO DE CLICS EN BOTONES DE ACCIÓN (APROBAR/RECHAZAR) ---
    detallesModalEl.addEventListener('click', function (evento) {
        const botonAccion = evento.target.closest('.btn-aprobar, .btn-rechazar');
        if (!botonAccion) return;

        evento.preventDefault();
        const url = botonAccion.dataset.url;
        if (!url || url === '#') {
            console.error('URL de acción no válida.');
            return;
        }

        const accion = botonAccion.classList.contains('btn-aprobar') ? 'aprobar' : 'rechazar';
        const confirmacionMsg = `¿Estás seguro de que quieres ${accion} esta solicitud?`;

        if (confirm(confirmacionMsg)) {
            const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json'
                }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        detallesModal.hide();
                        alert(data.message || 'Acción completada con éxito.');
                        window.location.reload();
                    } else {
                        const errorContainer = detallesModalEl.querySelector('#modal-error-container');
                        errorContainer.innerHTML = `<div class="alert alert-danger">${data.message || 'Ocurrió un error.'}</div>`;
                    }
                })
                .catch(error => {
                    console.error("Error en la acción:", error);
                    const errorContainer = detallesModalEl.querySelector('#modal-error-container');
                    errorContainer.innerHTML = `<div class="alert alert-danger">Ocurrió un error de red al procesar la solicitud.</div>`;
                });
        }
    });
});

function limpiarYMostrarCargando(modalEl) {
    const campos = ['#modal-ticket', '#modal-fecha-envio', '#modal-nombre-usuario', '#modal-ruc-usuario', '#modal-email-usuario', '#modal-telefono-usuario', '#modal-razon-social', '#modal-nombre-comercial', '#modal-direccion'];
    campos.forEach(sel => {
        const elemento = modalEl.querySelector(sel);
        if (elemento) elemento.textContent = '';
    });
    modalEl.querySelector('#modal-estado-container').innerHTML = '';
    modalEl.querySelector('#modal-documentos-list').innerHTML = '<p class="text-muted small">Cargando...</p>';
    modalEl.querySelector('#modal-error-container').innerHTML = '';
}

function llenarModalConDatos(modalEl, datos, urlAprobarBase, urlRechazarBase) {
    modalEl.querySelector('#modal-ticket').textContent = `#${datos.id.toString().padStart(5, '0')}`;
    modalEl.querySelector('#modal-fecha-envio').textContent = datos.fecha_envio;

    let badge = `<span class="badge bg-secondary">${datos.estado_display}</span>`;
    if (datos.estado === 'APROBADO') badge = `<span class="badge bg-success">${datos.estado_display}</span>`;
    else if (datos.estado === 'RECHAZADO') badge = `<span class="badge bg-danger">${datos.estado_display}</span>`;
    else if (datos.estado === 'PENDIENTE') badge = `<span class="badge bg-warning text-dark">${datos.estado_display}</span>`;
    modalEl.querySelector('#modal-estado-container').innerHTML = badge;

    modalEl.querySelector('#modal-nombre-usuario').textContent = datos.solicitante.nombre;
    modalEl.querySelector('#modal-ruc-usuario').textContent = datos.solicitante.cedula_ruc;
    modalEl.querySelector('#modal-email-usuario').textContent = datos.solicitante.email;
    modalEl.querySelector('#modal-telefono-usuario').textContent = datos.solicitante.telefono;

    const tarjetaEmpresa = modalEl.querySelector('#tarjeta-empresa');
    if (datos.tipo === 'juridica' && datos.empresa) {
        modalEl.querySelector('#modal-razon-social').textContent = datos.empresa.razon_social;
        modalEl.querySelector('#modal-nombre-comercial').textContent = datos.empresa.nombre_comercial;
        modalEl.querySelector('#modal-direccion').textContent = datos.empresa.direccion;
        tarjetaEmpresa.style.display = 'block';
    } else {
        tarjetaEmpresa.style.display = 'none';
    }

    const docList = modalEl.querySelector('#modal-documentos-list');
    docList.innerHTML = '';
    if (datos.documentos && datos.documentos.length > 0) {
        datos.documentos.forEach(doc => {
            docList.innerHTML += `<a href="${doc.url}" target="_blank" class="list-group-item list-group-item-action"><i class="bi bi-file-earmark-arrow-down me-2"></i> ${doc.nombre}</a>`;
        });
    } else {
        docList.innerHTML = '<p class="text-muted small">No hay documentos adjuntos.</p>';
    }

    const btnAceptar = modalEl.querySelector('#btnModalAceptar');
    const btnRechazar = modalEl.querySelector('#btnModalRechazar');

    if (datos.estado === 'PENDIENTE') {
        btnAceptar.style.display = 'inline-block';
        btnRechazar.style.display = 'inline-block';
        // Construir URLs dinámicamente usando las URLs base y el ID de la solicitud
        btnAceptar.dataset.url = urlAprobarBase.replace('0', datos.id);
        btnRechazar.dataset.url = urlRechazarBase.replace('0', datos.id);
    } else {
        btnAceptar.style.display = 'none';
        btnRechazar.style.display = 'none';
    }
}