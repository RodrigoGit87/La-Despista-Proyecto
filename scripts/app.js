document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('feedbackForm');
    const successMessage = document.getElementById('successMessage');

    form.addEventListener('submit', (e) => {
        // Prevenir el recargo de la página
        e.preventDefault();

        // Recoger los datos del formulario
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        // Convertir los checkboxes a Verdadero(True) o Falso(False)
        data.dataConsent = formData.has('dataConsent');
        data.promoConsent = formData.has('promoConsent');

        // Ponemos el botón en estado 'Enviando...'
        const btn = form.querySelector('.submit-btn');
        const btnText = btn.querySelector('span');
        const originalText = btnText.innerText;
        btnText.innerText = 'Enviando...';
        btn.style.opacity = '0.8';
        btn.disabled = true;

        // -- LA MAGIA: ENVIAMOS LOS DATOS A PYTHON --
        fetch('http://127.0.0.1:5000/recibir_datos', {
            method: 'POST', // Usamos POST porque estamos enviando (no pidiendo)
            headers: {
                'Content-Type': 'application/json' // Le decimos a Python que va en formato JSON
            },
            body: JSON.stringify(data) // Empaquetamos los datos
        })
        .then(respuesta => respuesta.json()) // Esperamos a que Python responda
        .then(resultado_servidor => {
            console.log("El servidor dice:", resultado_servidor);
            
            // Ocultar formulario y mostrar mensaje de éxito al cliente
            form.classList.add('hidden');
            successMessage.classList.remove('hidden');
        })
        .catch(error => {
            console.error("Error al enviar al servidor:", error);
            // Si hay un error, dejamos que vuelvan a intentarlo
            btnText.innerText = 'Error. Intentar de nuevo';
            btn.style.opacity = '1';
            btn.disabled = false;
        });
    });
});
