const URL = "http://127.0.0.1:5000/"
// Realizamos la solicitud GET al servidor para obtener todos las reservas
fetch(URL + 'reservas')
.then(function (response) {
if (response.ok) {
    return response.json();  
} else {
    // Si hubo un error, lanzar explícitamente una excepción
    // para ser "catcheada" más adelante
        throw new Error('Error al obtener las reservas.');
    }
    })
    .then(function (data) {
         let tablaReservas = document.getElementById('tablaReservas');
    // Iteramos sobre los productos y agregamos filas a la tabla
    for (let reserva of data) {
        let fila = document.createElement('tr');
        fila.innerHTML = '<td>' + reserva.nombre + '</td>' +
            '<td>' + reserva.telefono + '</td>' +
            '<td>' + reserva.cantidad + '</td>' +
            '<td>' + reserva.email + '</td>' +

    //Una vez que se crea la fila con el contenido del producto, 
    //se agrega a la tabla utilizando el método appendChild del elemento
    //tablaProductos.
    tablaReservas.appendChild(fila);
    }
    })
    .catch(function (error) {
    // En caso de error
    alert('Error al agregar la reserva.');
    console.error('Error:', error);
    })