// AQUI SE GUARDAN LAS VALIDACIONES DE LOS FORMULARIOS //
// validaciones.js

document.addEventListener('DOMContentLoaded', (event) => {
    const fechaEntregaInput = document.getElementById('fecha_entrega');
    
    if (fechaEntregaInput) {
        // Obtener la fecha actual
        const today = new Date();
        const yyyy = today.getFullYear();
        const mm = String(today.getMonth() + 1).padStart(2, '0'); // Meses en JavaScript son de 0-11
        const dd = String(today.getDate()).padStart(2, '0');

        // Formatear la fecha en el formato YYYY-MM-DD
        const todayFormatted = `${yyyy}-${mm}-${dd}`;

        // Establecer el atributo min para el input de fecha
        fechaEntregaInput.setAttribute('min', todayFormatted);

        // Agregar un evento para validar al cambiar la fecha
        fechaEntregaInput.addEventListener('change', (e) => {
            const selectedDate = e.target.value;
            if (selectedDate < todayFormatted) {
                alert('La fecha de entrega no puede ser anterior al día de hoy.');
                e.target.value = todayFormatted; // Reestablecer la fecha al valor mínimo permitido
            }
        });
    }
});

