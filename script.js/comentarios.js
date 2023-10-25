function comentarios() {
    fetch('https://jsonplaceholder.typicode.com/comments')
        .then(res => res.json())
        .then(res => {
            console.log(res)
            let contenidoHTML = ''

            for (let i = 0; i < 12; i++) {
                contenidoHTML += `
                    <div class="tarjeta">
                        
                        <h4> ${res[i].name}</h4>
                        <h6> ${res[i].body}</h6>
                    
                    </div>
                `
            }

            contenido.innerHTML = contenidoHTML
        })
        .catch(error => console.log("Ocurrió un error", error))
    }