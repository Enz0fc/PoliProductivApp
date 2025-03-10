function getCSRFToken() {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
            return cookie.substring("csrftoken=".length, cookie.length);
        }
    }
    return "";
}
function publicar(datosApublicar){
    fetch("http://127.0.0.1:8000/PoliProductivApp/",{
        method: "POST",
        headers: {
            "Content-Type": "application/json", // Indicar que enviamos JSON
            "X-CSRFToken": getCSRFToken()  // Obtener el token desde las cookies
        },
        body: JSON.stringify(datosApublicar)
    })
    .then(response => response.json()) // Convertir la respuesta a JSON
    .then(data => {
        console.log("Respuesta del servidor:", data);   // Mostrar respuesta en consola
    })
    .catch(error => console.error("Error al enviar datos:", error)); // Capturar errores
}
function actualizarContexto() {
    fetch('/PoliProductivApp/actualizarContexto/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Asegúrate de incluir el token CSRF
        }
    })
    .then(response => {
        console.log("Respuesta del servidor:", response);
        return response.json();  // Intenta parsear la respuesta como JSON
    })
    .then(data => {
        console.log("Datos parseados:", data);  // Verifica la estructura de la respuesta
        console.log("nuevoDiv:", data.nuevoDiv);  // Verifica el contenido de nuevoDiv

        document.getElementById('paso3').innerHTML = data.nuevoDiv;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('paso3').style.display = 'block';
}



function irAlPaso(n){
    if (n === 2){
        let carreraSeleccionada = document.getElementById("carrera").value;
        console.log(carreraSeleccionada);

        document.getElementById("paso1").style.display = "none";
        document.getElementById("paso2").style.display = "block";

        datos = {
            carrera: carreraSeleccionada
        };
        publicar(datos)
    }
    if (n === 3 ){
        let checkboxes = document.querySelectorAll("input[name='semestre']:checked");
        let semestreSeleccionado = Array.from(checkboxes).map(checkbox => parseInt(checkbox.value, 10));    
        console.log("Seleccionados:", semestreSeleccionado);

        document.getElementById("paso2").style.display = "none";
        
        datos = {
            semestres: semestreSeleccionado
        };
        publicar(datos)
        actualizarContexto()
        
    }
}


$(document).ready(function() {
    $('#carrera').change(function() {
        var carreraId = $(this).val();
        if (carreraId) {
            $.ajax({
                url: '{% url "get_semestres" %}',
                data: {
                    'carrera_id': carreraId
                },
                success: function(data) {
                    $('#semestre').html('<option value="">Selecciona un semestre</option>');
                    $.each(data, function(index, semestre) {
                        $('#semestre').append('<option value="' + semestre.id + '">' + semestre.numero + '</option>');
                    });
                    $('#semestre').prop('disabled', false);
                }
            });
        } else {
            $('#semestre').html('<option value="">Selecciona un semestre</option>').prop('disabled', true);
            $('#materia').html('<option value="">Selecciona una materia</option>').prop('disabled', true);
            $('#seccion').html('<option value="">Selecciona una sección</option>').prop('disabled', true);
        }
    });

    $('#semestre').change(function() {
        var semestreId = $(this).val();
        if (semestreId) {
            $.ajax({
                url: '{% url "get_materias" %}',
                data: {
                    'semestre_id': semestreId
                },
                success: function(data) {
                    $('#materia').html('<option value="">Selecciona una materia</option>');
                    $.each(data, function(index, materia) {
                        $('#materia').append('<option value="' + materia.id + '">' + materia.nombre + '</option>');
                    });
                    $('#materia').prop('disabled', false);
                }
            });
        } else {
            $('#materia').html('<option value="">Selecciona una materia</option>').prop('disabled', true);
            $('#seccion').html('<option value="">Selecciona una sección</option>').prop('disabled', true);
        }
    });

    $('#materia').change(function() {
        var materiaId = $(this).val();
        if (materiaId) {
            $.ajax({
                url: '{% url "get_secciones" %}',
                data: {
                    'materia_id': materiaId
                },
                success: function(data) {
                    $('#seccion').html('<option value="">Selecciona una sección</option>');
                    $.each(data, function(index, seccion) {
                        $('#seccion').append('<option value="' + seccion.id + '">' + seccion.nombre + '</option>');
                    });
                    $('#seccion').prop('disabled', false);
                }
            });
        } else {
            $('#seccion').html('<option value="">Selecciona una sección</option>').prop('disabled', true);
        }
    });
});