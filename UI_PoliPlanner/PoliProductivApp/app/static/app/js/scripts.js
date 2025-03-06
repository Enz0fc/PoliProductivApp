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
    .then(data => console.log("Respuesta del servidor:", data)) // Mostrar respuesta en consola
    .catch(error => console.error("Error al enviar datos:", error)); // Capturar errores
}
function actualizarContexto(){
    fetch('/PoliProductivApp/actualizarContexto/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Asegúrate de incluir el token CSRF
        }
    })
    .then(response => response)
    .then(data =>{
        console.log(data);  // Verifica la estructura de la respuesta
        console.log(data.nuevos_inputs);  // Verifica el contenido de nuevos_inputs

        document.getElementById('paso3').innerHTML = data.nuevoDiv;
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


