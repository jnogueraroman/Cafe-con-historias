const nombre = document.getElementById("nombre")
const apellido = document.getElementById("apellido")
const telefono = document.getElementById("telefono")
const email = document.getElementById("email")
const form = document.getElementById("form")
const parrafo = document.getElementById("warning")

form.addEventListener("submit", e=> {
 e.preventDefault()
 let boton =false
 let warnings = ""
 let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
 
 parrafo.innerHTML = ""
 if( nombre.value.length <2){
    warnings +='El nombre no es valido' <br>
    boton = true
     }
    if( apellido.value.length <2){
      warnings +='El apellido no es valido' <br>
      boton = true
       }
      if( telefono.value.length <10){
         warnings +='El numero no es valido' <br>
         boton = true
      } 

 console.log (regexEmail.test(email.value))
 if(!regexEmail.test(email.value)){
    warnings +=  'El email no es valido' <br>
 }
 if(boton){
   parrafo.innerHTML = warnings

 } else{
   parrafo.innerHTML = "ENVIADO NOS COMUNICAMOS A LA BREVEDAD"
 }
})