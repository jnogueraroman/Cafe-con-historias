const nombre = document.getElementById("nombre")
const apellido = document.getElementById("apellido")
const telefono = document.getElementById("telefono")
const email = document.getElementById("email")
const form = document.getElementById("form")
const parrafo = document.getElementById("warning")

form.addEventListener("submit", e=< {
 e.preventDefault()
 let enviar =false
 let warnings = ""
 let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
 if(nombre.value.length <2){
    warnings +=  'El nombre no es valido' <br>

 } 

 console.log (regexEmail.test(email.value))
 if(!regexEmail.test(email.value)){
    warnings +=  'El email no es valido' <br>
 }
})