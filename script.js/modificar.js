//const URL = "http://127.0.0.1:5000/"
const URL = "https://jnogueraroman.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            nombre: '',
            telefono: '',
            cantidad: '',
            email: '',
            mostrarDatosReserva: false,
        };
    },

    methods: {
        obtenerReserva() {
            fetch(URL + 'reservas/' + this.telefono)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        //Si la respuesta es un error, lanzamos una excepción para ser "catcheada" más adelante en el catch.
                        throw new Error('Error al obtener los datos de la reserva.')
                    }
                })

                .then(data => {
                    this.nombre = data.nombre;
                    this.cantidad = data.cantidad;
                    this.email = data.email;
                    this.mostrarDatosReserva = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('Telefono no encontrado.');
                 })
    },

    
    guardarCambios() {
        const formData = new FormData();
        formData.append('nombre', this.nombre);
        formData.append('telefono', this.telefono);
        formData.append('cantidad', this.cantidad);
        formData.append('email', this.email);

    //Utilizamos fetch para realizar una solicitud PUT a la API y guardar los cambios.
        fetch(URL + 'reservas/' + this.telefono, {
                method: 'PUT',
                body: formData,
        })
        .then(response => {
            //Si la respuesta es exitosa, utilizamos response.json() para parsear la respuesta en formato JSON.
                if(response.ok) {
                    return response.json()
            } else {
                //Si la respuesta es un error, lanzamos una excepción.
                throw new Error('Error al guardar los cambios de la reserva.')
            }
        })
        .then(data => {
            alert('Reserva actualizada correctamente.');
            this.limpiarFormulario();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al actualizar la reserva.');
        });
    },
    limpiarFormulario() {
        this.nombre = '';
        this.telefono = '';
        this.cantidad = '';
        this.email = '';
        this.imagen_url = '';
        this.mostrarDatosReserva = false;
        }
    }
});

app.mount('#app');